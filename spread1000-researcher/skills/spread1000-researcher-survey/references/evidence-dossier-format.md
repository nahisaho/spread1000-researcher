# Evidence Dossier Format

Read this reference when executing Phase 1 or when constructing an Evidence Dossier.

## Structure

```markdown
## Identity
- name: {研究者名}
- affiliation: {所属機関}
- department: {研究科・学部}
- research_area: {主要研究分野}
- profile_urls: {プロフィール URL リスト}
- orcid: {ORCID ID（判明した場合）}

## Publications
- key_papers:
  - title: {論文タイトル}
    journal: {掲載誌}
    year: {年}
    citations: {被引用数}
- total_papers_estimate: {推定総論文数}
- h_index_estimate: {推定 h-index}
- evidence_confidence: high/medium/low

## Funding
- grants:
  - name: {資金名}
    agency: {配分機関}
    period: {期間}
    amount_category: {規模カテゴリ: 大型/中規模/小規模}
- evidence_confidence: high/medium/low

## Innovation Signals
- novel_methods: {新手法}
- new_fields: {新分野開拓}
- patents: {特許}
- evidence_confidence: high/medium/low

## International Activity
- intl_collaborations: {国際共同研究}
- invited_talks: {招待講演}
- overseas_experience: {海外経験}
- evidence_confidence: high/medium/low

## Interdisciplinary Impact
- cross_field_work: {分野横断研究}
- industry_collaboration: {産学連携}
- social_impact: {社会実装}
- evidence_confidence: high/medium/low

## Career Stage
- estimated_stage: early/mid/senior
- mentoring: {指導実績}
- lab_management: {研究室運営}
- evidence_confidence: high/medium/low

## Sources
| # | URL | 取得日 | 信頼性 | 内容 |
|---|-----|--------|--------|------|
```

## Confidence Level Definitions

| Level | Definition |
|-------|-----------|
| high | 公式ページ・学術データベースから確認。複数ソースで裏付け |
| medium | 単一ソースのみ、または間接的な証拠。追加確認推奨 |
| low | 情報が見つからない、または信頼性が低い。スコアリングでは N/A 扱い |
