**📚 Library Inventory Manager**
* A lightweight and modular Command-Line Application for managing a book catalog in a campus library environment using Object-Oriented Programming, JSON persistence, exception handling, and a menu-driven CLI.
This project helps library staff maintain records of available and issued books along with searching and tracking functionality.

**🚀 Features**
* Add new books with title, author, and ISBN
* Issue and return books with status tracking
* Search books by title or ISBN
* View entire inventory in a formatted view
* Data persistence using JSON file handling
* Handles missing or corrupted files gracefully
* Built using OOP principles (encapsulation, magic methods, abstraction)
* Structured as a Python package
* Logging support
* Extensible design for UI or database integration in the future

**🧠 Learning Objectives**
* By working on this project, you will understand:
* Class design using attributes and methods
* Python magic methods like __str__() and __init__()
* Encapsulation and modular programming
* Persistent storage using JSON with pathlib
* Logging and exception handling
* Creating CLI applications
* Packaging and organizing a real-world project

**🏗 Project Structure**
``library-inventory-manager-harsh/
├── catalog.json
├── requirements.txt
├── .gitignore
├── README.md
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   └── inventory.py
└── cli/
    └── main.py``

**📥 Installation & Setup**
1️⃣ Clone the repository
git clone https://github.com/harsh240707/library-inventory-manager.git
cd library-inventory-manager
2️⃣ Ensure Python is installed (Python 3.8+ recommended)
python --version
3️⃣ Run the CLI
python cli/main.py

**Screenshots**
<img width="1903" height="800" alt="image" src="https://github.com/user-attachments/assets/21091161-15f0-49dc-a4ef-eeac84d45aba" />

**📌 Usage**
When running the application, a command menu will appear:
Library Inventory Manager
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search by Title
6. Search by ISBN
7. Exit
Enter an option number to perform an action.

**🗂 JSON Data Storage**
All book data is stored inside:
``catalog.json``
Example saved data:

``[
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "isbn": "9780735211292",
    "status": "available"
  }
]``

**🧪 Testing (Optional Future Addition)**
Create a tests/ folder and write tests using unittest or pytest.
Example test file structure:

``tests/
 └── test_inventory.py``

**🔧 Requirements**
This project uses only Python's standard library.
Still, for clarity:
``pathlib
json
logging``

**🌟 Future Enhancements**
* GUI version with Tkinter or PyQt
* MySQL or SQLite database integration
* REST API version with Flask or FastAPI
* Web dashboard for real-time inventory insights

``👨‍💻 Author``
Harsh Yadav
