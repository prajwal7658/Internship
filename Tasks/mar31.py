##print("----------------------TASK 1----------------------")
##s="Python Programming Language"
##print("String :",s)
##
##print(s[7:18])
##print(s[::-1])
##print(s[1::2])
##print(s[-1:-11:-1])
##print()
##
##
##
##print("----------------------TASK 2----------------------")
##s="Artificial Intelligence"
##print("String :",s)
##
##s1=s[11::]
##print(s1)
##
##s2=s[9::-1]
##print(s1)
##
##s3=s2+ " " +s1[::-1]
##print(s3)
##print()
##
##
##
##
##print("----------------------TASK 3----------------------")
##l=[5,15,25,35,45]
##print("List :",l)
##
##l.insert(3,30)
##print(l)
##
##l.remove(15)
##print(l)
##
##l.append(50)
##print(l)
##
##l[3]=100
##print(l)
##print()
##
##
##
##
##print("----------------------TASK 4----------------------")
##l=["Apple","Banana","Cherry"]
##print("List :",l)
##
##l.insert(0,"Mango")
##print(l)
##
##l.insert(2,"Orange")
##print(l)
##
##l.remove("Apple")
##print(l)
##
##l.sort()
##print(l)
##
##print()
##
##
##
##
##print("----------------------TASK 5----------------------")
##m=[
##    [2,4,6],
##    [8,10,12],
##    [14,16,18]
##]
##print("Matrix :",m)
##
##print([r[0] for r in m])
##
##print([m[i][i] for i in range(len(m))])
##
##print(m[-1])
##print()
##
##
##
##
##print("----------------------TASK 6----------------------")
##m=[
##    [1,2,3],
##    [4,5,6]
##]
##print("Matrix :",m)
##
##m.append([7,8,9])
##print(m)
##
##m.insert(0,[0,0,0])
##print(m)
##print()
##
##
##
##
##print("----------------------TASK 7----------------------")
##import json
##
##data=[
##    {"name":"A","marks":80},
##    {"name":"B","marks":60}
##]
##
##with open("students.json","w") as f:
##    json.dump(data,f)
##
##with open("students.json","r") as f:
##    d=json.load(f)
##print(d)
##
##top=max(d,key=lambda x:x["marks"])
##print(top)
##
##d.append({"name":"C","marks":90})
##print(d)
##
##with open("students.json","w") as f:
##    json.dump(d,f)
##print()
##
##
##
##
##print("----------------------TASK 8----------------------")
##
##def check_email(e):
##    if "@" in e and (e.endswith(".com") or e.endswith(".in")):
##        return True
##    else:
##        return False
##
##print(check_email(input("Enter email: ")))
##print()
##
##
##
##
##print("----------------------TASK 9----------------------")
##import random
##
##n=random.randint(1,100)
##att=5
##
##while att>0:
##    guess=int(input("Enter guess: "))
##    
##    if guess>n:
##        print("Too high")
##    elif guess<n:
##        print("Too low")
##    else:
##        print("Correct guess")
##        break 
##    att-=1
##
##if att==0:
##    print("Game Over. Number was:",n)
##print()
##
##
##
##
##print("----------------------TASK 10----------------------")
##start=int(input("Enter start: "))
##end=int(input("Enter end: "))
##
##prime=[]
##
##for n in range(start,end+1):
##    if n>1:
##        for i in range(2,n):
##            if n%i==0:
##                break
##        else:
##            prime.append(n)
##
##print(prime)
##print("count :",len(prime))
##print("largest :",max(prime))
##print()
##
##
##
##
##print("----------------------TASK 11----------------------")
##con={}
##
##while True:
##    print("1.Add 2.Search 3.Delete 4.Display 5.Exit")
##    c=int(input("Enter choice: "))
##    
##    if c==1:
##        name=input("Enter name: ")
##        n=input("Enter number: ")
##        con[name]=n
##        print("Contact added")
##    
##    elif c==2:
##        name=input("Enter name: ")
##        if name in con:
##            print(con[name])
##        else:
##            print("Not found")
##    
##    elif c==3:
##        name=input("Enter name: ")
##        if name in con:
##            con.pop(name)
##            print("deleted")
##        else:
##            print("not found")
##    
##    elif c==4:
##        print(con)
##    
##    else:
##        break
##print()
##
##
##
##
##print("----------------------TASK 13----------------------")
##import threading
##
##def num():
##    for i in range(1,6):
##        print(i)
##
##def alph():
##    for ch in "ABCDE":
##        print(ch)
##
##t1=threading.Thread(target=num)
##t2=threading.Thread(target=alph)
##
##t1.start()
##t2.start()
##
##t1.join()
##t2.join()
##print()
##
##
##
##
##print("----------------------TASK 12----------------------")
##import cv2
##
##img=cv2.imread("image.jpg")
##
##gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##edge=cv2.Canny(img,100,200)
##re=cv2.resize(img,(300,300))
##
##cv2.imshow("Original",img)
##cv2.imshow("Gray",gray)
##cv2.imshow("Edges",edge)
##cv2.imshow("Resized",re)
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##
##
##
##
##print("----------------------TASK 14----------------------")
##import pandas as pd
##from sklearn.model_selection import train_test_split
##from sklearn.tree import DecisionTreeClassifier
##import joblib
##import tkinter as tk
##
##df=pd.read_csv("iris.csv")
##
##x=df.drop(columns=["Id","Species"])
##y=df["Species"]
##
##x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
##
##model=DecisionTreeClassifier()
##model.fit(x_train,y_train)
##
##joblib.dump(model,"model.pkl")
##print("Model trained and saved")
##
##def predict():
##    vals=[float(e1.get()),
##          float(e2.get()),
##          float(e3.get()),
##          float(e4.get())
##          ]
##    res=model.predict([vals])
##    result.config(text=res)
##
##root=tk.Tk()
##root.title("Prediction App")
##root.geometry("300x350")
##
##heading=tk.Label(root,text="Iris Prediction",font=("Arial",14))
##heading.pack(pady=10)
##
##tk.Label(root,text="Sepal length").pack()
##e1=tk.Entry(root)
##e1.pack(pady=5)
##
##tk.Label(root,text="Sepal width").pack()
##e2=tk.Entry(root)
##e2.pack(pady=5)
##
##tk.Label(root,text="Petal length").pack()
##e3=tk.Entry(root)
##e3.pack(pady=5)
##
##tk.Label(root,text="Petal width").pack()
##e4=tk.Entry(root)
##e4.pack(pady=5)
##
##tk.Button(root,text="Predict",command=predict).pack(pady=10)
##
##result=tk.Label(root,text="")
##result.pack(pady=10)
##
##root.mainloop()
##
##print()
##
##
##
##
##print("----------------------TASK 15----------------------")
##
##import librosa as lb
##import matplotlib.pyplot as plt
##import librosa.display
##
##y,sr=lb.load("C:\\Users\\Hp\\Desktop\\Internship Program\\task\\game_over.wav",sr=None)
##
##print("Sampling Rate:",sr)
##
##plt.figure(figsize=(10,4))
##lb.display.waveshow(y,sr=sr)
##
##plt.title("Waveform")
##plt.xlabel("Time")
##plt.ylabel("Amplitude")
##
##plt.show()





##print("----------------------TASK 16----------------------")
##
##import cv2
##import numpy as np
##
##img=cv2.imread("image.jpg")
##
##gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##print("Grayscale applied")
##
##blur=cv2.GaussianBlur(img,(7,7),0)
##print("Blur applied")
##
##kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
##sharp=cv2.filter2D(img,-1,kernel)
##print("Sharpen applied")
##
##cv2.imshow("Original",img)
##cv2.imshow("Gray",gray)
##cv2.imshow("Blur",blur)
##cv2.imshow("Sharpen",sharp)
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()




print("----------------------TASK 17----------------------")
class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def increase_salary(self,amt):
        self.salary+=amt
        print("Salary increased")

    def display(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Salary:",self.salary)

    def annual_salary(self):
        print("Annual Salary:",self.salary*12)

e=Employee("Prajwal",101,20000)

e.display()
e.increase_salary(5000)
e.display()
e.annual_salary()
print()




print("----------------------TASK 18----------------------")
class Vehicle:
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate
        self.available=True

    def rent(self,days):
        if self.available:
            self.available=False
            cost=self.rate*days
            print(self.name,"rented for",days,"days")
            print("Rent:",cost)
            print()
        else:
            print(self.name,"not available")
            print()

    def return_vehicle(self):
        self.available=True
        print(self.name,"returned")
        print()

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c=Car("Car",1000)
b=Bike("Bike",500)

c.rent(2)
c.return_vehicle()

b.rent(3)
b.return_vehicle()
print()





print("----------------------TASK 19----------------------")
class Patient:
    def __init__(self,name):
        self.name=name
        self.history=[]

class Doctor:
    def __init__(self,name):
        self.name=name

class Appointment:
    def __init__(self,patient,doctor):
        self.patient=patient
        self.doctor=doctor

p=Patient("Prajwal")
d=Doctor("Dr.Sudeep")

a=Appointment(p,d)

print("Appointment booked for",p.name,"with",d.name)

p.history.append("Fever")
p.history.append("Checkup")

print("Patient History:",p.history)
print()




print("----------------------TASK 20----------------------")

class Menu:
    def __init__(self):
        self.items={"Burger":100,"Pizza":200,"Juice":50}

class Customer:
    def __init__(self,name):
        self.name=name

class Order:
    def __init__(self):
        self.total=0

    def add_item(self,item,price):
        self.total+=price
        print(item,"added")

    def bill(self):
        print("Total Bill:",self.total)

m=Menu()
c=Customer("Prajwal")
o=Order()

o.add_item("Burger",m.items["Burger"])
o.add_item("Juice",m.items["Juice"])
o.bill()

print("Order status: Confirmed")
print()
