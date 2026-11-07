# Project Record

`faq-from-docs` provides a deterministic, grounded framework for generating FAQs from existing Markdown documentation.

## Objective

To transform technical documentation into a structured, verifiable FAQ database using Large Language Models, ensuring that every generated answer is directly attributable to the source documentation.

## Scope

- **Documentation Parsing**: ATX heading-based section splitting with slug generation and collision handling.
- **Verification**: Strict validation of LLM-generated JSON, including length bounds, verbatim quote substring checks, and question deduplication via Jaccard similarity (>= 0.8).
- **Output**: Rendered Markdown output with backslash-escaped structural characters.

## Out-of-Scope

- Implementing a command-line interface for production LLM providers.
- Generating HTML output or external documentation site integration.
- Automated web crawling or scraping of documentation.
- Qualitative answer scoring or ranking of LLM outputs beyond schema validation.

## Factory run u117 (measured from API usage)

| Phase | Model | Batch | Input | Output | Cache write | Cache read | Cost (USD) |
|---|---|---|---|---|---|---|---|
| generation | gemini-3.8-flash | yes | 4334 | 11274 | 0 | 0 | 0.0228 |
| fix-1 | gemini-3.8-flash | no | 22156 | 1777 | 0 | 43686 | 0.0266 |
| fix-2 | gemini-3.8-flash | no | 27162 | 447 | 0 | 70902 | 0.0274 |
| audit | gemini-3.1-flash-lite | no | 64679 | 280 | 0 | 136192 | 0.0200 |
| docs | gemini-3.1-flash-lite | no | 172961 | 1418 | 0 | 0 | 0.0454 |

Total: $0.1421. Prices: Anthropic list prices.
