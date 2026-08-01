# 📋 Task Manager CLI

> A lightweight, keyboard-driven task management tool for developers who value speed and simplicity.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/dev-awa/task-manager.svg)](https://github.com/dev-awa/task-manager/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/dev-awa/task-manager.svg)](https://github.com/dev-awa/task-manager/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/dev-awa/task-manager.svg)](https://github.com/dev-awa/task-manager/commits/main)

---

## 📖 About

**Task Manager CLI** is a simple yet powerful command-line application built with Python that helps you manage your daily tasks efficiently. With persistent JSON storage, status tracking (TODO/DOING/DONE), and an intuitive CLI, it's perfect for developers who prefer terminal-based productivity tools.

This project was built as a hands-on learning experience to master:
- Python OOP and data modeling
- Working with dates and statuses
- File I/O and JSON serialization
- Professional Git workflow (branches, PRs, code reviews)
- CLI design and user experience

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ➕ **Add Tasks** | Create tasks with a title and optional description |
| 📋 **List Tasks** | View all tasks with status, description, and creation date |
| ✅ **Complete Tasks** | Mark tasks as done with a simple command |
| 🗑️ **Delete Tasks** | Remove tasks you no longer need |
| 💾 **Persistent Storage** | All tasks are automatically saved to a JSON file |
| 📅 **Date Tracking** | Each task stores creation and last-updated timestamps |
| 🚀 **Lightweight** | No external dependencies — just Python! |
| 🎨 **User-Friendly** | Colorful emoji-based output and helpful error messages |

---

## 📸 Screenshots

```

📋 Your Tasks (2/4 completed)
============================================================

1. Buy groceries
   Status: ✅ DONE
   Description: From supermarket
   📅 Created: 2026-07-30

---

1. Read book
   Status: ⏳ TODO
   Description: Finish chapter 3
   📅 Created: 2026-07-30

---

1. Write project docs
   Status: 🔄 DOING
   📅 Created: 2026-07-31

---

1. Call plumber
   Status: ⏳ TODO
   Description: Fix kitchen sink
   📅 Created: 2026-07-31

---

```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning)

### Step 1: Clone the repository

```bash
git clone git@github.com:dev-awa/task-manager.git
cd task-manager
```

Step 2: (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

Note: This project has no external dependencies, so requirements.txt is currently empty.

---

📖 Usage

Basic Commands

Command Description

python task_manager.py add "Title" "Description" Add a new task

python task_manager.py list Show all tasks

python task_manager.py complete <number> Mark a task as done

python task_manager.py delete <number> Delete a task

python task_manager.py help Show help message

Examples

```bash
# Add a task with title and description
python task_manager.py add "Buy milk" "From the supermarket"

# Add a task without description
python task_manager.py add "Call mom"

# List all tasks
python task_manager.py list

# Complete task number 2
python task_manager.py complete 2

# Delete task number 1
python task_manager.py delete 1

# Show help
python task_manager.py help
```

Example Session

```bash
$ python task_manager.py add "Buy groceries"
✅ Task added: Buy groceries

$ python task_manager.py add "Read book" "Finish chapter 3"
✅ Task added: Read book

$ python task_manager.py list
📋 Your Tasks (0/2 completed)
============================================================
1. Buy groceries
   Status: ⏳ TODO
   📅 Created: 2026-07-30
------------------------------------------------------------
2. Read book
   Status: ⏳ TODO
   Description: Finish chapter 3
   📅 Created: 2026-07-30
------------------------------------------------------------

$ python task_manager.py complete 1
✅ Task completed: Buy groceries

$ python task_manager.py list
📋 Your Tasks (1/2 completed)
============================================================
1. Buy groceries
   Status: ✅ DONE
   📅 Created: 2026-07-30
------------------------------------------------------------
2. Read book
   Status: ⏳ TODO
   Description: Finish chapter 3
   📅 Created: 2026-07-30
------------------------------------------------------------
```

---

📁 Project Structure

```
task-manager/
├── src/
│   ├── models/
│   │   └── task.py              # Task class with status and dates
│   ├── services/
│   │   └── file_service.py      # JSON file storage (CRUD operations)
│   └── cli/
│       └── commands.py          # CLI command implementations
├── tests/
│   ├── test_task.py             # Unit tests for Task model
│   └── test_file_service.py     # Unit tests for file service
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies (empty)
└── task_manager.py              # Main entry point
```

---

📦 Dependencies

Package Version Purpose

Python 3.8+ Core language

json Built-in JSON serialization

os Built-in File system operations

datetime Built-in Date and time handling

Zero external dependencies! This project uses only Python's standard library.

---

🔮 Feature Improvements

Future enhancements planned for this project:

· Add DOING (IN_PROGRESS) status

· Add due dates for tasks

· Add search by title or description

· Add filter by status

· Add sorting by date or status

· Add task tags/categories

· Add export/import (CSV, JSON)

· Add database support (SQLite)

· Add color-coded output using rich library

· Add interactive mode with menu

· Add unit tests with pytest

---

🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch: git checkout -b feature/your-feature
3. Make your changes and commit: git commit -m "feat: add your feature"
4. Push to your fork: git push origin feature/your-feature
5. Open a Pull Request

Please make sure your code follows the existing style and includes appropriate comments.

---

🔄 Development Workflow

This project follows a professional Git workflow:

```bash
# 1. Create a new branch for each feature
git checkout -b feature/your-feature

# 2. Make your changes and commit
git add .
git commit -m "feat: add your feature"

# 3. Push to GitHub
git push origin feature/your-feature

# 4. Create a Pull Request on GitHub

# 5. After PR is merged, delete the branch
git checkout main
git pull origin main
git branch -d feature/your-feature
```

Branch Naming Convention

| Branch Type     | Naming Pattern          | Example                  |
|-----------------|-------------------------|--------------------------|
| **Feature**     | feature/description     | feature/task-model       |
| **Chore**       | chore/description       | chore/initial-setup      |
| **Docs**        | docs/description        | docs/final-polish        |
| **Bugfix**      | bugfix/description      | bugfix/status-transition |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](https://github.com/dev-awa/task-manager/blob/main/LICENSE) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/dev-awa/task-manager/blob/main/LICENSE)

---

🙏 Acknowledgements

· Inspired by various CLI tools in the Python ecosystem

· Built as a learning project to master Git and Python

· Thanks to the open-source community for inspiration

---

## 📬 Contact & Support

| Platform | Link |
|----------|------|
| GitHub Profile | [github.com/dev-awa](https://github.com/dev-awa) |
| Repository | [github.com/dev-awa/task-manager](https://github.com/dev-awa/task-manager) |
| Report Issues | [github.com/dev-awa/task-manager/issues](https://github.com/dev-awa/task-manager/issues) |
| Email | [miladzadehsoltani@gmail.com](mailto:miladzadehsoltani@gmail.com) |

---

## ⭐ Support This Project

If you find this project useful, please consider giving it a star ⭐ on GitHub!  
It helps others discover it and motivates further development.

[![GitHub stars](https://img.shields.io/github/stars/dev-awa/task-manager.svg)](https://github.com/dev-awa/task-manager)

[⭐ Click here to star this project on GitHub](https://github.com/dev-awa/task-manager)

---

Built with ❤️ using Python