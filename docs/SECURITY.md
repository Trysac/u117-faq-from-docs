# Security

## Threat Model

`faq-from-docs` processes untrusted documentation text and potentially adversarial LLM responses.

### Defended Threats

- **Prompt Injection & Tag Breakouts**: User documentation is wrapped in `<section title="...">` tags. The title attribute is escaped (using `&`, `"`, `'`), and any `</section` case-insensitive sequences within the document text are neutralized to `&lt;/section`. System prompts instruct the model to ignore any instructions inside the document section.
- **Hallucinations**: Every accepted answer is validated against the source. An answer candidate must contain a `quote` that is a whitespace-collapsed substring of the section text. Failures are rejected with `quote_not_found`.
- **Denial of Service**: 
    - Global input size is strictly capped at 2,000,000 characters, raising `FaqError('input_too_large')`.
    - Bounds on string length (question, answer, quote) prevent memory exhaustion.
    - Sections with length < `min_section_chars` are skipped entirely.
- **Information Disclosure**: Telemetry emitted via `on_event` is limited to section identifiers and outcome counts. Sensitive document sentinels are never included.

### Not Defended

- The library assumes the provided `LLMPort` implementation is trusted; malicious implementations can ignore system prompts or bypass verification logic.