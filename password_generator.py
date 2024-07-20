import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    characters = ''
    
    if complexity == 1:  # Simple: only letters and digits
        characters = string.ascii_letters + string.digits
    elif complexity == 2:  # Medium: letters, digits, and some punctuation
        characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    elif complexity == 3:  # Complex: letters, digits, and all punctuation
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    def generate():
        try:
            password_length = int(length_entry.get())
            if password_length <= 0:
                messagebox.showerror("Error", "Password length must be greater than zero.")
                return
            
            complexity = complexity_var.get()
            password = generate_password(password_length, complexity)
            password_var.set(password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")
    
    # Create main window
    root = tk.Tk()
    root.title("Password Generator")
    root.configure(background="grey")
    
    # Length label and entry
    length_label = tk.Label(root, text="Password Length:",fg="red")
    length_label.pack(pady=10)
    length_entry = tk.Entry(root)
    length_entry.pack()
    
    # Complexity label and radio buttons
    complexity_label = tk.Label(root, text="Complexity:",fg="red")
    complexity_label.pack(pady=10)
    
    complexity_var = tk.IntVar()
    complexity_var.set(1)  
    
    simple_radio = tk.Radiobutton(root, text="Simple",bg="green",variable=complexity_var,value=1)
    simple_radio.pack(anchor=tk.W)
    medium_radio = tk.Radiobutton(root, text="Medium",bg="green",variable=complexity_var, value=2)
    medium_radio.pack(anchor=tk.W)
    complex_radio = tk.Radiobutton(root, text="Complex",bg="green",variable=complexity_var, value=3)
    complex_radio.pack(anchor=tk.W)
    
    # Generate button
    generate_button = tk.Button(root, text="Generate Password", command=generate,fg="orange")
    generate_button.pack(pady=20)
    
    password_var = tk.StringVar()
    password_label = tk.Label(root, text="Generated Password:",fg="orange")
    password_label.pack()
    password_entry = tk.Entry(root, textvariable=password_var, state='readonly',fg="blue")
    password_entry.pack()
    
    root.mainloop()

if __name__ == "__main__":
    generate_password_gui()




