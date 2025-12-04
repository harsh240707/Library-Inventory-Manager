# library_manager/book.py
from dataclasses import dataclass, asdict

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: str = "available"  # either "available" or "issued"

    def __post_init__(self):
        # normalize status
        self.status = self.status.lower()

    def __str__(self) -> str:
        return f"{self.title} — {self.author} (ISBN: {self.isbn}) [{self.status}]"

    def to_dict(self) -> dict:
        """Return a JSON-serializable dict."""
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict):
        """Create Book instance from dict (used when loading JSON)."""
        return cls(
            title=d.get("title", ""),
            author=d.get("author", ""),
            isbn=str(d.get("isbn", "")),
            status=d.get("status", "available")
        )

    def issue(self) -> bool:
        """Issue the book. Return True if successful, False if already issued."""
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self) -> bool:
        """Return the book. Return True if successful, False if already available."""
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self) -> bool:
        return self.status == "available"
