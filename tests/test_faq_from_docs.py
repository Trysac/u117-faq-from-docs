"""Behavior tests for the public API of faq_from_docs."""

from __future__ import annotations

import pytest

import faq_from_docs


def test_normalize_trims_and_lowercases() -> None:
    assert faq_from_docs.normalize("  Hello World ") == "hello world"


@pytest.mark.parametrize("value", ["", "   ", "\t\n"])
def test_normalize_rejects_blank_input(value: str) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        faq_from_docs.normalize(value)


def test_version_is_semver() -> None:
    parts = faq_from_docs.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
