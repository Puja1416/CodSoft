import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Length must be at least 4.")
            return

       
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        
        if length > 4:
            all_chars = string.ascii_letters + string.digits + string.punctuation
            password += [random.choice(all_chars) for _ in range(length - 4)]

      
        random.shuffle(password)

        result_label.config(text="Generated Password:\n" + ''.join(password))
    except ValueError:
        result_label.config(text="Please enter a valid number.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")


length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


result_label = tk.Label(root, text="", wraplength=350, justify="center")
result_label.pack(pady=10)


root.mainloop()
