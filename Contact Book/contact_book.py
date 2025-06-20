

import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    if not name:
        return
    if name in contacts:
        messagebox.showinfo("Duplicate", "Contact already exists.")
        return
    number = simpledialog.askstring("Add Contact", "Enter phone number:")
    email = simpledialog.askstring("Add Contact", "Enter email:")
    address = simpledialog.askstring("Add Contact", "Enter address:")

    contacts[name] = {
        "number": number or "",
        "email": email or "",
        "address": address or ""
    }
    messagebox.showinfo("Success", f"Contact '{name}' added.")

def view_contacts():
    if not contacts:
        messagebox.showinfo("Contacts", "No contacts available.")
        return
    result = ""
    for name, details in contacts.items():
        result += f"\nName: {name}\nPhone: {details['number']}\nEmail: {details['email']}\nAddress: {details['address']}\n"
    messagebox.showinfo("All Contacts", result.strip())

def search_contact():
    name = simpledialog.askstring("Search Contact", "Enter name to search:")
    if not name:
        return
    if name in contacts:
        details = contacts[name]
        messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['number']}\nEmail: {details['email']}\nAddress: {details['address']}")
    else:
        messagebox.showinfo("Not Found", "Contact not found.")

def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter name to update:")
    if not name or name not in contacts:
        messagebox.showinfo("Not Found", "Contact not found.")
        return

    current = contacts[name]
    number = simpledialog.askstring("Update Contact", f"Phone (current: {current['number']}):") or current['number']
    email = simpledialog.askstring("Update Contact", f"Email (current: {current['email']}):") or current['email']
    address = simpledialog.askstring("Update Contact", f"Address (current: {current['address']}):") or current['address']

    contacts[name] = {
        "number": number,
        "email": email,
        "address": address
    }
    messagebox.showinfo("Updated", f"Contact '{name}' updated.")

def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter name to delete:")
    if not name or name not in contacts:
        messagebox.showinfo("Not Found", "Contact not found.")
        return
    del contacts[name]
    messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("300x350")

tk.Label(root, text="Contact Book", font=("Arial", 18, "bold")).pack(pady=10)

tk.Button(root, text="Add Contact", width=25, command=add_contact).pack(pady=5)
tk.Button(root, text="View All Contacts", width=25, command=view_contacts).pack(pady=5)
tk.Button(root, text="Search Contact", width=25, command=search_contact).pack(pady=5)
tk.Button(root, text="Update Contact", width=25, command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=25, command=delete_contact).pack(pady=5)
tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

root.mainloop()
