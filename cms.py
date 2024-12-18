import json

def add_contact():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    contact = {"name": name, "age": age, "email": email}
    return contact

def display_contacts(contacts):
     for i, contact in enumerate(contacts):
        print(i + 1, "-", contact["name"], "|", contact["age"], "|", contact["email"])

def delete_contact(contacts):
    display_contacts(contacts)
    
    while True:
        print()
        number = input("Enter a number to delete (or '0' to go back): ")
        
        if number == '0':
            print("Main menu.")
            break
        
        try: 
            number = int(number)
            if number <=0 or number > len(contacts):
                print("Invalid number, out of range.")
            else:
                contacts.pop(number - 1)
                print("Contact deleted.")
                break
        except:
            print("Invalid number.")
        
def search(contacts):
    search_name = input("Search for a name: ").lower()
    print()
    results = []
    
    for contact in contacts:
        name = contact["name"]
        if search_name in name.lower():
            results.append(contact)
            
    display_contacts(results)
    
print()
print("Hi, welcome to the Contact Managemement System")

with open("contacts.json", "r") as f:
    contacts = json.load(f)["contacts"]

while True:
    print("Contact list size:", len(contacts))
    print()

    command = input("You can 'Add', 'Delete' or 'Search' for Contacts. Use 'Q' to Quit: ").lower()
    
    if command == "add":
        contact = add_contact()
        contacts.append(contact)
        print()
        print("Contact added!")
        print()
        display_contacts(contacts)
    elif command == "delete":
        delete_contact(contacts)
    elif command == "search":
        search(contacts)
    elif command == "q":
        break
    else:
        print("Invalid entry.")

with open("contacts.json", "w") as f:
    json.dump({"contacts": contacts}, f)
