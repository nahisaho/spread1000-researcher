---
name: spread1000-researcher-survey
description: |
  SPReAD-1000 申請者の公開情報を Web 検索で収集し、構造化エビデンスドシエを生成する。
  Use when 研究者名と所属機関が与えられ、論文・資金・研究活動の情報を収集する。
---

# SPReAD-1000 Researcher Survey

研究者の公開情報を Web 検索で収集し、6 軸評価に必要なエビデンスを構造化データとして出力する。

## Use This Skill When

- 研究者名と所属機関が入力され、情報収集を求められた。
- 「調べて」「サーベイ」「調査して」等のキーワードがある。
- Full Workflow の Phase 1 として呼び出された。

## Required Inputs

- 研究者名（日本語・英語いずれか）
- 所属機関名

## Workflow

1. **検索戦略の策定**
   - 日本語クエリ: `"{研究者名}" "{所属}" 研究`
   - 英語クエリ: `"{researcher name}" "{affiliation}" research`
   - 追加クエリ: `"{研究者名}" 科研費`, `"{researcher name}" Google Scholar`

2. **情報収集（6 軸対応）**

   **研究実績**:
   - 主要論文（タイトル、掲載誌、年、被引用数）
   - 総論文数推定、h-index 推定
   - Web 検索: `"{name}" publications OR 論文 OR paper`

   **外部資金**:
   - 科研費・CREST・さきがけ等の獲得実績
   - Web 検索: `"{name}" KAKEN OR 科研費 OR grant`

   **革新性シグナル**:
   - 新手法・特許・新分野開拓の兆候
   - Web 検索: `"{name}" 特許 OR patent OR novel OR 新手法`

   **国際活動**:
   - 国際共著、海外機関との共同研究、招待講演
   - Web 検索: `"{name}" international OR collaboration OR invited`

   **学際性・波及効果**:
   - 分野横断研究、産学連携、社会実装
   - Web 検索: `"{name}" interdisciplinary OR 産学連携 OR 社会実装`

   **キャリア段階**:
   - 職位、博士取得年、指導実績
   - Web 検索: `"{name}" "{affiliation}" professor OR 准教授 OR 助教`

3. **Evidence Dossier 生成**
   - Read `references/evidence-dossier-format.md` when constructing the Evidence Dossier
   - Read `references/example-evidence-dossier.md` when first-time execution or output quality uncertain
   - 各セクションに `evidence_confidence: high/medium/low` を付与
   - ソース URL と取得日を記録
   - `evidence-dossier.md` として保存
   - Run `scripts/validate_dossier.py evidence-dossier.md` to verify structural validity

4. **⏸️ ユーザーにエビデンス承認を求める**

## Deliverables

- `evidence-dossier.md`: 構造化エビデンスドシエ（AGENTS.md の Evidence Dossier Format 準拠）

## Quality Gates

- [ ] 日本語・英語の両方で検索を実施した
- [ ] 6 軸すべてのセクションが Evidence Dossier に含まれている
- [ ] 各セクションに evidence_confidence が付与されている
- [ ] ソース URL と取得日が全エビデンスに記録されている
- [ ] 検索で情報が見つからなかった軸は「情報不足」と明記されている

## Gotchas

- 日本語名の研究者は英語表記（ローマ字）でも検索する。論文は英語名で発表されていることが多い
- Google Scholar や ResearchGate のプロフィールが見つかれば効率的に情報を集約できるが、プロフィールがない研究者も多い
- KAKEN（科研費データベース）は Web 検索経由でアクセスできるが、最新年度のデータは反映が遅れる場合がある
- 所属機関の表記ゆれに注意（例: 「東大」「東京大学」「University of Tokyo」「UTokyo」）

## Validation Loop

1. Evidence Dossier を生成
2. チェック:
   - 6 軸すべてのセクションが存在するか
   - confidence レベルが付与されているか
   - ソース URL が有効か（最低1つ確認）
3. `scripts/validate_dossier.py` を実行して構造チェック
4. 不合格の場合:
   - 欠落セクションを追加検索で補完
   - confidence を再評価
   - バリデーションスクリプトを再実行
5. 全ゲート通過後、ユーザー承認へ進む
