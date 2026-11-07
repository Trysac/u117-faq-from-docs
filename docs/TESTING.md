# Testing

Tests are located in `tests/test_faq_from_docs.py` and are designed for execution with `pytest`.

## Coverage Areas

- **Section Splitting**: Verifies parsing of ATX headings (1-6 levels), handling of fenced code blocks (which contain no headers), collisions in slug generation (e.g., `-2`), and processing of documents without any headers (the 'intro' section).
- **Verbatim Verification**: Ensures that quotes must exist exactly within the section source, normalized for whitespace.
- **Constraint Validation**: Exercises the rejection logic for `invalid_json`, `invalid_question` (missing `?` or length), `too_long` answers, `quote_not_found`, and `duplicate` questions based on token Jaccard similarity.
- **Formatting**: Tests backslash escaping for `[`, `]`, `<`, and `>` to ensure safe Markdown output.
- **Flow Control**: Confirms that sections under `min_section_chars` are skipped and the `per_section` limit is strictly enforced with `over_limit` codes.
- **Safety**: Validates that telemetry events do not leak restricted document content.