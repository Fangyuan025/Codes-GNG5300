import csv
import re
import datetime
import os

# Constants for file paths
CONTACTS_FILE = 'contacts.csv'
LOG_FILE = 'log.txt'

# Contact Manager Class
class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.contacts = list(reader)

    def save_contacts(self):
        with open(CONTACTS_FILE, mode='w', newline='') as file:
            fieldnames = ['First Name', 'Last Name', 'Phone Number', 'Email Address', 'Address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

    def log_action(self, action):
        with open(LOG_FILE, mode='a') as file:
            file.write(f'{datetime.datetime.now()}: {action}\n')

    def add_contact(self, first_name, last_name, phone_number, email='', address=''):
        if not self.validate_phone(phone_number):
            print("Invalid phone number format. Expected (###) ###-####.")
            return
        if email and not self.validate_email(email):
            print("Invalid email address.")
            return
        self.contacts.append({
            'First Name': first_name,
            'Last Name': last_name,
            'Phone Number': phone_number,
            'Email Address': email,
            'Address': address
        })
        self.save_contacts()
        self.log_action(f'Added contact: {first_name} {last_name}')
        print("Contact added successfully.")

    def validate_phone(self, phone):
        return re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone)

    def validate_email(self, email):
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query.lower() in (contact['First Name'].lower() + contact['Last Name'].lower() + contact['Phone Number'])]
        for result in results:
            print(result)

    def delete_contact(self, phone_number):
        self.contacts = [contact for contact in self.contacts if contact['Phone Number'] != phone_number]
        self.save_contacts()
        self.log_action(f'Deleted contact with phone number: {phone_number}')
        print("Contact deleted successfully.")

    def update_contact(self, phone_number, **kwargs):
        for contact in self.contacts:
            if contact['Phone Number'] == phone_number:
                contact.update((k, v) for k, v in kwargs.items() if v)
                self.save_contacts()
                self.log_action(f'Updated contact with phone number: {phone_number}')
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def import_contacts(self, file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_contact(
                    row['First Name'],
                    row['Last Name'],
                    row['Phone Number'],
                    row.get('Email Address', ''),
                    row.get('Address', '')
                )

    def sort_contacts(self, by='Last Name'):
        self.contacts.sort(key=lambda x: x[by])

# Command-line interface
def main():
    cm = ContactManager()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Import Contacts from CSV")
        print("7. Sort Contacts")
        print("8. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone_number = input("Phone Number (###) ###-####: ")
            email = input("Email Address: ")
            address = input("Address: ")
            cm.add_contact(first_name, last_name, phone_number, email, address)

        elif choice == '2':
            cm.view_contacts()

        elif choice == '3':
            query = input("Search query: ")
            cm.search_contacts(query)

        elif choice == '4':
            phone_number = input("Phone Number of contact to update: ")
            print("Enter new details (leave blank to keep current value):")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email Address: ")
            address = input("Address: ")
            cm.update_contact(phone_number, first_name=first_name, last_name=last_name, email=email, address=address)

        elif choice == '5':
            phone_number = input("Phone Number of contact to delete: ")
            cm.delete_contact(phone_number)

        elif choice == '6':
            file_path = input("CSV file path: ")
            cm.import_contacts(file_path)

        elif choice == '7':
            sort_by = input("Sort by (First Name/Last Name/Phone Number): ")
            cm.sort_contacts(by=sort_by)
            print(f"Contacts sorted by {sort_by}.")

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()