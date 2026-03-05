####TASK 1:
##print("-------------TASK 1-------------")
##print("Welcome to AIML Academy\n")
##
##name=input("Enter Full Name: ")
##age=input("Enter Age: ")
##fee=input("Enter Course Fee: ")
##email=input("Enter Email: ")
##
##part=name.split()
##
##fn=part[0]
##
##ini=part[0][0]+"." +part[1][0]+"."
##
##age=int(age)
##fee=float(fee)
##email=email.lower()
##
##print("\nStudent registration details")
##print(f"Student Name: {name}")
##print(f"Initials: {ini}")
##print(f"Age: {age}")
##print(f"Course fee: Rs.{fee:.2f}")
##print(f"Email: {email}")
##print()
##
##
####TASK 2:
##print("-------------TASK 2-------------")
##sale=[]
##
##for i in range(1,6):
##    x=int(input(f"Enter sale amount {i}: "))
##    sale.append(x)
##
##print("\nDaily Sales:",sale)
##
##total=sum(sale)
##avg=total/len(sale)
##
##print("Total Revenue:", total)
##print("Average Revenue:", avg)
##
##asc=sorted(sale)
##des=sorted(sale,reverse=True)
##
##print("Ascending Order:", asc)
##print("Descending Order:", des)
##
##low=min(sale)
##sale.remove(low)
##
##print("Lowest sale removed:", low)
##print("Updated Sales List:", sale)
##
##for i in sale:
##    if i<1000:
##        print("Low Sales Alert Triggered")
##        break
##print()
##
##
####TASK 3
##print("-------------TASK 3-------------")
##e1={
##    "ID":101,
##    "Name":"Prajwal",
##    "Department":"AI",
##    "Skills": {"Python","ML","SQL"}
##}
##e2={
##    "ID": 102,
##    "Name":"Pradeep",
##    "Department": "AI",
##    "Skills": {"Python","SQL","Deep Learning","NLP"}
##}
##
##e1["Skills"].add("NLP")
##
##all_skills=e1["Skills"].union(e2["Skills"])
##common_skills=e1["Skills"].intersection(e2["Skills"])
##
##print("All Skills (Union): ",all_skills)
##print("Common Skills (Intersection): ",common_skills)
##
##salary=("Grade A",50000,70000)
##
##grade,min_sal,max_sal=salary
##
##print("Salary Grade:", grade)
##print("Salary Range:", min_sal,"-",max_sal)
##
##print("\nEmployee 1 Details:")
##for key,value in e1.items():
##    print(key,": ",value)
##    print()
##print()
##
##
####TASK 4:
##print("-------------TASK 4-------------")
##
##class Person:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def get(self):
##        return self.name
##
##class Doctor(Person):
##    def __init__(self,name,age,spec):
##        super().__init__(name,age)
##        self.spec=spec
##    def get(self):
##        return f"Doctor {self.name}, Specialization: {self.spec}"
##
##class Patient(Person):
##    def __init__(self,name,age):
##        if age<0:
##            raise ValueError("Age cannot be negative")
##        super().__init__(name,age)
##        self.__record="Normal"
##    def get(self):
##        return f"Patient {self.name}, Age: {self.age}"
##
##try:
##    d1=Doctor("Dr. Mehta",45,"Cardiology")
##    p1=Patient("Ravi",30)
##    print(d1.get())
##    print(p1.get())
##except:
##    print("Something went wrong")
##print()
##
####TASK 5:
##print("-------------TASK 5-------------")
##import numpy as np
##import pandas as pd
##
##marks=np.array([85,90,78,90,85,88])
##
##arr=marks.reshape(3,2)
##print("2D Array:")
##print(arr)
##
##df=pd.DataFrame(arr,columns=["Maths","Science"])
##
##df.loc[1,"Science"]=None
##
##mean=df["Science"].mean()
##df["Science"]=df["Science"].fillna(mean)
##
##df=df.drop_duplicates()
##
##print("\nCleaned DataFrame:")
##print(df)
##
##print("\nSummary Statistics:")
##print(df.describe())
##print()

####TASK 6:
##import tkinter as tk
##
##root=tk.Tk()
##root.title("Color theme switcher")
##root.geometry("300x200")
##
##label=tk.Label(root,text="Enter name")
##label.pack(pady=5)
##
##entry=tk.Entry(root)
##entry.pack(pady=5)
##
##def light_mode():
##    root.config(bg="white")
##    label.config(bg="white",fg="black")
##    entry.config(bg="white",fg="black")
##
##def dark_mode():
##    root.config(bg="black")
##    label.config(bg="black",fg="white")
##    entry.config(bg="gray",fg="white")
##
##def blue_mode():
##    root.config(bg="lightblue")
##    label.config(bg="lightblue",fg="darkblue")
##    entry.config(bg="white",fg="darkblue")
##
##b1=tk.Button(root,text="Light Mode",command=light_mode)
##b1.pack(pady=2)
##
##b2=tk.Button(root,text="Dark Mode",command=dark_mode)
##b2.pack(pady=2)
##
##b3=tk.Button(root,text="Blue Theme",command=blue_mode)
##b3.pack(pady=2)
##
##root.mainloop()


##TASK 7:
print("-------------TASK 7-------------")

import datetime as dt
import random
import math
import os
import sys

now=dt.datetime.now()

print("\nPatient checkin details")
print("Date :",now.strftime("%d-%m-%Y"))
print("Time :",now.strftime("%I:%M %p"))
print("Day  :",now.strftime("%A"))

doc_list=["Dr. Sudeep","Dr. Krishnamurthy","Dr. Prabhachandra"]
doc=random.choice(doc_list)
room=random.randint(100,500)

print("\nDoctor assignment")
print("Doctor Name :",doc)
print("Room Number :",room)

amount=2500
tax=amount*0.05
final=math.ceil(amount+tax)

print("\nBilling details")
print("Base Amount :",amount)
print("Tax Amount  :",int(tax))
print("Final Bill  :",final)

print("\nPatient Record Status")

if os.path.exists("patient.txt"):
    print("File exists")
else:
    f=open("patient.txt","w")
    f.close()
    print("File dont exists")
    print("File created successfully!")

print("\nSystem Information")
print("Python Version:", sys.version)
print("Program closed safely.")



















