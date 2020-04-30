#contact prototype

from inputs import *
import pickle


contacts = []

class Contact(object):

    min_session_length = 0.5
    max_session_length = 3.5

    __min_text_length = 4
    __open_fee = 30
    __hourly_fee = 50

    @staticmethod
    def valid_text(text):
        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not Contact.valid_text(name):
            raise Exception('Invalid length')
        self.__name = name


    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        if not Contact.valid_text(address):
            raise Exception('Invalid length')
        self.__address = address



    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone


    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.__hours_worked = 0
        self.__billing_amount = 0
        self.__version = 1.0



    def get_hours_worked(self):
        return self.hours_worked

    @property
    def hours_worked(self):
        return self.__hours_worked
    @hours_worked.setter
    def hours_worked(self, hours_worked):
        return self.__hours_worked

    @property
    def billing_amount(self):
        return self.__billing_amount

    def check_version(self):
        pass

    @staticmethod
    def validate_session_length(session_length):
        if session_length < Contact.min_session_length:
            return False
        if session_length > Contact.max_session_length:
            return False
        return True

    def add_session(self, session_length):
        if not Contact.validate_session_length(session_length):
            raise Exception('Invalid session length')
        self.__hours_worked = self.__hours_worked + session_length
        amount_to_bill = Contact.__open_fee + (Contact.__hourly_fee * session_length)
        self.__billing_amount = amount_to_bill
        return True



def new_contact():
    print('Create new contact')
    name = read_text('Enter contact name: ')
    address = read_text('Enter contact address: ')
    telephone = read_text('Enter contact phone: ')
    new_contact = Contact(name, address, telephone)
    contacts.append(new_contact)


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


def display_contact():
    print('Find contact')
    contact = find_contact(read_text('Enter contact name: '))
    if contact != None:
        print(f'Name: {contact.name}')
        print(f'Address: {contact.address}')
        print(f'Phone: {contact.telephone}')
        print(f'Hours on the case: {contact.hours_worked}')
        print(f'Amount to bill: {contact.billing_amount}')



    else:
        print('This name was not found')


def edit_contact():
    print('Edit contact')
    contact = find_contact(read_text('Name: '))
    if contact != None:
        print('Enter (.) to leave unchaged')
        name = read_text('Name: ')
        address = read_text('Address: ')
        telephone = read_text('Telephone: ')
        if name != '.':
            contact.name = name
        if address != '.':
            contact.address = address
        if telephone != '.':
            contact.telephone = telephone
    else:
        print('This name was not found')


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
    for contact in contacts:
        contact.check_version()


def delete_contact():
    print('Delete contact')
    if len(contacts) == 0:
        print('Contacts list empty!')
    else:
        contact = find_contact(read_text('Name: '))
        confirm = read_text(f'Delete {contact.name}??\nYes or No: ')
        confirm = confirm.strip()
        confirm = confirm.lower()
        option1, option2 = ['yes', 'y'], ['no', 'n']
        if confirm in option1:
            contacts.remove(contact)
            print('Contact deleted successfully!')
        elif confirm in option2:
            print('Operation cancelled.')




def add_session_to_contact():
    print('Add session')
    search_name = read_text('Contact name: ')
    contact = find_contact(search_name)
    if contact != None:
        print(f'Name: {contact.name}')
        print(f'Previous hours worked: {contact.hours_worked}')
        session_length = read_float('Session length: ')
        try:
            contact.add_session(session_length)
            print(f'Updated hours worked: {contact.hours_worked}')
        except Exception as e:
            print('Add hours failed: ', e)
    else:
        print('This name was not found')






try:
    load_contact()
except Exception:
    print('Contacts file not found')
    contacts = []
else:
    print('Contacts loaded successfully!')
finally:
    print(f'Contacts available: {len(contacts)}')

menu = '''Tiny Contact

1.New contact
2.Find contact
3.Edit contact
4.Add session
5.Save contact
6.Delete contact
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
       delete_contact()
       save_contact()
    elif command == 7:
        break

