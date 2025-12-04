# cli/main.py
import logging
import sys

from pathlib import Path

from library_manager import Book, LibraryInventory

LOG_FORMAT = "%(asctime)s — %(levelname)s — %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger("library_cli")

def prompt_non_empty(prompt_msg: str) -> str:
    while True:
        val = input(prompt_msg).strip()
        if val:
            return val
        print("Input cannot be empty. Try again.")

def show_menu():
    print("\nLibrary Inventory Manager")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search by Title")
    print("6. Search by ISBN")
    print("7. Exit")

def main():
    # Optional: allow custom catalog path via env arg
    catalog_path = Path("catalog.json")
    inv = LibraryInventory(catalog_path=catalog_path)

    while True:
        show_menu()
        choice = input("Choose an option [1-7]: ").strip()
        if choice == "1":
            title = prompt_non_empty("Title: ")
            author = prompt_non_empty("Author: ")
            isbn = prompt_non_empty("ISBN: ")
            book = Book(title=title, author=author, isbn=isbn)
            if inv.add_book(book):
                print("Book added successfully.")
            else:
                print("A book with that ISBN already exists.")
        elif choice == "2":
            isbn = prompt_non_empty("ISBN to issue: ")
            if inv.issue_book(isbn):
                print("Book issued successfully.")
            else:
                print("Issue failed — book not found or already issued.")
        elif choice == "3":
            isbn = prompt_non_empty("ISBN to return: ")
            if inv.return_book(isbn):
                print("Book returned successfully.")
            else:
                print("Return failed — book not found or already available.")
        elif choice == "4":
            all_books = inv.display_all()
            if not all_books:
                print("No books in inventory.")
            else:
                print("\nAll Books:")
                for line in all_books:
                    print(" -", line)
        elif choice == "5":
            q = prompt_non_empty("Title query: ")
            results = inv.search_by_title(q)
            if not results:
                print("No books match that title.")
            else:
                print(f"Found {len(results)} book(s):")
                for b in results:
                    print(" -", b)
        elif choice == "6":
            isbn = prompt_non_empty("ISBN to search: ")
            b = inv.search_by_isbn(isbn)
            if b:
                print("Found:", b)
            else:
                print("No book with that ISBN.")
        elif choice == "7":
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid option. Enter a number between 1 and 7.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
