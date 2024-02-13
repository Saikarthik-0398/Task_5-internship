contacts = []

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone_number": phone_number, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone Number: {contact['phone_number']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
            found_contacts.append(contact)
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
            found_contacts.append(contact)
    if found_contacts:
        if len(found_contacts) == 1:
            contact = found_contacts[0]
            print("Contact found:")
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
            choice = input("Do you want to update this contact? (yes/no): ")
            if choice.lower() == 'yes':
                contact['name'] = input("Enter new name: ")
                contact['phone_number'] = input("Enter new phone number: ")
                contact['email'] = input("Enter new email: ")
                contact['address'] = input("Enter new address: ")
                print("Contact updated successfully.")
        else:
            print("Multiple contacts found. Please refine your search.")
    else:
        print("No matching contacts found.")

def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
            found_contacts.append(contact)
    if found_contacts:
        if len(found_contacts) == 1:
            contact = found_contacts[0]
            print("Contact found:")
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
            choice = input("Do you want to delete this contact? (yes/no): ")
            if choice.lower() == 'yes':
                contacts.remove(contact)
                print("Contact deleted successfully.")
        else:
            print("Multiple contacts found. Please refine your search.")
    else:
        print("No matching contacts found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
