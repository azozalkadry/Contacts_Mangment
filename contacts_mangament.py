import json
import shortuuid
from contacts import Contacts


class ContactsMangement:
    def __init__(self):
        self.contacts_list = []
        self.id_counter = 0

    def add_contact(self):
        name = input("Enter Your Name: ")
        number = input("Enter Your Number: ")
        email = input("Enter Your Email: ")
        self.id_counter += 1
        unique_id = self.id_counter

        contact = Contacts(unique_id, name, number, email)
        self.contacts_list.append(contact)

        file_path = "contacts.json"
        contacts_data = []
        for contact in self.contacts_list:
            contacts_data.append(contact)

        print("Add Data Sucssfull.")

    def update_contacts(self):
        contact_id = int(
            input("Enter The Id For Contact to Update Contact : "))
        found = False

        for contact in self.contacts_list:
            if contact.id == contact_id:
                found = True
                name = input("Enter Your Name: ")
                number = input("Enter Your Number: ")
                email = input("Enter Your Email: ")

                contact.name = name
                contact.number = number
                contact.email = email
                print("Contact updated successfully.")

        if not found:
            print("Contact Not Found.")
    # def save_contacts(self,filepath):
    #     self.data_contact =[]
    #     for contact in self.contacts_list:
    #         self.data_contact.append(contact.to_dict())

    #         with open(filepath , "w") as file:
    #             json.dump(self.data_contact ,file)

    def display_contacts(self):
        for contact in self.contacts_list:
            print(f"ID: {contact.id}")
            print(f"Name: {contact.name}")
            print(f"Number: {contact.number}")
            print(f"Email: {contact.email}")
            print()

    def delete_contacts(self):
        contact_id = int(input("Enter The Id For Contact to Delete Contact: "))
        found = False

        for contact in self.contacts_list:
            if contact.id == contact_id:
                found = True
                self.contacts_list.remove(contact)
                print("Contact Deleted successfully.")

        if not found:
            print("Contact Not Found.")

    def search_contacts(self):
        search_term = input("Enter the search term: ").lower()
        found = False

        for contact in self.contacts_list:
            if (
                search_term in contact.name.lower()
                or search_term in contact.number.lower()
                or search_term in contact.email.lower()
            ):
                found = True
                print(f"ID: {contact.id}")
                print(f"Name: {contact.name}")
                print(f"Number: {contact.number}")
                print(f"Email: {contact.email}")
                print()

        if not found:
            print("No contacts found.")
