'''import tkinter as tk
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
    generate_password_gui()'''

'''import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = {}

        # Create GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.grid(row=3, column=1)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=4, column=0)
        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.grid(row=4, column=1)

        self.search_by_label = tk.Label(root, text="Search by:")
        self.search_by_label.grid(row=5, column=0)
        self.search_by_var = tk.StringVar()
        self.search_by_name_radio = tk.Radiobutton(root, text="Name", variable=self.search_by_var, value="name")
        self.search_by_name_radio.grid(row=5, column=1)
        self.search_by_phone_radio = tk.Radiobutton(root, text="Phone", variable=self.search_by_var, value="phone")
        self.search_by_phone_radio.grid(row=5, column=2)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=6, column=0)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=6, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=6, column=2)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=7, column=1)

        self.contact_listbox = tk.Listbox(root, width=40)
        self.contact_listbox.grid(row=8, column=0, columnspan=3)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.contact_listbox.insert(tk.END, f"{name} - {phone}")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        search_term = self.search_entry.get()
        search_by = self.search_by_var.get()
        if search_by == "name":
            for name, details in self.contacts.items():
                if search_term.lower() in name.lower():
                    self.contact_listbox.delete(0, tk.END)
                    self.contact_listbox.insert(tk.END, f"{name} - {details['phone']}")
                    return
        elif search_by == "phone":
            for name, details in self.contacts.items():
                if search_term in details["phone"]:
                    self.contact_listbox.delete(0, tk.END)
                    self.contact_listbox.insert(tk.END, f"{name} - {details['phone']}")
                    return
        messagebox.showinfo("Not Found", "Contact not found")

    def update_contact(self):
        selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
        if selected_contact:
            name, phone = selected_contact.split(" - ")
            self.name_entry.delete(0, tk.END)'''
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = []

        self.name_label = tk.Label(root, text="Name:",bg="pink")
        self.name_label.pack()
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:",bg="pink")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=50)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:",bg="orange")
        self.email_label.pack()
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:",bg="orange")
        self.address_label.pack()
        self.address_entry = tk.Entry(root, width=50)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact",bg="green", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contacts",bg="green", command=self.view_contacts)
        self.view_button.pack()

        self.search_label = tk.Label(root, text="Search:",fg="red")
        self.search_label.pack()
        self.search_entry = tk.Entry(root, width=50)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search",fg="red", command=self.search_contact)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact",bg="yellow",fg="red", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact",bg="yellow",fg="red", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_entries()

    def view_contacts(self):
        contact_list = ""
        for contact in self.contacts:
            contact_list += f"Name: {contact.name}, Phone: {contact.phone}\n"
        messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        query = self.search_entry.get()
        found = False
        for contact in self.contacts:
            if query in contact.name or query in contact.phone:
                messagebox.showinfo("Contact Found", f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                found = True
                break
        if not found:
            messagebox.showinfo("Not Found", "Contact not found!")

    def update_contact(self):
        name = self.name_entry.get()
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = self.phone_entry.get()
                contact.email = self.email_entry.get()
                contact.address = self.address_entry.get()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                return
        messagebox.showinfo("Not Found", "Contact not found!")

    def delete_contact(self):
        name = self.name_entry.get()
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                return
        messagebox.showinfo("Not Found", "Contact not found!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Management System")
contact_manager = ContactManager(root)
root.mainloop()