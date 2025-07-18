from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import datetime
from tkinter import ttk

class ToDo(Tk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.config(bg="white", pady=20, padx=20)

        # Load logo
        self.logo_image = Image.open("check-list.png")
        self.resized_logo = self.logo_image.resize((32, 32))
        self.logo_photo = ImageTk.PhotoImage(self.resized_logo)
        self.iconphoto(False, self.logo_photo)

        self.resized_img = self.logo_image.resize((100, 100))
        self.image = ImageTk.PhotoImage(self.resized_img)
        self.canvas = Canvas(self, height=100, width=100, highlightthickness=0, background="white")
        self.canvas.place(x=400, y=0)
        self.canvas.create_image(50, 50, image=self.image)

        self.my_todo_label = Label(text="To Do List", font=("Times New Roman", 50, "bold"), fg="#af72c2", background="white")
        self.my_todo_label.place(x=520, y=30)

        # Task input
        self.add_task = Entry(self, bd=0, background="white", font=("Times New Roman", 20))
        self.add_task.place(x=1000, y=150, width=300, height=50)
        self.blue_frame(width=300, x=1000, y=200)

        self.add_task_placeholder = ' Add your task here...'
        self.add_task.insert(0, self.add_task_placeholder)
        self.add_task.config(fg="grey")
        self.add_task.bind("<FocusIn>", lambda e: self.on_entry_click(e, self.add_task_placeholder, self.add_task))
        self.add_task.bind("<FocusOut>", lambda e: self.on_entry_out(e, self.add_task_placeholder, self.add_task))

        # Date input
        self.add_date = Entry(self, bd=0, background="white", font=("Times New Roman", 20))
        self.add_date.place(x=1000, y=300, width=300, height=50)
        self.blue_frame(width=300, x=1000, y=350)

        self.add_date_placeholder = ' Add completion date (YYYY-MM-DD)...'
        self.add_date.insert(0, self.add_date_placeholder)
        self.add_date.config(fg="grey")
        self.add_date.bind("<FocusIn>", lambda e: self.on_entry_click(e, self.add_date_placeholder, self.add_date))
        self.add_date.bind("<FocusOut>", lambda e: self.on_entry_out(e, self.add_date_placeholder, self.add_date))

        self.add_button = Button(self, text="Add", bg="Blue", fg="White", bd=0, activebackground="cyan", font=("Arial", 10), command=self.add_task_func)
        self.add_button.place(x=1000, y=400, height=50, width=300)

        # Treeview for tasks
        self.task_view = ttk.Treeview(self, columns=("Task Id", "Task Name", "Date of completion", "Status"), show="headings")
        self.task_view.heading("Task Id", text="Task Id")
        self.task_view.heading("Task Name", text="Task Name")
        self.task_view.heading("Date of completion", text="Date of completion")
        self.task_view.heading("Status", text="Status")
        self.task_view.place(x=30, y=150, height=600)
        self.task_view.bind("<<TreeviewSelect>>", self.on_row_select)

        self.create_task_json()
        self.load_tasks_into_tree()

    def create_task_json(self):
        try:
            with open("task.json", "r") as file:
                json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("task.json", "w") as file:
                json.dump({"last task id": 0, "task": {}}, file, indent=4)

    def add_task_func(self):
        task = self.add_task.get()
        date = self.add_date.get()

        if task == self.add_task_placeholder or date == self.add_date_placeholder:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")  # validate date format
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format.")
            return

        with open("task.json", "r") as file:
            data = json.load(file)

        task_id = str(data["last task id"] + 1)

        new_task = {
            "task": task,
            "due_date": date,
            "status": "Incomplete"
        }

        data["task"][task_id] = new_task
        data["last task id"] += 1

        with open("task.json", "w") as file:
            json.dump(data, file, indent=4)

        self.add_task.delete(0, END)
        self.add_task.insert(0, self.add_task_placeholder)
        self.add_task.config(fg="grey")

        self.add_date.delete(0, END)
        self.add_date.insert(0, self.add_date_placeholder)
        self.add_date.config(fg="grey")

        self.load_tasks_into_tree()

    def load_tasks_into_tree(self):
        self.task_view.delete(*self.task_view.get_children())

        try:
            with open("task.json", "r") as file:
                data = json.load(file)
                tasks = data.get("task", {})
        except:
            tasks = {}

        today = datetime.datetime.now().date()

        for task_id, task_info in tasks.items():
            task = task_info.get("task", "")
            due_date_str = task_info.get("due_date", "")
            status = task_info.get("status", "")

            try:
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                if status == "Completed":
                    tag = "completed"
                elif due_date < today:
                    tag = "overdue"
                else:
                    tag = ""
            except:
                tag = ""

            self.task_view.insert("", "end", values=(task_id, task, due_date_str, status), tags=(tag,))

        self.task_view.tag_configure("overdue", background="lightcoral")
        self.task_view.tag_configure("completed", background="lightgreen")

    def on_row_select(self, event):
        selected = self.task_view.selection()
        if not selected:
            return

        item = selected[0]
        values = self.task_view.item(item, "values")
        task_id = values[0]
        status = values[3]
        due_date_str = values[2]

        try:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except:
            return

        today = datetime.datetime.now().date()

        if status == "Completed" or due_date < today:
            return

        x, y, width, height = self.task_view.bbox(item, column="#4")
        self.status_combobox = ttk.Combobox(self, values=["Incomplete", "Completed"], state="readonly")
        self.status_combobox.place(x=x + 30, y=y + 150, width=width)
        self.status_combobox.set(status)
        self.status_combobox.focus()
        self.status_combobox.bind("<<ComboboxSelected>>", lambda e: self.on_status_change(task_id, item))

    def on_status_change(self, task_id, tree_item_id):
        new_status = self.status_combobox.get()

        with open("task.json", "r") as file:
            data = json.load(file)

        tasks = data.get("task", {})

        if new_status == "Completed":
            if task_id in tasks:
                del tasks[task_id]
            data["task"] = tasks
            with open("task.json", "w") as file:
                json.dump(data, file, indent=4)
            self.task_view.delete(tree_item_id)
        else:
            if task_id in tasks:
                tasks[task_id]["status"] = new_status
            with open("task.json", "w") as file:
                json.dump(data, file, indent=4)
            self.task_view.set(tree_item_id, column="Status", value=new_status)

        self.status_combobox.destroy()

    def last_task_id(self):
        with open("task.json", "r") as file:
            data = json.load(file)
            return data.get("last task id", 0)

    def blue_frame(self, width, x, y):
        self.frame = Frame(self, bg="Blue")
        self.frame.place(x=x, y=y, width=width, height=0)

    def on_entry_click(self, event, placeholder, entry):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg="black")

    def on_entry_out(self, event, placeholder, entry):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")


# Run the app
app = ToDo()
app.mainloop()
