#!/usr/bin/env python3

# File Name: TestContact.py

class ContactList(list):
    """ Return all contacts that contains the search value 
    in their name.
    """
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
        
        
class Contact:
    """ Initialize a list for all contacts so that
    only one list exists for any instances of Contact
    """
    all_contacts = ContactList()
    
    """ What is in a Contact"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
        
class Supplier(Contact):
    """What if we have suppliers in our contacts that
    we want to give an order() method exclusively to them.
    By inheriting the Contact parent class, Supplier sub class
    is able to get the same attributes yet have an exclusive
    method supplied to it.
    """
    def order(self, order):
        print("If this were a real system, we would send "\
              "'{0}' order to '{1}'".format(order, self.name))