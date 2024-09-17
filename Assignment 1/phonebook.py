import csv
import re
import datetime
import os

CONTACTS_FILE = 'contacts.csv'
LOG_FILE = 'log.txt'

class ContactManager:
    """A class to manage contact information with CRUD operations, search, and logging."""

    def __init__(self):
        """Initialize the contact manager by loading existing contacts."""
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from a CSV file."""
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.contacts = list(reader)

    def save_contacts(self):
        """Save the current list of contacts to a CSV file."""
        with open(CONTACTS_FILE, mode='w', newline='') as file:
            fieldnames = ['First Name', 'Last Name', 'Phone Number', 'Email Address', 'Address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

    def log_action(self, action):
        """Log an action to the log file with a timestamp."""
        with open(LOG_FILE, mode='a') as file:
            file.write(f'{datetime.datetime.now()}: {action}\n')

    def add_contact(self, first_name, last_name, phone_number, email='', address=''):
        """Add a new contact to the list and save it.

        Args:
            first_name (str): First name of the contact.
            last_name (str): Last name of the contact.
            phone_number (str): Phone number of the contact.
            email (str, optional): Email address of the contact.
            address (str, optional): Address of the contact.
        """
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
        """Validate the phone number format.

        Args:
            phone (str): Phone number to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone)

    def validate_email(self, email):
        """Validate the email address format.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

    def view_contacts(self):
        """Display all contacts."""
        for contact in self.contacts:
            print(contact)

    def search_contacts(self, query):
        """Search for contacts matching a query.

        Args:
            query (str): Query string to search for.
        """
        results = [contact for contact in self.contacts if query.lower() in (
            contact['First Name'].lower() + contact['Last Name'].lower() + contact['Phone Number'])]
        for result in results:
            print(result)

    def delete_contact(self, phone_number):
        """Delete a contact by phone number.

        Args:
            phone_number (str): Phone number of the contact to delete.
        """
        self.contacts = [contact for contact in self.contacts if contact['Phone Number'] != phone_number]
        self.save_contacts()
        self.log_action(f'Deleted contact with phone number: {phone_number}')
        print("Contact deleted successfully.")

    def update_contact(self, phone_number, **kwargs):
        """Update a contact's information.

        Args:
            phone_number (str): Phone number of the contact to update.
            **kwargs: New values for contact fields.
        """
        for contact in self.contacts:
            if contact['Phone Number'] == phone_number:
                contact.update((k, v) for k, v in kwargs.items() if v)
                self.save_contacts()
                self.log_action(f'Updated contact with phone number: {phone_number}')
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def import_contacts(self, file_path):
        """Import contacts from a CSV file.

        Args:
            file_path (str): Path to the CSV file.
        """
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
        """Sort contacts by a specified field.

        Args:
            by (str, optional): Field to sort by. Defaults to 'Last Name'.
        """
        self.contacts.sort(key=lambda x: x[by])

def main():
    """Main function to run the contact manager CLI."""
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
            while not cm.validate_phone(phone_number):
                print("Invalid phone number format. Expected (###) ###-####.")
                phone_number = input("Phone Number (###) ###-####: ")

            email = input("Email Address: ")
            while email and not cm.validate_email(email):
                print("Invalid email address.")
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

            new_phone_number = input("New Phone Number (###) ###-####: ")
            while new_phone_number and not cm.validate_phone(new_phone_number):
                print("Invalid phone number format. Expected (###) ###-####.")
                new_phone_number = input("New Phone Number (###) ###-####: ")

            new_email = input("New Email Address: ")
            while new_email and not cm.validate_email(new_email):
                print("Invalid email address.")
                new_email = input("New Email Address: ")

            address = input("Address: ")
            cm.update_contact(phone_number, first_name=first_name, last_name=last_name, phone_number=new_phone_number, email=new_email, address=address)

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