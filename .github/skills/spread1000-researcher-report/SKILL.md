---
name: spread1000-researcher-report
description: |
  6 軸評価結果を基に SPReAD-1000 申請者の構造化評価レポートを生成する。
  Use when 評価結果（evaluation.md）が準備済みで、最終レポートを作成する。
---

# SPReAD-1000 Researcher Report

評価結果を基に、SPReAD-1000 審査用の構造化評価レポートを生成する。

## Use This Skill When

- `evaluation.md` が既に生成されている。
- 「レポート」「報告書」「まとめ」等のキーワードがある。
- Full Workflow の Phase 3 として呼び出された。

## Required Inputs

- `evidence-dossier.md`: エビデンスドシエ
- `evaluation.md`: 6 軸評価結果

## Workflow

1. **入力ファイルの読み込み**
   - `evidence-dossier.md` と `evaluation.md` を読み込む

2. **レポート生成**
   - Reuse `assets/report-template.md` when producing the evaluation report
   - テンプレートの各セクションにデータを充填
   - ユーザーの入力言語に合わせて記述

3. **レポートの保存**
   - `report.md` として保存
   - ファイル名規則: `report-{researcher-name}-{YYYYMMDD}.md`

4. **⏸️ 最終承認をユーザーに求める**

## Deliverables

- `report-{researcher-name}-{YYYYMMDD}.md`: 最終評価レポート

## Quality Gates

- [ ] テンプレートの全必須セクションが含まれている
- [ ] 各軸のスコアと根拠が記載されている
- [ ] 総合評価ランク（S/A/B/C/D）が明記されている
- [ ] 情報不足の軸が適切に表記されている
- [ ] ソース一覧が末尾に含まれている
- [ ] ファイルとして保存されている

## Gotchas

- テンプレートの構造を変更しない。セクションの追加は可だが、既存セクションの削除は禁止
- 日付は ISO 8601 形式（YYYY-MM-DD）で統一する
- レポートに研究者の個人連絡先（メール、電話番号）を含めない
- 総合評価が「評価保留」の場合、ランク（S/A/B/C/D）を付与せず「保留」と明記する

## Validation Loop

1. レポートを生成
2. チェック:
   - テンプレートの全セクションが存在するか
   - スコアと根拠の対応が正しいか
   - ファイルが正しく保存されたか
3. 不合格の場合:
   - 欠落セクションを追加
   - スコア—根拠の不整合を修正
   - 再保存
4. 全ゲート通過後、ユーザー承認へ進む
