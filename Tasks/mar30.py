print("#------------------------------TASK 1--------------------------------")
s="Machine Learning"
print("Original String: ",s)
print(s.upper())
print(s.lower())

l=[s[:5],s[6:12],s[4],s[-1]]
print(l)
print()



print("#------------------------------TASK 2--------------------------------")
s="Plants need air, water and sunlight to grow"
print("Original String: ",s)

print(s[12:26])
print(s[15::-1])
print(s[7:35:3])
print(s[::-1])
print(s[2::5])
print()



print("#------------------------------TASK 3--------------------------------")
s="Indentation is very important in Python"
print("Original String: ",s)

print(s[-11:-20:-1])
print(s[-2:-19:-2])
print(s[13::-1])
print()



print("#------------------------------TASK 4--------------------------------")
l=[10,20,30,40,50]
print("Original List: ",l)

l.insert(3,35)
print(l)

l.append(60)
print(l)
print()



print("#------------------------------TASK 5--------------------------------")
l=["Lion","Tiger","Elephant","Leopard"]
print("Original List: ",l)

l.insert(1,"Cheetah")
print(l)

l.append("Monkey")
print(l)

l.insert(0,"Giraffe")
print(l)
print()



print("#------------------------------TASK 6--------------------------------")
t=(10,20,30,40)
print("Tuple: ",t)

l=list(t)
l.remove(30)
t=tuple(l)

print(t)
print()



print("#------------------------------TASK 7--------------------------------")
m=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(m[1])
print(m[2],m[3])

print([row[0] for row in m])

print([row[2:] for row in m[1:3]])

print([m[i][i] for i in range(len(m))])

print([m[i][len(m)-1-i] for i in range(len(m))])
print()




print("#------------------------------TASK 8--------------------------------")
m=[
    [1,2,3,4],
    [3,6,8,9],
    [4,7,9,10],
    [5,8,10,12]
]
m.append([6,6,6,6])
print(m)

m.insert(2,[20,25,30,35])
print(m)
print()




print("#------------------------------TASK 9--------------------------------")

def check(p):
    u,l,d,s=0,0,0,0

    for i in p:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        elif i.isdigit():
            d+=1
        else:
            s+=1

    if u and l and d and s and len(p)>=8:
        return "Strong"
    elif (u or l) and d:
        return "Medium"
    else:
        return "Weak"

print(check(input("Enter password: ")))
print()




print("#------------------------------TASK 10--------------------------------")

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,b):
        self.books.append(b)
        print("Added: ",b)

    def issue_book(self,b):
        if b in self.books:
            self.books.remove(b)
            print("Issued: ",b)
        else:
            print("Not available")

    def return_book(self,b):
        self.books.append(b)
        print("Returned: ",b)

    def show(self):
        print("Available: ",self.books)

l=Library()

l.add_book("Python")
l.add_book("ML")

l.show()

l.issue_book("Python")
l.show()

l.return_book("Python")
l.show()

print()




print("#------------------------------TASK 11--------------------------------")

pin=1234
balance=1000
attempt=0

while attempt<3:
    p=int(input("Enter PIN: "))
    
    if p==pin:
        while True:
            print("1.Deposit 2.Withdraw 3.Balance 4.Exit")
            ch=int(input("Enter choice: "))
            
            if ch==1:
                amt=int(input("Amount: "))
                balance+=amt
                print("Balance:",balance)
            
            elif ch==2:
                amt=int(input("Amount: "))
                if amt<=balance:
                    balance-=amt
                    print("Balance:",balance)
                else:
                    print("Insufficient balance")
            
            elif ch==3:
                print("Balance:",balance)
            
            else:
                break
        break
    else:
        attempt+=1
        print("Wrong PIN")

if attempt==3:
    print("Account blocked")
print()



print("#------------------------------TASK 12--------------------------------")

import pandas as pd

df=pd.read_csv("C:\\Users\\Hp\\Desktop\\Internship Program\\task\\mark.csv")

print("Average: ",df["Marks"].mean())

top=df[df["Marks"]==df["Marks"].max()]
print("Topper:")
print(top)

f=df[df["Marks"]>75]
print("Above 75 :")
print(f)
print()



print("#------------------------------TASK 13--------------------------------")

import matplotlib.pyplot as plt

products=["A","B","C","D"]
sales=[100,150,80,120]

months=["Jan","Feb","Mar","Apr"]
growth=[10,20,15,25]

categories=["Electronics","Clothing","Food"]
share=[40,35,25]

plt.bar(products,sales)
plt.title("Sales per product")
plt.show()

plt.plot(months,growth)
plt.title("Monthly growth")
plt.show()

plt.pie(share,labels=categories,autopct="%1.1f%%")
plt.title("Category share")
plt.show()
print()




print("#------------------------------TASK 14--------------------------------")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
import tkinter as tk

df=pd.read_csv("iris.csv")

x=df.drop(columns=["Id","Species"])
y=df["Species"]

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)

model=DecisionTreeClassifier()
model.fit(x_train,y_train)

joblib.dump(model,"model.pkl")

model=joblib.load("model.pkl")

def predict():
    vals=[
          float(e1.get()),
          float(e2.get()),
          float(e3.get()),
          float(e4.get())
          ]
    r=model.predict([vals])
    res.config(text="Prediction: "+r[0])

root=tk.Tk()
root.geometry("350x400")
root.title("Iris Prediction")

title=tk.Label(root,text="Iris prediction",font=("Arial",14,"bold italic"))
title.pack(pady=10)

tk.Label(root,text="Sepal Length").pack()
e1=tk.Entry(root)
e1.pack(pady=5)

tk.Label(root,text="Sepal Width").pack()
e2=tk.Entry(root)
e2.pack(pady=5)

tk.Label(root,text="Petal Length").pack()
e3=tk.Entry(root)
e3.pack(pady=5)

tk.Label(root,text="Petal Width").pack()
e4=tk.Entry(root)
e4.pack(pady=5)

b=tk.Button(root,text="Predict",command=predict)
b.pack(pady=15)

res=tk.Label(root,text="",font=("Arial",12))
res.pack(pady=10)

root.mainloop()

print()




print("#------------------------------TASK 15--------------------------------")

class Cart:
    def __init__(self):
        self.items={}

    def add(self,name,price):
        self.items[name]=price
        print("Added:",name)

    def remove(self,name):
        if name in self.items:
            del self.items[name]
            print("Removed:",name)

    def total(self):
        t=sum(self.items.values())
        print("Total:",t)

    def discount(self,per):
        t=sum(self.items.values())
        d=t-(t*per/100)
        print("After discount:",d)

    def show(self):
        print("Cart:",self.items)

c=Cart()

c.add("Pen",20)
c.add("Book",100)
c.show()

c.remove("Pen")
c.show()

c.total()
c.discount(10)
print()




print("#------------------------------TASK 16--------------------------------")

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg=self.average()
        if avg>=90:
            return "A"
        elif avg>=75:
            return "B"
        elif avg>=50:
            return "C"
        else:
            return "F"

s=Student("Prajwal",[85,78,92,88])

print("Name:",s.name)
print("Total:",s.total())
print("Average:",s.average())
print("Grade:",s.grade())

print()
