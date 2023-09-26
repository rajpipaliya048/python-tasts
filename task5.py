telephone_directory = {}

# add contct function
def add_contact():
    name = input("Enter name: ")
    if name in telephone_directory:
        print("Contact already exist")
    else:
        number = input("Enter number: ")
        telephone_directory[name] = number
        print("Contact added successfully.")
        
# function to delete contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in telephone_directory:
        del telephone_directory[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
        
# function to search contact
def search():
    name = input("Enter the name to search: ")
    if name in telephone_directory:
        print(f"Name: {name}, Number: {telephone_directory[name]}")
    else:
        print("Contact not found.")
        
# function to update existing contact
def update_contact():
    name = input("Enter the name to update: ")
    if name in telephone_directory:
        new_number = input("Enter the new number: ")
        telephone_directory[name] = new_number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")
        
# function to display all contact details
def display_all():
    print("All Contacts:")
    for name, number in telephone_directory.items():
        print(f"Name: {name}, Number: {number}")

while True:
    print("\nTelephone Directory Operations:")
    print("1. Add contact")
    print("2. Delete a contact")
    print("3. Search")
    print("4. Update existing contact number")
    print("5. Display All")
    print("6. Exit")
    
    choice = input("Please enter operation number: ")
    print("\n")

    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == "3":
        search()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        display_all()
    elif choice == "6":
        break
    else:
        print("please enter right operation number")
