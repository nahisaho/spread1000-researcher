---
name: spread1000-researcher-evaluate
description: |
  Evidence Dossier を入力として SPReAD-1000 申請者を 6 軸 5 段階でスコアリングする。
  Use when エビデンスドシエが準備済みで、研究者の多軸評価・採点を行う。
---

# SPReAD-1000 Researcher Evaluate

Evidence Dossier を基に 6 軸 × 5 段階でスコアリングし、総合評価を算出する。

## Use This Skill When

- Evidence Dossier（`evidence-dossier.md`）が既に生成・承認済みである。
- 「評価して」「スコアリング」「採点」等のキーワードがある。
- Full Workflow の Phase 2 として呼び出された。

## Required Inputs

- `evidence-dossier.md`: 承認済みエビデンスドシエ

## Workflow

1. **Evidence Dossier の読み込み**
   - `evidence-dossier.md` を読み込む
   - 各セクションの evidence_confidence を確認

2. **6 軸スコアリング**
   - Read `references/scoring-rubric.md` when applying per-axis scoring criteria
   - 各軸について:
     a. エビデンスを確認
     b. confidence レベルに応じた評価ルールを適用
     c. スコア（1-5）と根拠を記録

3. **Confidence ベースの評価ルール**
   - `high`: 通常のスコアリング基準を適用
   - `medium`: スコア上限を 4 とし、「追加確認推奨」と注記
   - `low`: スコアを「N/A（情報不足）」とし、総合評価から除外

4. **総合評価の算出**
   - 有効軸（confidence: high/medium）のスコア平均を算出
   - 有効軸数が 4 未満の場合:「評価保留 — 追加情報が必要」と明記
   - 総合スコア: 平均値を 5 段階に変換
     - 4.5〜5.0 → S（卓越）
     - 3.5〜4.4 → A（優秀）
     - 2.5〜3.4 → B（良好）
     - 1.5〜2.4 → C（発展途上）
     - 1.0〜1.4 → D（要改善）

5. **評価結果の保存**
   - `evaluation.md` として出力

## Deliverables

- `evaluation.md`: 6 軸スコア + 総合評価 + 根拠

## Quality Gates

- [ ] 全 6 軸にスコアまたは「N/A（情報不足）」が記録されている
- [ ] 各スコアに Evidence Dossier からの根拠引用がある
- [ ] confidence: low の軸にスコア 4-5 が付与されていない
- [ ] 総合評価の算出方法が明示されている
- [ ] 有効軸数が 4 未満の場合「評価保留」と記載されている

## Gotchas

- confidence: low のエビデンスでスコア 1 を付与しない。「N/A」とし総合評価から除外する
- キャリア段階によって同じ実績でも適切なスコアが異なる。若手（助教・講師）は将来性を、シニア（教授）は蓄積を重視する
- 分野間でのスコア比較は無効。理論物理と臨床医学では論文数・被引用数の基準が大きく異なる
- 総合評価は加重平均ではなく単純平均を使用する。特定軸の重み付けはユーザーが判断すべき事項

## Validation Loop

1. 6 軸のスコアリングを実行
2. チェック:
   - confidence: low の軸が不当にスコア化されていないか
   - 各スコアに根拠があるか
   - 総合評価の算出が正しいか
3. 不合格の場合:
   - confidence ルールを再適用
   - 根拠の欠落を補完
   - 総合評価を再計算
4. 全ゲート通過後、Phase 3 へ進む
