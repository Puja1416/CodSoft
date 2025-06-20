import tkinter as tk
from tkinter import messagebox, simpledialog
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")

tasks = []

def update_task_listbox():
    listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        status = "✔️" if task['done'] else "❌"
        listbox.insert(tk.END, f"{status} {task['title']}")

def add_task():
    title = entry.get()
    if title:
        tasks.append({"title": title, "done": False})
        entry.delete(0, tk.END)
        update_task_listbox()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_task_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

def update_task():
    selected = listbox.curselection()
    if selected:
        new_title = simpledialog.askstring("Update Task", "Enter new task:")
        if new_title:
            tasks[selected[0]]['title'] = new_title
            update_task_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a task to update.")

def toggle_status():
    selected = listbox.curselection()
    if selected:
        tasks[selected[0]]['done'] = not tasks[selected[0]]['done']
        update_task_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a task to toggle status.")

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=10)

update_btn = tk.Button(root, text="Update Task", command=update_task)
update_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

toggle_btn = tk.Button(root, text="Mark/Unmark Completed", command=toggle_status)
toggle_btn.pack(pady=5)

root.mainloop()
