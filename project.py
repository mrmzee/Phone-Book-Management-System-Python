import json

def load_contacts(file_name="contacts.json"):
    """Loads contacts from a JSON file."""
    try:
        with open(file_name, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts, file_name="contacts.json"):
    """Saves contacts to a JSON file."""
    with open(file_name, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, last_name, age, country, file_name="contacts.json"):
    """Adds a new contact to the contacts list."""
    contacts = load_contacts(file_name)
    contacts.append({
        "name": name,
        "phone": phone,
        "last_name": last_name,
        "age": age,
        "country": country
    })
    save_contacts(contacts, file_name)

def find_contact(phone, file_name="contacts.json"):
    """Finds a contact by phone number."""
    contacts = load_contacts(file_name)
    for contact in contacts:
        if contact["phone"] == phone:
            return contact
    return None

def main():
    """Main function to demonstrate adding a contact and finding a contact."""
    while True:
        print("1. Add contact")
        print("2. Find contact by phone number")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter contact name: ")
            last_name = input("Enter contact last name: ")
            phone = input("Enter contact phone number: ")
            age = input("Enter contact age: ")
            country = input("Enter contact country: ")
            add_contact(name, phone, last_name, age, country)
            print("Contact added successfully!")
        elif choice == "2":
            phone = input("Enter contact phone number: ")
            contact = find_contact(phone)
            if contact:
                print(f"Contact found:\n"
                      f"Name: {contact['name']}\n"
                      f"Last Name: {contact['last_name']}\n"
                      f"Phone: {contact['phone']}\n"
                      f"Age: {contact['age']}\n"
                      f"Country: {contact['country']}\n")
            else:
                print("Contact not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
