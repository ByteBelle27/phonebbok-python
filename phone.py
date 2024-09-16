
phonebook = {}

# Step 3: User Interface
def display_menu():
    print("\nPhonebook Menu:")
    print("1. Add a New Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. List All Contacts")
    print("5. Exit")

def add_contact():
    name = input("Enter the contact name: ").strip()
    if name in phonebook:
        print(f"Contact '{name}' already exists.")
    else:
        phone = input("Enter the contact phone number: ").strip()
        phonebook[name] = phone
        print(f"Contact '{name}' added successfully.")

def search_contact():
    name = input("Enter the contact name to search: ").strip()
    if name in phonebook:
        print(f"Phone number of {name}: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter the contact name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def list_contacts():
    if phonebook:
        print("\nContacts in Phonebook:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phonebook is empty.")

# Step 3: Main loop for user interaction
while True:
    display_menu()
    choice = input("\nChoose an option (1-5): ").strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        print("Exiting Phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
