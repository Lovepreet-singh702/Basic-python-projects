import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print("Contact Added Successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No Contacts Found!")
    else:
        for name, phone in contacts.items():
            print(f"\nName: {name}\nPhone: {phone}")

def search_contact():
    name = input("Enter Name to Search: ")
    contacts = load_contacts()
    if name in contacts:
        print(f"\nName: {name}\nPhone: {contacts[name]}")
    else:
        print("Contact Not Found!")

def update_contact():
    contacts = load_contacts()
    name = input("Enter Name to Update: ")
    if name in contacts:
        phone = input("Enter New Phone Number: ")
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found!")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter Name to Delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")

def main():
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid Choice! Try Again.")

main()
