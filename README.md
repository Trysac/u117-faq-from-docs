# faq-from-docs

[![PyPI version](https://img.shields.io/pypi/v/trysac-faq-from-docs)](https://pypi.org/project/trysac-faq-from-docs/)
[![License: MIT](https://img.shields.io/pypi/l/trysac-faq-from-docs)](LICENSE)
[![CI](https://github.com/Trysac/u117-faq-from-docs/actions/workflows/ci.yml/badge.svg)](https://github.com/Trysac/u117-faq-from-docs/actions/workflows/ci.yml)

Generate FAQ entries from Markdown documentation with an injected LLM, one cited section per answer, verbatim quote checks, question deduplication and Markdown output

## Problem

Describe in two or three sentences the concrete problem this utility solves, who hits it, and what
they do today without it. Replace this paragraph when the first real feature lands.

## Install

```sh
pip install trysac-faq-from-docs
# or
uv add trysac-faq-from-docs
```

Requires Python 3.10 or newer. No runtime dependencies.

## Usage

```python
import faq_from_docs

# normalize() trims surrounding whitespace and lower-cases the text.
print(faq_from_docs.normalize("  Hello World "))  # -> "hello world"

# Blank input is rejected explicitly instead of returning an empty string.
try:
    faq_from_docs.normalize("   ")
except ValueError as exc:
    print(f"rejected: {exc}")
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md) and [decisions](docs/decisions/)
- [Testing](docs/TESTING.md) and [security](docs/SECURITY.md)
- [Project record](docs/PROJECT.md) and [stack](docs/STACK.md)
- [Changelog](CHANGELOG.md) and [contributing guide](CONTRIBUTING.md)

## License

[MIT](LICENSE) (c) 2026 Miguel Gomez
