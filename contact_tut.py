#contact prototype

from inputs import *
import pickle


contacts = []

class Contact(object):

    min_session_length = 0.5
    max_session_length = 3.5

    def __init__(self, name, address, telephone = 'No telephone'):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.hours_worked = 0


    def get_hours_worked(self):
        return self.hours_worked

    @staticmethod
    def validate_session_length(session_length):
        if session_length < Contact.min_session_length:
            return False
        if session_length > Contact.max_session_length:
            return False
        return True

    def add_session(self, session_length):
        if not Contact.validate_session_length(session_length):
            return
        self.hours_worked = self.hours_worked + session_length
        return True



def new_contact():
    print('Create new contact')
    name = read_text('Enter contact name: ')
    address = read_text('Enter contact address: ')
    telephone = read_text('Enter contact phone: ')
    new_contact = Contact(name, address, telephone)
    contacts.append(new_contact)


def display_contact():
    print('Find contact')
    search_name = name = read_text('Enter contact name: ')
    search_name = search_name.strip()
    search_name = search_name.lower()
    result = None
    for contact in contacts:
        name = contact.name
        name = name.strip()
        name = name.lower()
        if name.startswith(search_name):
            result = contact
            break
    if result != None:
        print(f'Name: {contact.name}')
        print(f'Address: {contact.address}')
        print(f'Phone: {contact.telephone}')

    else:
        print('This name was not found')

def find_contact(search_name):
    search_name = search_name.strip()
    search_name = search_name.lower()
    for contact in contacts:
        name = contact.name
        name = name.strip()
        name = name.lower()
        if name.startswith(search_name):
            return contact
    return None


def edit_contact():
    print('Edit contact')
    search = read_text('Name: ')
    contact = find_contact(search)
    if contact != None:
        print('Enter (.) to leave unchaged')
        name = read_text('Name: ')
        address = read_text('Address: ')
        telephone = read_text('Phone: ')

        if name != '.':
            contact.name = name
        if address != '.':
            contact.address = address
        if telephone != '.':
            contact.telephone = telephone
    else:
        ('This name was not found')


def save_contact():
    print('Save contact')
    file_name = 'contacts.pickle'
    with open(file_name, 'wb') as output_file:
        pickle.dump(contacts, output_file)


def load_contact():
    #print('Load contact')
    file_name = 'contacts.pickle'
    global contacts
    with open(file_name, 'rb') as input_file:
        contacts = pickle.load(input_file)


def add_session_to_contact():
    print('Add session')
    search_name = read_text('Contact name: ')
    contact = find_contact(search_name)
    if contact != None:
        print(f'Name: {contact.name}')
        print(f'Previous hours worked: {contact.get_hours_worked()}')
        session_length = read_float('Session length: ')
        if contact.add_session(session_length):
            print(f'Updated hours worked: {contact.get_hours_worked()}')
        else:
            print('Add hours failed')
    else:
        print('This name was not found')






try:
    load_contact()
except Exception:
    print('Contacts file not found')
    contacts = []
else:
    print('Contacts loaded successfully!')

menu = '''Tiny Contact

1.New contact
2.Find contact
3.Edit contact
4.Add session
5.Save contact
6.Load contact
7.Exit program

Enter command: '''

while True:
    command = menu_selector(menu, 1, 7)
    if command == 1:
        new_contact()
        print(contacts)
    elif command == 2:
        display_contact()
    elif command == 3:
        edit_contact()
    elif command == 4:
        add_session_to_contact()
    elif command == 5:
        save_contact()
    elif command == 6:
        print('Load contacts')
        try:
            load_contact()
            for contact in contacts:
                print(f'Name: {contact.name}')
                print(f'Address: {contact.address}')
                print(f'Phone: {contact.telephone}')
                print(' ')
        except Exception:
            print('Something went wrong!')
        else:
            print('Contacts loaded successfully!')
    elif command == 7:
        break

