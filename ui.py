import tkinter as tk
from tkinter import messagebox
from functools import partial
import commands

def handle_update(id, title, app):
    if not title:
        messagebox.showerror(title="Update task!", message="Cannot update with empty task", parent=app)
    else:
        commands.update_tasks(id, {"title": title})
        show_all_tasks_frame(app)


def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)

def submit_task(title, app):
    if not title:
        messagebox.showerror(
            title="Add task",
            message="Cannot add empty task!",
            parent=app
        )

    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app)

def show_edit_task_frame(task, app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text=f"edit task: {task["title"]}")
    label.grid(column=0, row=0)
    # Add an entry widget and show the task title
    entry = tk.Entry(master=frame)
    entry.insert(0, task["title"])
    entry.grid(column=0, row=1, columnspan=2, sticky="ew", pady=(10,10))
    # Add a button with text update for saving the changes
    update_btn = tk.Button(master=frame, text="update", command=lambda: handle_update(task["_id"], entry.get(), app))
    update_btn.grid(column=1, row=2)
    # Add a button with the text Back/cancel to remove the frame 
    cancel_btn = tk.Button(master=frame, text="Back", command=lambda: frame.destroy())
    cancel_btn.grid(column=0, row=2, padx=5, pady=5)

    frame.tkraise()


def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text="What do you want to do?\n")
    label.grid()
    entry = tk.Entry(master=frame)
    entry.grid()
    btn = tk.Button(master=frame, text="Submit", command=lambda: submit_task(entry.get(), app))
    btn.grid()

    frame.tkraise()

def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0)

        edit_btn = tk.Button(master=frame, text="edit", command=partial(show_edit_task_frame, task, app))
        edit_btn.grid(row=tasks.index(task), column=1)

        delete_btn = tk.Button(master=frame, text="Delete", command=partial(handle_delete, task["_id"], app))
        delete_btn.grid(row=tasks.index(task), column=2)

    add_btn = tk.Button(master=frame, text="Add task", command=lambda: show_add_task_frame(app))
    add_btn.grid(row=len(tasks) + 1, column=0, padx=10, pady=10)


    frame.tkraise()





    # root = tk.Tk()
    # default_text = tk.StringVar(root, "Edit task here")
    # entry = tk.Entry(root, textvariable=default_text)
    # entry.pack()