import tkinter as tk
from tkinter import messagebox
import random
import string
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Define the function to generate a password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected for password generation.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password.decode()

# Define the function to handle the button click
def on_generate():
    try:
        length = int(length_entry.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        encrypted_password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
        result_entry.delete(0, tk.END)
        result_entry.insert(0, decrypted_password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Add a copy to clipboard function
def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Initialize the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")
app.configure(bg="#f0f0f0")

title_label = tk.Label(app, text="Password Generator", font=("Helvetica", 16), bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(app, text="Length:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky='e')
length_entry = tk.Entry(app)
length_entry.grid(row=1, column=1, padx=10, pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Include Uppercase", variable=upper_var, bg="#f0f0f0").grid(row=2, column=0, columnspan=2, pady=5, sticky='w')
tk.Checkbutton(app, text="Include Lowercase", variable=lower_var, bg="#f0f0f0").grid(row=3, column=0, columnspan=2, pady=5, sticky='w')
tk.Checkbutton(app, text="Include Digits", variable=digits_var, bg="#f0f0f0").grid(row=4, column=0, columnspan=2, pady=5, sticky='w')
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var, bg="#f0f0f0").grid(row=5, column=0, columnspan=2, pady=5, sticky='w')

generate_button = tk.Button(app, text="Generate", command=on_generate, bg="#4CAF50", fg="white", font=("Helvetica", 12))
generate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

result_entry = tk.Entry(app, width=40)
result_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(app, text="Copy", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Helvetica", 12))
copy_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Run the application
app.mainloop()

