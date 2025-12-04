# library_manager/__init__.py
"""
Library Manager Package
Exports:
 - Book
 - LibraryInventory
"""
from .book import Book
from .inventory import LibraryInventory

__all__ = ["Book", "LibraryInventory"]
