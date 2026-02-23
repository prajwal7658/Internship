#1
print("#1.")
import os

if os.path.exists("dairy.txt"):
    print("Diary already exists")
else:
    print("Diary not found, creating new diary")

    f=open("dairy.txt","w")
    f.write("Hello\n")
    f.write("Today is saturday\n")
    f.write("I go to gym daily\n")
    f.write("Tomorrow is sunday\n")
    f.write("Python is easy\n")
    f.close()

f=open("dairy.txt","r")
data=f.read()
print("\nDiary content:")
print(data)

print("First 50 characters:")
print(data[:50])

f=open("dairy.txt","r")
print("\nReading line by line:")
print(f.readline())
print(f.readline())
f.close()


os.remove("dairy.txt")
print("\nDiary deleted\n")

#2.
print("#2.")
mn=input("Enter mobile number: ")
budget=int(input("Enter your budget: "))

if budget==199:
    print("Plan selected: 28 days validity")
elif budget==299:
    print("Plan selected: 56 days validity")
elif budget==499:
    print("Plan selected: 84 days validity")
else:
    print("Sorry, no plan available for this amount")
print()

#3.
print("#3.")

clothType=input("Enter clothes type (cotton/wool/synthetic): ")
count=int(input("Enter number of clothes: "))
weight=float(input("Enter weight per cloth (kg): "))

total=count*weight

if total<=7:
    status="Wash started"
else:
    status="Overload. Reduce clothes"

print("\nClothes type:", clothType)
print("Total Weight:", total,)
print("Status:", status)
print()


#4
print("#4.")
class BusTicket:
    def __init__(self,name,busno,seatno):
        self.name=name
        self.busno=busno
        self.seatno=seatno

    def show(self):
        print("\npassenger name:", self.name)
        print("Bus number:", self.busno)
        print("Seat number:", self.seatno)

t1 = BusTicket("Prajwal","KA70MN5676",12)
t2 = BusTicket("Pradeep","KA19HN0283",7)

t1.show()
t2.show()
print()


#5.
print("#5.")
class Mobile:
    def __init__(self, pin):
        self.__pin = pin

    def verify(self,entered):
        if entered==self.__pin:
            print("PIN correct")
        else:
            print("Wrong PIN")

    def change(self,old,new):
        if old==self.__pin:
            self.__pin=new
            print("PIN changed successfully")
        else:
            print("Old PIN incorrect")

m=Mobile(1234)

m.verify(1234)
m.change(1234,5678)
m.verify(5678)
print()

#6.
print("#6.")
import datetime as dt
import math
import os

name=input("Enter name: ")
city=input("Enter destination city: ")
n=int(input("Enter number of travelers: "))
price=float(input("Enter cost per ticket: "))

now=dt.datetime.now()

total=n*price
service=total*0.05
final_amount=total+service

final_amount=math.ceil(final_amount)

if os.path.exists("book.txt"):
    print("Booking file already exists")
else:
    print("Creating booking file")

f = open("booking.txt","w")

f.write("Customer name: " +name+"\n")
f.write("Destination: " +city+"\n")
f.write("Number of travelers: "+str(n)+"\n")
f.write("Final Cost: " +str(final_amount)+"\n")
f.write("Booking Time: " +str(now)+"\n")

f.close()

print("\nBooking Time:", now)
print("Final Cost:", final_amount)
print("Booking confirmed")
print()


#7.
print("#7")
import datetime as dt
import os
import sys

name=input("Enter patient name: ")
age=int(input("Enter age: "))
temp=float(input("Enter body temperature: "))
heart=int(input("Enter heart rate: "))

now=dt.datetime.now()

if temp>37.5:
    status="Fever present"
else:
    status="normal"

if os.path.exists("health_report.txt"):
    print("Report file already exists")
else:
    print("Creating new report file")

f=open("health_report.txt", "w")

f.write("Patient Name: "+ name +"\n")
f.write("Age: " +str(age)+"\n")
f.write("Temperature: " +str(temp)+"\n")
f.write("Heart Rate: " +str(heart)+"\n")
f.write("Status: " + status +"\n")
f.write("Checkup Time: " +str(now)+"\n")

f.close()
print()

#8
print("#8")
import math
import datetime as dt
import os

temp=[]

for i in range(5):
    t=float(input("Enter temperatures: "))
    temp.append(t)

maxt=max(temp)
mint=min(temp)
avg=sum(temp)/len(temp)

avg=math.ceil(avg)

if avg>=35:
    cat="Hot week"
elif avg>=20:
    cat="Pleasant week"
else:
    cat="Cold week"

if os.path.exists("weather_report.txt"):
    print("Weather file already exists")
else:
    print("Creating weather file")

f=open("weather_report.txt","w")

f.write("Report Date: " +str(dt.datetime.now())+"\n")
f.write("Maximum Temperature: "+str(maxt)+"\n")
f.write("Minimum Temperature: "+str(mint)+"\n")
f.write("Average Temperature: "+str(avg)+"\n")
f.write("Weather Type: " + cat+"\n")

f.close()
print()

#9
print("#9.")
import tkinter as tk
def add():
    n1=float(e1.get())
    n2=float(e2.get())
    result.config(text="Result: "+str(n1+n2))

def sub():
    n1=float(e1.get())
    n2=float(e2.get())
    result.config(text="Result: "+str(n1-n2))

def mul():
    n1=float(e1.get())
    n2=float(e2.get())
    result.config(text="Result: "+str(n1*n2))

def div():
    n1=float(e1.get())
    n2=float(e2.get())
    result.config(text="Cannot divide by zero")

root=tk.Tk()
root.title("Calculator")

e1=tk.Entry(root)
e1.pack()
e2=tk.Entry(root)
e2.pack()

tk.Button(root,text="Add",command=add).pack()
tk.Button(root,text="Subtract",command=sub).pack()
tk.Button(root,text="Multiply",command=mul).pack()
tk.Button(root,text="Divide",command=div).pack()

result=tk.Label(root,text="Result:")
result.pack()

root.mainloop()



#10.
print("#10.")
import datetime as dt
import random
import math
import os
import sys

now=dt.datetime.now()
print("Current Date:",now.date())
print("Current Time:",now.time())
print("Day:", now.strftime("%A"))

roads = ["north road","south road","east road","west road"]
green_road=random.choice(roads)
duration=random.randint(30,90)

print("\nGreen signal for:",green_road)
print("Green light duration:",duration,"seconds")

units=[120,150,130,140,110]

total=sum(units)
average=total/len(units)
rounded=math.ceil(total)

print("\nElectricity used:",total)
print("Average daily usage:",average)
print("Rounded units:",rounded)

if os.path.exists("complaints.txt"):
    print("\nfile already exists")
else:
    print("\nCreating file")
    f=open("complaints.txt", "w")
    f.close()

print("File name:", "complaints.txt")
print("File size:", os.path.getsize("complaints.txt"))
print()



#11
print("#11")
import numpy as np
import pandas as pd

marks=np.array([85,90,78,90,85,88])


marks_2d=marks.reshape(3,2)
print(marks_2d)

df=pd.DataFrame(marks_2d,columns=["Maths","Science"])

df.loc[1,"Science"]=None

df["Science"]=df["Science"].fillna(df["Science"].mean())

df=df.drop_duplicates()

print("\nCleaned dataFrame:\n")
print(df)
print("\nSummary tsatistics:\n")
print(df.describe())

































