# Architecture

`trysac-faq-from-docs` parses documentation into addressable sections, prompts an injected LLM adapter (`LLMPort`) for candidate question-answer-quote triples per section, verifies that every quote is an exact verbatim substring of the cited section text, filters near-duplicate questions, and renders an anchored Markdown FAQ.

## Pipeline

1. **Section Splitting (`split_sections`)**:
   - Scans ATX Markdown headings outside fenced code blocks.
   - Generates deterministic NFKD slugs with collision counters (`-2`, `-3`).
   - Handles leading text as `#intro` sections.

2. **Candidate Generation & Verification (`generate_faq`)**:
   - Enforces an input size limit (`max_input_chars = 2_000_000`).
   - Skips short sections (`< min_section_chars`).
   - Wraps section text in `<section title="...">` tags, escaping title attributes and neutralizing `</section>` injection payloads.
   - Enforces strict response verification:
     - JSON array parsing with code block stripping fallback.
     - Type schema validation (`missing_field`).
     - Question constraints: 5-200 characters ending with `?` (`invalid_question`).
     - Answer constraints: 1-1000 characters (`too_long`).
     - Quote verification: 1-500 characters, whitespace-collapsed substring of section text (`quote_not_found`).
     - Jaccard similarity >= 0.8 deduplication (`duplicate`).
     - Per-section quota enforcement (`over_limit`).

3. **Markdown Rendering (`render_markdown`)**:
   - Generates `# FAQ` with `## <question>` and markdown links back to the source section anchor.
   - Backslash-escapes `[`, `]`, `<`, and `>` characters.
