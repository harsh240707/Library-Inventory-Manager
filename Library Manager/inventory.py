# library_manager/inventory.py
import json
import logging
from pathlib import Path
from typing import List, Optional

from .book import Book

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, catalog_path: Optional[Path] = None):
        self.catalog_path = Path(catalog_path) if catalog_path else Path("catalog.json")
        self.books: List[Book] = []
        # ensure directory exists for file if nested
        try:
            if self.catalog_path.parent and not self.catalog_path.parent.exists():
                self.catalog_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        self.load()

    def add_book(self, book: Book) -> bool:
        """Add book if ISBN not duplicate. Return True if added."""
        if self.search_by_isbn(book.isbn):
            logger.info("Attempt to add duplicate ISBN %s", book.isbn)
            return False
        self.books.append(book)
        logger.info("Book added: %s", book)
        self.save()
        return True

    def search_by_title(self, title_query: str) -> List[Book]:
        q = title_query.lower().strip()
        return [b for b in self.books if q in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        isbn = str(isbn).strip()
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self) -> List[str]:
        return [str(b) for b in self.books]

    def issue_book(self, isbn: str) -> bool:
        b = self.search_by_isbn(isbn)
        if not b:
            logger.info("Issue failed: ISBN %s not found", isbn)
            return False
        if b.issue():
            logger.info("Book issued: %s", b)
            self.save()
            return True
        logger.info("Issue failed: Book already issued %s", b)
        return False

    def return_book(self, isbn: str) -> bool:
        b = self.search_by_isbn(isbn)
        if not b:
            logger.info("Return failed: ISBN %s not found", isbn)
            return False
        if b.return_book():
            logger.info("Book returned: %s", b)
            self.save()
            return True
        logger.info("Return failed: Book already available %s", b)
        return False

    def save(self) -> None:
        try:
            data = [b.to_dict() for b in self.books]
            with self.catalog_path.open("w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=2, ensure_ascii=False)
            logger.info("Catalog saved to %s", self.catalog_path)
        except Exception as e:
            logger.exception("Failed to save catalog: %s", e)

    def load(self) -> None:
        if not self.catalog_path.exists():
            logger.info("Catalog file not found: %s — starting empty inventory", self.catalog_path)
            self.books = []
            return
        try:
            with self.catalog_path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            if not isinstance(data, list):
                raise ValueError("Catalog JSON root must be a list")
            self.books = [Book.from_dict(item) for item in data]
            logger.info("Loaded %d books from %s", len(self.books), self.catalog_path)
        except Exception as e:
            logger.exception("Failed to load catalog; starting with empty list: %s", e)
            self.books = []
