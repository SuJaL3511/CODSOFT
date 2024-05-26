contacts = {}

def display_contact():
    print("Email\t\tName\tContact Number\t\tAddress")
    for email, info in contacts.items():
        print("{}\t{}\t{}\t\t{}".format(email, info["name"], info["phone"], info["address"]))

while True:
    choice = int(input(" 1. Add Contact \n 2. Display Contact list \n 3. Search Contact \n 4. Update Contact \n 5. Delete Contact \n 6. Exit \n Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the contact name: ")
        email = input("Enter the email address: ")
        if email in contacts:
            print("Email already exists. Try updating the contact instead.")
        else:
            phone = input("Enter the mobile number: ")
            address = input("Enter the address: ")
            contacts[email] = {"name": name, "phone": phone, "address": address}
        
    elif choice == 2:
        if not contacts:
            print("Empty contact book")
        else:
            display_contact()
            
    elif choice == 3:
        search_name = input("Enter the contact name: ")
        found = False
        for email, info in contacts.items():
            if info["name"].lower() == search_name.lower():
                print("{}'s contact number is {}, email is {}, and address is {}".format(info["name"], info["phone"], email, info["address"]))
                found = True
                break
        if not found:
            print("Name is not found in contact book")
            
    elif choice == 4:
        update_name = input("Enter the contact name to be updated: ")
        found = False
        for email, info in contacts.items():
            if info["name"].lower() == update_name.lower():
                update_choice = input("Do you want to update the name, number, address, or all? (name/number/address/all): ").lower()
                if update_choice == "name":
                    new_name = input("Enter the new contact name: ")
                    contacts[email]["name"] = new_name
                elif update_choice == "number":
                    new_number = input("Enter the new mobile number: ")
                    contacts[email]["phone"] = new_number
                elif update_choice == "address":
                    new_address = input("Enter the new address: ")
                    contacts[email]["address"] = new_address
                elif update_choice == "all":
                    new_name = input("Enter the new contact name: ")
                    new_number = input("Enter the new mobile number: ")
                    new_address = input("Enter the new address: ")
                    contacts[email]["name"] = new_name
                    contacts[email]["phone"] = new_number
                    contacts[email]["address"] = new_address
                print("Contact Updated")
                found = True
                break
        if not found:
            print("Name is not found in contact book")
            
    elif choice == 5:
        del_name = input("Enter the contact name to be deleted: ")
        found = False
        for email, info in list(contacts.items()):
            if info["name"].lower() == del_name.lower():
                confirm = input(f"Do you want to delete the contact {info['name']} with email {email}? (y/n): ").lower()
                if confirm == 'y':
                    contacts.pop(email)
                    print("Contact Deleted")
                else:
                    print("Delete operation cancelled")
                found = True
                break
        if not found:
            print("Name is not found in contact book")
            
    elif choice == 6:
        break
    
    else:
        print("Invalid choice, please try again.")
