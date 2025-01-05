# -*- coding: utf-8 -*-
"""contactmanager.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18GOPy6whqEo2v3P9ASZ2dDdUNf2eQv0V

contact manager
"""

# A simple contact manager program using a dictionary

# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact(name, phone):
    """Add a new contact."""
    if name in contacts:
        print(f"{name} already exists in contacts.")
    else:
        contacts[name] = phone
        print(f"Contact {name} added successfully.")

def update_contact(name, phone):
    """Update an existing contact."""
    if name in contacts:
        contacts[name] = phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    """Delete a contact."""
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"{name} not found in contacts.")

def display_contacts():
    """Display all contacts."""
    if contacts:
        print("\nContacts List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("\nNo contacts found.")

def main():
    """Main function to interact with the contact manager."""
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to update: ")
            phone = input("Enter new contact phone: ")
            update_contact(name, phone)
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()