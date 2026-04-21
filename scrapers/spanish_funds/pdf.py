"""PDF text extraction using pypdf."""
from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(path: Path) -> str:
    """Extract concatenated text from all pages of a PDF.

    Raises FileNotFoundError if path does not exist.
    Returns empty string for PDFs with no extractable text.
    """
    if not path.exists():
        raise FileNotFoundError(str(path))
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)
