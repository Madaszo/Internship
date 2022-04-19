from ast import Add, Delete
from datetime import datetime
from pickle import TRUE

class Customer:
    def __init__(self):
        self.name = input("Name: ")
        self.vat =  input("Vat: ")
        self.address = input("Address: ")
        self.time = datetime.now()
        self.next = None
    
    def edit(self):
        editing = True
        while(editing):
            val = input("Do you want to change (N)ame, (A)ddress or (E)xit editing?")
            if val == "E" or val =="e":
                editing = False
            elif val == "N" or val == "n":
                self.name = input("Name: ")
            elif val == "A" or val == "a":
                self.address = input("Address: ")

    def show(self):
        print( self.name, self.vat, self.address, self.time.strftime("%d/%m/%Y %H:%M:%S"))

class Customer_book:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def add_customer(self):
        if self.head is None:
            self.head = Customer()
            self.tail = self.head
        else:
            self.tail.next = Customer()
            self.tail = self.tail.next
    
    def edit_customer(self):
        vat = input("Provide VAT number of a customer: ")
        tmp = self.head
        while(tmp is not None):
            if tmp.vat == vat:
                tmp.edit()
                break
            tmp = tmp.next
        
        if tmp is None:
            print("There is no such a customer")

    def delete_customer(self):
        vat = input("Provide Vat number of a customer: ")
        if self.head.vat == vat:
            self.head = self.head.next
        else:
            tmp = self.head
            p = self.head.next
            while p is not None:
                if p.vat == vat:
                    tmp.next = p.next
                    break
                tmp = p
                p = p.next
            if p is None:
                print("There is no such a customer")

    def list_customers(self):
        tmp = self.head
        while(tmp is not None):
            tmp.show()
            tmp = tmp.next

working = True
book = Customer_book()
while(working):
    c = input("(A)dd a customer, (E)dit a customer, (D)elete a customer, (L)ist customers, (S)top working: ")
    if c == "A" or c == "a":
        book.add_customer()
    elif c == "E" or c == "e":
        book.edit_customer()
    elif c == "D" or c == "d":
        book.delete_customer()
    elif c == "L" or c == "l":
        book.list_customers()
    elif c == "S" or c == "s":
        working = False
