# faq-from-docs

Generate FAQ entries from Markdown documentation with an injected LLM. This library ensures every answer is grounded in the documentation by requiring the LLM to provide a verbatim quote from the source, performing near-duplicate filtering, and verifying inputs against strict constraints.

## The Problem

Support teams often struggle to keep FAQs in sync with documentation. Using a generic LLM often leads to hallucinations or answers without provenance. This library forces the LLM to cite a specific documentation section and verifies that the provided quote exists exactly as written in the source text.

## Installation

`pip install faq-from-docs`

## Usage

```python
from faq_from_docs import RecordedLLM, generate_faq, render_markdown, split_sections

sections = split_sections("# Install\nRun pip install pkg.\n", "guide.md")
reply = '[{"question": "How do I install?", "answer": "Run pip install pkg.", "quote": "Run pip install pkg."}]'
faq = generate_faq(sections, RecordedLLM([reply]))
markdown = render_markdown(faq)
print(markdown)
```

## Public API Summary

- `split_sections(markdown: str, source: str) -> list[Section]`
- `generate_faq(sections: Sequence[Section], llm: LLMPort, *, ... ) -> Faq`
- `render_markdown(faq: Faq) -> str`

- `FaqError`: Raised on `input_too_large` or `invalid_option`.
- Limits: 2,000,000 character global input cap; strict bounds on question, answer, and quote lengths.
- Options: Configurable `per_section` count, `max_tokens` budget, and `min_section_chars` for skipping short text blocks.

## Why not just prompt a chatbot?

Directly prompting a general chatbot lacks the mandatory grounding step. `faq-from-docs` performs an automated verification step for every candidate answer: if the LLM cannot find a verbatim quote in the cited section, the answer is rejected.

See [docs/SECURITY.md](docs/SECURITY.md) for a detailed threat model and defense against injection.