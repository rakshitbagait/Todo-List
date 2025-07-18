
---

## 📝 To-Do List App (Desktop GUI)

A sleek and efficient desktop **To-Do List application** built using **Python and Tkinter**, designed to help users manage daily tasks with ease and clarity. This application provides a clean, interactive GUI that enables users to add, view, update, and delete tasks, along with helpful features like **status tracking**, **automatic task ID generation**, and **overdue task highlighting**.

---

### 🔧 Key Features:

* **Simple and intuitive interface** powered by Tkinter
* **Auto-generated Task IDs** for easy reference
* **Dynamic Treeview** display for all tasks
* **Status dropdown** for each task (e.g., Pending, Completed)
* **Real-time overdue detection**: tasks past due are highlighted
* **Task deletion** upon completion
* Lightweight and fully offline; runs on any Windows/Linux system

---

### 🎯 Purpose:

This project was created to explore GUI development in Python while solving a real-world problem — task and time management. It's ideal for students, developers, or professionals who prefer a minimalist daily planner without relying on web or cloud platforms.

---

### 🚀 Tech Stack:

* **Python 3.x**
* **Tkinter** (GUI)
* **ttk Treeview** for dynamic task display
* Basic file handling / (or optional SQLite in advanced version)

---

Let me know if you want to:

* Add **screenshots or a GIF**
* Include **future features** (e.g., reminders, notifications)
* Convert it to a web version or host the code on GitHub

Here’s a well-written and professional description of how your To-Do List app **manages Task IDs and stores data using JSON** — ideal for GitHub README, documentation, or a portfolio:

---

### 🗂️ Task Management with Unique IDs and JSON-based Storage

The core of the To-Do List app revolves around efficient task tracking and persistence. To achieve this, the application uses a combination of **auto-incrementing Task IDs** and **JSON file storage** to simulate a lightweight, local database system.

---

#### 🔢 Auto-Incrementing Task IDs

Each task in the app is uniquely identified using an **automatically generated Task ID**, which ensures that no two tasks have the same identifier. This feature is essential for:

* Referencing specific tasks for updates or deletions
* Maintaining a clean, structured, and searchable task list
* Supporting future features like task prioritization or sorting

**How it works:**

* On app launch, the app loads the JSON data file.
* It determines the highest existing Task ID.
* New tasks are assigned a Task ID that is **one greater** than the current highest ID.
* This avoids ID duplication and ensures continuity, even across sessions.

---

#### 💾 JSON-Based Storage (Simulated Database)

The app uses a `.json` file to **store and retrieve tasks persistently**, mimicking the behavior of a lightweight database:

* Tasks are saved in a structured format:

  ```json
  {
    "tasks": [
      {
        "id": 1,
        "title": "Buy groceries",
        "status": "Pending",
        "due_date": "2025-07-19"
      },
      ...
    ]
  }
  ```
* On every add/update/delete operation, the JSON file is updated in real-time.
* On app launch, the entire JSON file is read to repopulate the task list.

**Advantages:**

* Fully offline: no internet or external database needed
* Lightweight and fast for personal use
* Easy to debug and migrate to databases like SQLite or PostgreSQL in future

---

This setup allows the app to maintain **state between sessions**, support **searchability and extensibility**, and provide a database-like experience with minimal overhead.

---



## Screenshots

![App Screenshot](C:\Users\Rakshit\OneDrive\画像\Screenshots\Screenshot (43).png)

