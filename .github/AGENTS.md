---
name: spread1000-researcher
description: |
  SPReAD-1000 申請者の研究実績・資金獲得・革新性・国際活動・学際性・キャリア段階を
  Web 検索で調査し、6 軸 5 段階で総合評価レポートを生成する。
  Use when 研究者名と所属を入力して SPReAD-1000 申請者を評価する、研究者サーベイを行う、
  または申請者の研究力を多軸評価する。
---

# SPReAD-1000 Researcher Survey v0.1.0

申請者の公開情報を Web 検索で収集し、6 軸 × 5 段階で評価レポートを生成する。
Route work to the narrowest sub-skill, save all outputs as files.

## Core Rules

- `report.md` はユーザーの入力言語と同じ言語で記述する。
- すべての成果物をファイルに保存する。チャットのみに結果を残さない。
- 最も狭い範囲にマッチするサブスキルにルーティングする。

## Routing Rules

### WHEN/DO Dispatch

WHEN: 研究者の情報を調べる、サーベイする、論文・資金・業績を調査する
DO: → `spread1000-researcher-survey`

WHEN: 評価する、スコアリングする、採点する、6軸で評価する
DO: → `spread1000-researcher-evaluate`

WHEN: レポートを生成する、報告書を作成する、評価結果をまとめる
DO: → `spread1000-researcher-report`

### Task Classification

1. 研究者名・所属が入力され「調べて」「サーベイ」が含まれるか？
   - YES → `spread1000-researcher-survey`
   - NO → next
2. エビデンスドシエが既にあり「評価」「スコア」が含まれるか？
   - YES → `spread1000-researcher-evaluate`
   - NO → next
3. <Decision question>: 評価結果が既にあり「レポート」「報告」が含まれるか？
   - YES → `spread1000-researcher-report`
   - NO → next
4. キーワードが不明確か？
   - YES → ユーザーに目的を確認してから適切なスキルへルーティング
   - NO → Full Workflow を実行

### Full Workflow

Phase 0 → 研究者同定: 名前・所属から正しい人物を特定（同姓同名対策）
Phase 1 → `spread1000-researcher-survey`: Web 検索で情報収集 ⏸️ エビデンス承認
Phase 2 → `spread1000-researcher-evaluate`: 6 軸 5 段階スコアリング
Phase 3 → `spread1000-researcher-report`: 評価レポート生成 ⏸️ 最終承認

### Urgency Triage

| Urgency | Keywords | Workflow |
|---------|----------|---------|
| Normal | (default) | Full Workflow（全Phase） |
| Urgent | "急ぎ", "urgent" | Phase 0+1+2 を統合、簡易レポート |
| Critical | "即時", "immediately" | サマリーのみ出力 |

## Phase 0: 研究者同定

Full Workflow 開始時に必ず実行する:

1. 研究者名と所属機関を確認
2. Web 検索で以下の同定シグナルを2つ以上取得:
   - 研究室/個人ページ URL
   - ORCID / Google Scholar プロフィール
   - 所属学部・研究科
   - 主要研究分野
3. 同姓同名の候補が複数ある場合 → ユーザーに選択を求める ⏸️
4. 同定完了後、Phase 1 に進む

## Evidence Dossier Format

Phase 1 の出力として構造化エビデンスドシエを生成する。Phase 2・3 はこのデータを消費する。

Read `skills/spread1000-researcher-survey/references/evidence-dossier-format.md` when executing Phase 1 or constructing an Evidence Dossier.

## Verification Loop

PLAN → EXECUTE → VERIFY → REPORT → LOG

## Quality Gates

- [ ] 研究者が正しく同定されている（2+ 同定シグナル）
- [ ] エビデンスドシエの全セクションに confidence レベルが付与されている
- [ ] 各軸のスコアに根拠（エビデンス引用）が紐付いている
- [ ] 証拠不足の軸は「情報不足」と明記し、不当な低評価をしていない
- [ ] レポートがファイルとして保存されている

## Prohibited Operations

- 非公開情報（個人の連絡先、給与、私生活）の収集・記載
- 証拠なしでのスコア確定（推測のみでの評価は禁止）
- 他の申請者との比較ランキング（個別評価のみ）
- PII（個人識別情報）の不必要な記録

## Data Handling & Confidentiality

- 収集した情報は評価目的のみに使用する
- ソース URL と取得日を必ず記録する
- 評価レポートには個人の連絡先情報を含めない

## Gotchas

- Web 検索で見つからない ≠ 実績がない。`evidence_confidence: low` と明記し、スコア1を自動的に付与しない
- 同姓同名の研究者が多い分野（例: 田中、鈴木）では Phase 0 の同定ステップを省略しない
- 日本語と英語で異なる情報が出る場合がある。両方の言語で検索すること
- 科研費データベース（KAKEN）の情報は Web 検索で取得可能だが、最新年度が反映されていない場合がある
- キャリア段階によって同じ実績でも評価が異なる。若手の将来性とシニアの蓄積を同列に比較しない
