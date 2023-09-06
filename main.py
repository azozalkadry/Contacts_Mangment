from contacts_mangament import ContactsMangement


def main():
    contactmangament = ContactsMangement()
    input_message = """
        What Do You Want To Do ?
        -------------------------
        1. Add Contacts: 
        2. Update Contacts: 
        3. Delete Contacts: 
        4. Show Contacts: 
        5. Search by ID:
        6. Exit
    """
    while True:
        print(input_message)
        choice = input("Enter your choice: ")

        if choice == "1":
            contactmangament.add_contact()
        elif choice == "2":
            contactmangament.update_contacts()
        elif choice == "3":
            contactmangament.delete_contacts()
        elif choice == "4":
            contactmangament.display_contacts()
        elif choice == "5":
            contactmangament.search_contacts()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
