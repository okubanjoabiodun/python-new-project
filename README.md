# 📝 Task Tracker

A simple and interactive **command-line Task Tracker** built with Python. This project allows users to create, view, edit, and delete tasks directly from the terminal.

The project was created as part of the **Task Tracker project challenge from roadmap.sh**.

🔗 **Project Challenge:**
https://roadmap.sh/projects/task-tracker

---

## 🚀 Features

* ➕ Create new tasks
* 👀 View all tasks
* ✏️ Edit existing tasks
* 🗑️ Delete tasks
* 📌 Track task status
* 💻 Interactive command-line interface
* 🐍 Built entirely with Python

---

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* Basic CRUD operations

---

## 📂 Project Structure

```text
task-tracker/
│
├── task_tracker.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/task-tracker.git
```

### 2. Navigate into the project

```bash
cd task-tracker
```

### 3. Run the application

```bash
python task_tracker.py
```

---

## 🎮 How to Use

When the application starts, you will see an interactive menu:

```text
===== TASK TRACKER =====

1. Create task
2. View tasks
3. Edit task
4. Delete task
5. Exit

Choose an option:
```

### ➕ Create a Task

Choose option `1` and enter your task.

```text
Enter task: Study Python

Task created successfully!
```

---

### 👀 View Tasks

Choose option `2` to display your tasks.

```text
Your Tasks:

1. Study Python - Pending
2. Practice Nmap - Pending
```

---

### ✏️ Edit a Task

Choose option `3`, select the task number, and enter the new task name.

```text
Enter task number to edit: 1
Enter new task name: Study Python for 2 hours

Task updated successfully!
```

---

### 🗑️ Delete a Task

Choose option `4`, select the task you want to remove, and the application will delete it.

```text
Enter task number to delete: 2

Deleted: Practice Nmap
```

---

## 🧠 How Tasks Are Stored

Tasks are stored using a Python list containing dictionaries.

Example:

```python
tasks = [
    {
        "title": "Study Python",
        "completed": False
    },
    {
        "title": "Practice Nmap",
        "completed": False
    }
]
```

Each task contains:

* `title` — The name of the task
* `completed` — The current task status

---

## 🔄 CRUD Operations

This project demonstrates the basic **CRUD** concept:

| Operation | Function            |
| --------- | ------------------- |
| Create    | Add a new task      |
| Read      | View existing tasks |
| Update    | Edit a task         |
| Delete    | Remove a task       |

---

## 📚 What I Learned

Building this project helped me practice:

* Python lists
* Python dictionaries
* Loops
* Conditional statements
* User input
* Data manipulation
* Adding and removing items
* Updating existing data
* Building an interactive CLI application
* Basic CRUD application design

---

## 🔮 Future Improvements

Planned improvements include:

* [ ] Save tasks permanently using JSON
* [ ] Add task completion functionality
* [ ] Add task descriptions
* [ ] Add due dates
* [ ] Add task priorities
* [ ] Add task categories
* [ ] Add task search
* [ ] Add task filtering
* [ ] Add input validation
* [ ] Add a graphical user interface
* [ ] Use SQLite for database storage
* [ ] Add user accounts
* [ ] Add authentication
* [ ] Create a web version of the application

---

## 🎯 Project Goal

The goal of this project is to build a simple but practical task management application while improving my Python programming and problem-solving skills.

It also serves as one of my beginner projects as I continue developing my skills as a **Python Developer and Cybersecurity Analyst**.

---

## 📖 Reference

This project was inspired by the **Task Tracker** challenge on roadmap.sh.

🔗 https://roadmap.sh/projects/task-tracker

---

## 👨‍💻 Author

**Abiodun Okubanjo**

**Python Developer | Cybersecurity Analyst**

I build practical Python and cybersecurity projects while developing my skills in programming, automation, networking, and cybersecurity.

---

⭐ **If you find this project useful, consider giving the repository a star!**
