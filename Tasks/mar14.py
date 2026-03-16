###-----------------------TASK 1--------------------------
##import tkinter as tk
##
##def Convert():
##    Celsius=float(Cels.get())
##    Farhenheit=(Celsius * 9/5)+32
##    result.config(text=f"Farenheit : {Farhenheit}")
##
##root=tk.Tk()
##root.title("Temperature Converter")
##root.geometry("500x300")
##root.config(bg="beige")
##
##heading=tk.Label(root,text="TEMPERATURE CONVERTER",font=("calibri",20,"bold italic"),fg="white",bg="purple")
##heading.pack()
##
##tk.Label(root,text="Enter Temperature in Celcius").pack(pady=5)
##Cels=tk.Entry(root)
##Cels.pack()
##
##tk.Button(root,text="Convert",command=Convert).pack(pady=5)
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()
##
##
##
###-----------------------TASK 2--------------------------
##import tkinter as tk
##import numpy as np
##import pandas as pd
##import matplotlib.pyplot as plt
##
##def generate():
##    n=np.random.randint(1,100,20)
##    df=pd.DataFrame(n,columns=["Numbers"])
##
##    mean=np.mean(df["Numbers"])
##    median=np.median(df["Numbers"])
##    std=np.std(df["Numbers"])
##
##    result.config(text=f"Mean: {mean}\nMedian: {median}\nStd Dev: {std}")
##
##    plt.hist(df["Numbers"])
##    plt.title("Random Number Histogram")
##    plt.xlabel("Numbers")
##    plt.ylabel("Frequency")
##    plt.show()
##
##root=tk.Tk()
##root.title("Random Number Statistics")
##root.geometry("700x300")
##
##heading=tk.Label(root,text="RANDOM NUMBER STATISTICS ANALYZER",font=("Georgia", 20, "italic"),fg="white",bg="black")
##heading.pack(pady=5)
##
##button=tk.Button(root,text="Generate Numbers",command=generate)
##button.pack(pady=5)
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()



##print("-----------------------TASK 3--------------------------")
##class Book:
##    def __init__(self,title,auther,price):
##        self.title=title
##        self.auther=auther
##        self.price=price
##
##    def display(self):
##        print(f"Book Title : {self.title}")
##        print(f"Book Auther : {self.auther}")
##        print(f"Book Price : {self.price}")
##        print()
##
##b1=Book("Romeo Juliet","W Shakespere","Rs.1200")
##b1.display()
##
##b2=Book("Ramayana Darshanam","Kuvempu","Rs.1500")
##b2.display()        



##print("-----------------------TASK 4--------------------------")
##class Product:
##    def __init__(self,name,price):
##        self.name=name
##        self.price=price
##
##class Cart:
##    def __init__(self):
##        self.products=[]
##
##    def add_product(self,product):
##        self.products.append(product)
##
##    def total_price(self):
##        total=0
##        for p in self.products:
##            total=total+p.price
##        return total
##
##cart=Cart()
##
##n=int(input("Enter number of products: "))
##
##for i in range(n):
##    name=input("Enter product name: ")
##    price=float(input("Enter price: "))
##    
##    p=Product(name,price)
##    cart.add_product(p)
##
##print("Total:",cart.total_price())



##print("-----------------------TASK 5--------------------------")
##class ATM:
##    def __init__(self):
##        self.balance=0
##
##    def check_balance(self):
##        print("Balance:",self.balance)
##        print()
##
##    def deposit(self):
##        amount=int(input("Enter deposit amount: "))
##        self.balance=self.balance+amount
##        print("Money deposited")
##
##    def withdraw(self):
##        amount=int(input("Enter withdraw amount: "))
##        if amount<=self.balance:
##            self.balance=self.balance-amount
##            print("Money withdrawn")
##            print("Available balance: ",self.balance)
##            print()
##        else:
##            print("Insufficient balance")
##            print()
##
##    def exit_system(self):
##        print("Thank you for using ATM")
##        print()
##        exit()



##atm = ATM()
##while True:
##    print("\n1. Check Balance")
##    print("2. Deposit ")
##    print("3. Withdraw ")
##    print("4. Exit")
##
##    c=int(input("Enter choice: "))
##    
##    if c==1:
##        atm.check_balance()
##    elif c==2:
##        atm.deposit()
##    elif c==3:
##        atm.withdraw()
##    elif c==4:
##        atm.exit_system()
##print()



print("-----------------------TASK 6--------------------------")
class Student:
    def __init__(self,name):
        self.name=name

class Teacher:
    def __init__(self,name):
        self.name=name

class Course:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.teacher=None

    def add_student(self,student):
        self.students.append(student)

    def assign_teacher(self,teacher):
        self.teacher=teacher

    def display(self):
        print("COURSE DETAILS:")
        print("Course Name:",self.name)
        print("Teacher:",self.teacher.name)
        print()
        print("Students:")
        for s in self.students:
            print(s.name)
        print()

course_name=input("Enter course name: ")
course=Course(course_name)

teacher_name=input("Enter teacher name: ")
teacher=Teacher(teacher_name)

course.assign_teacher(teacher)

n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter student name: ")
    student=Student(name)
    course.add_student(student)
course.display()



print("-----------------------TASK 7--------------------------")
for n in range(2,101):
    prime=True

    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime:
        print(n,end=" ")
print()



print("-----------------------TASK 8--------------------------")

s="ABCDEFGHIJKL"

print("String :",s)
print()
print(s[2:9:2])
print(s[-2:-10:-1])
print(s[-2:-12:-1])
print(s[-2:-9:-2])
print(s[::4])
print()

print("##################################")
s="Python String Slicing Example"
print("String :",s)
print()
print(s[12::-1])     
print(s[14:])        
print(s[-1::-3])     
print(s[0::4])     
print(s[-1:-8:-1])        
print(s[12::-4])    
print()



print("-----------------------TASK 9--------------------------")
l=["Cat","Dog","Lion","Tiger","Rabbit","Monkey"]
print("List :",l)
print()
print(l[2])
print(l[-1],l[-2])
print(l[3:0:-1])
print(l[:4:3])
print(l[3::-3])
print(l[-1:-5:-3])
print(l[-2::-2])
print(l[::-1])
print()


print("##################################")
l=["apple","banana","cherry"]
print("List :",l)
print()
l.append("orange")
print(l)

l.insert(3,"cherry")
print(l)

l.extend(["kiwi","grape"])
print(l)
print()


print("##################################")
l=[10,20,30,40,50]
print("List :",l)
print()
l[2]=300
print(l)

l[1],l[2],l[3]=200,3000,400
print(l)
print()

print("##################################")
l=[1,2,3]
print("List :",l)
print()
l.insert(1,100)
print(l)

l[-1]=999
print(l)
print()


print("##################################")
l=[10,20,30,40,50]

print("List :",l)
print()
l.append(60)
print(l)

l.insert(0,5)
print(l)

l.extend([70,80,90])
print(l)
print()


print("##################################")
l=[42,3.14,"Hello",True]
print("List :",l)
print()

l[0]=2.718
print(l)

l.append(True)
print(l)

l.insert(1,False)
print(l)

l[0]=5
l.pop(1)
print(l)
print()


print("##################################")
s="Hello World, Welcome to Python!"
print("String :",s)
print()

print(s.upper())
print(s.lower())
print(s.split(" "))
print(s.split("o"))
print(s.replace("W","X"))














