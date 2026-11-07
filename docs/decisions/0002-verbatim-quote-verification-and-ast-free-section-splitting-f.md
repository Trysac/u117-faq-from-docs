# Verbatim quote verification and AST-free section splitting for grounded FAQs

Status: accepted (generated, pending human review)

## Context

Support and product teams need accurate FAQs synchronized with source Markdown documentation. Generative models commonly hallucinate ungrounded facts or attribute answers to inaccurate source locations. The library must run with standard library dependencies only while reliably splitting ATX headings and verifying citations.

## Decision

We implemented `split_sections` using deterministic regex-based ATX parsing outside fenced code blocks with NFKD slug generation. In `generate_faq`, sections are passed to an LLMPort protocol adapter in an XML-like tag environment with escaped attributes and neutralized closing tags. Candidate entries must supply a verbatim quote matching a whitespace-collapsed substring in the source section, pass length and syntax validation, and satisfy token Jaccard similarity <= 0.8 against previously accepted questions.

## Consequences

FAQs generated through this pipeline are strictly grounded with explicit citations back to documentation sections. No answers without valid source quotes are accepted. Standard library only ensures minimal overhead and zero dependency maintenance.
