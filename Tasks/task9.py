class Employee:
    comp_name="XYZ"

    def __init__(self,name,emp_id):
        self.Name=name
        self.Emp_id=emp_id

    def display(self):
        print(f"Name : {self.Name}")
        print(f"ID : {self.Emp_id}")
        print(f"Company name :{Employee.comp_name}")
        print()

e1=Employee("Ram","E1")
e2=Employee("Sham","E2")

e1.display()
e2.display()


class Student:
    def __init__(self,name,roll_no):
        self.Name=name
        self.Roll=roll_no

    def display(self):
        print(f"Name :{self.Name}")
        print(f"Roll No :{self.Roll}")
        print()

s1=Student("Nick",21)
s2=Student("Ram",16)

s1.display()
s2.display()


class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def display(self):
        print("ID:",self.emp_id)
        print("Name:",self.name)
        print("Salary:",self.salary)
        print()


e1=Employee(1,"Prajwal",50000)
e2=Employee(2,"Pradeep",30000)
e1.display()
e2.display()

class College:
    col_name="Sahyadri"

    def __init__(self,name,branch):
        self.Name=name
        self.Branch=branch

    def display(self):
        print(f"Name : {self.Name}")
        print(f"Branch : {self.Branch}")
        print(f"College name :{College.col_name}")
        print()

e1=College("Ram","CSE")
e2=College("Sham","ECE")

e1.display()
e2.display()



class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:",self.__balance)
        print()


b=BankAccount()
b.deposit(1000)
b.withdraw(500)
b.show_balance()


class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks!!")

a1=Dog()
a1.sound()
a1.bark()


class Vehicle:
    def start(self):
        print("Vehicle")


class Car(Vehicle):
    def drive(self):
        print("Car ")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


e=ElectricCar()
e.start()
e.drive()
e.charge()


class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print()


m1=Mobile("Samsung",20000)
m2=Mobile("Apple",80000)
m3=Mobile("OnePlus",35000)

m1.display()
m2.display()
m3.display()


class Laptop:
    def __init__(self,ram,processor,storage):
        self.Ram=ram
        self.Processor=processor
        self.Storage=storage

    def display(self):
        print("RAM:",self.Ram)
        print("Processor:",self.Processor)
        print("Storage:",self.Storage)
        print()


l1 = Laptop("16GB","Ryzen5","512GB")
l1.display()




















