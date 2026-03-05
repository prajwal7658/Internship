###TASK 1:
##s= "DataScienceWithPython"
##print("-------------------TASK 1:--------------------")
##print(s[0:4])
##
##print(s[-6:])
##
##print(s[::-1])
##
##print(s[::2])
##
##print(s.lower())
##
##v="aeiouAEIOU"
##count=0
##for i in s:
##    if i in v:
##        count+=1
##print("Number of vowels:", count)
##print()
##
###TASK 2:
##print("-------------------TASK 2:--------------------")
##n=[10,20,30,40,50,20,10]
##
##n.append(60)
##
##n.insert(1,15)
##
##n=list(set(n))
##
##n.sort(reverse=True)
##
##print("Frequency of 20 :",n.count(20))
##
##t=tuple(n)
##print(n)
##print(t)
##print()
##
###TASK 3:
##t=(5,10,15,20,25,10)
##print("-------------------TASK 3:--------------------")
##print(t[3])
##
##l=list(t)
##l.append(30)
##
##print(t[1:5])
##print()
##
###TASK 4:
##print("-------------------TASK 4:--------------------")
##s={
##    "name":"Prajwal",
##    "age":21,
##    "marks":85
##}
##print("##TASK 4:")
##s["grade"]="A"
##
##s["marks"]=90
##
##del s["age"]
##
##print(s.keys())
##
##print(s.values())
##
##if "name" in s:
##    print("Name is present")
##else:
##    print("Name is not present")
##print()
##
###TASK 5:
##print("-------------------TASK 5:--------------------")
##A={1,2,3,4}
##B={3,4,5,6}
##
##print(A|B)
##
##print(A&B)
##
##print(A-B)
##
##print(A^B)
##
##A.add(10)
##
##A.remove(2)
##
##print(A)
##print()
##
###TASK 6:
##print("-------------------TASK 6:--------------------")
###Prime number
##def Prime(n):
##    if n<=1:
##        return False
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    return True
##print("The number is prime :",Prime(10))
##print()
##
###Factorial
##def fact(n):
##    if n == 1:
##        return 1
##    return n*fact(n-1)
##print("factorial is :",fact(10))
##print()
##
###Fibonacci
##def fib(n):
##    if n==0:
##        return 0
##    if n==1:
##        return 1
##    return fib(n-1)+fib(n-2)
##
##for i in range(10):
##    print(fib(i),end=" ")
##print()
##
###default argument
##def greet(name="Prajwal"):
##    print("Hello", name)
##
##print(greet())
##print()
##
###Lambda function
##s=lambda x:x*x
##print("Square root is :",s(5))
##print()
##
###TASK 7:
##print("-------------------TASK 7:--------------------")
###table
##n=int(input("Enter a number: "))
##for i in range(1, 11):
##    print(n ,"x",i ,"= ",n*i)
##print()
##
###Pattern
##for i in range(1,6):
##    print("*" * i)
##print()
##
###Sum of digits
##n=int(input("Enter a number: "))
##total=0
##for x in str(n):
##    total+=int(x)
##print("Sum of digits:", total)
##print()
##
###Count even and odd numbers in list
##n=[10,15,20,25,30,35]
##even=0
##odd=0
##
##for n in n:
##    if n%2==0:
##        even+=1
##    else:
##        odd+=1
##
##print("Even numbers:", even)
##print("Odd numbers:", odd)
##print()
##
###first 10 prime numbers
##count=0
##n=2
##while count<10:
##    prime=True
##    for i in range(2,n):
##        if n%i==0:
##            prime=False
##            break
##    if prime:
##        print(n,end=" ")
##        print()
##        count+=1
##    n+=1
##print()
##
##
###TASK 8:
##print("-------------------TASK 8:--------------------")
###1
##class Student:  
##    def __init__(self,name,age,marks):
##        self.name=name         
##        self.age=age
##        self.marks=marks      
##
##    def display(self):
##        print("Name :",self.name)
##        print("Age :",self.age)
##        print("Marks :",self.marks)
##s1=Student("Prajwal",22,94)
##s1.display()
##print()
##
###2
##class Rectangle:
##    def __init__(self,length,width):
##        self.length=length
##        self.width=width
##
##    def area(self):
##        return self.length*self.width
##
##    def perimeter(self):
##        return 2*(self.length+self.width)
##a=Rectangle(2,4)
##a.area()
##a.perimeter()
##print()
##
###3
##class Student:
##    school="Sahyadri" 
##
##    def __init__(self,name,age): 
##        self.name=name         
##        self.age=age
##    def display(self):
##        print("School: ",Student.school)
##        print("Name: ",self.name)
##        print("Age: ",self.age)
##s1=Student("Prajwal",20)
##s1.display()
##print()
##
###4
###INHERITENCE
##class Animal:
##    def sound(self):
##        print("Animal makes sound")
##
##class Dog(Animal):
##    def bark(self):
##        print("Dog barks")
##
##t=Dog()
##t.sound()
##t.bark()
##print()
##
###METHOD OVERRIDING
##class Person:
##    def speak(self):
##        print("Person speaking")
##
##class Teacher(Person):
##    def speak(self):
##        print("Teacher speaking")
##
##t=Teacher()
##t.speak()
##print()
##
###ENCAPSULATION
##class Student:
##    def __init__(self,marks):
##        self.__marks=marks   
##
##    def show_marks(self):
##        print("Marks :",self.__marks)
##
##s=Student(90)
##s.show_marks()
##print()
##
###POLYMORPHISM
##class Dog:
##    def sound(self):
##        print("Bark")
##
##class Cat:
##    def sound(self):
##        print("Meow")
##
##def make_sound(animal):
##    animal.sound()
##
##d=Dog()
##c=Cat()
##
##make_sound(d)
##make_sound(c)
##print()
##
###TASK 9:
##print("-------------------TASK 9:--------------------")
##import numpy as np
##
##a=np.arange(1,11)
##print("1d Array: ",a)
##
##zero=np.zeros((3,3))
##print("\nZero matrix:\n",zero)
##
##identity=np.eye(3)
##print("\nIdentity matrix:\n",identity)
##
##rand=np.random.randint(1,101,5)
##print("\nRandom numbers:", rand)
##
##reshape=a.reshape(2,5)
##print("\nReshaped:\n", reshape)
##
##sorted_des= np.sort(a)[::-1]
##print("\nSorted in descending order:", sorted_des)
##print()
##
##
###TASK 10:
##print("-------------------TASK 10:--------------------")
##import pandas as pd
##
##data={
##    "Name": ["Prajwal","Pradeep","Ram","Sham"],
##    "Marks": [80,90,None,90],
##    "Age": [20,21,22,21]
##}
##
##df=pd.DataFrame(data)
##print("DataFrame:\n", df)
##print()
##
##df_csv=pd.read_csv("data.csv")
##print("\nFirst 5 rows:\n", df.head())
##print()
##
##print("\nSummary statistics:\n", df.describe())
##print()
##
##df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
##df["Marks"] = df["Marks"].fillna(df["Marks"].median())
##
##print("\nAfter handling missing values:\n", df)
##print()
##
##df.drop_duplicates(inplace=True)
##print("\nAfter Removing Duplicates:\n",df)
##print()
##
##df.rename(columns={"Marks": "Score"},inplace=True)
##print("\nAfter renaming column:\n",df)
##print()
##
##df.to_csv("cleaned_data.csv",index=False)
##print("\nCleaned data exported successfully.")
##print()



###TASK 11:
##import matplotlib.pyplot as plt
##x=[1,2,3,4,5]
##y=[10,20,25,30,40]
##
###1.Line Plot
##plt.figure()
##plt.plot(x,y)
##plt.title("Line Plot")
##plt.xlabel("X values")
##plt.ylabel("Y values")
##plt.show()
##
###2.Bar Chart
##plt.figure()
##plt.bar(x,y)
##plt.title("Bar chart")
##plt.xlabel("X values")
##plt.ylabel("Y values")
##plt.show()
##
###3.Pie Chart
##plt.figure()
##plt.pie(y,labels=x)
##plt.title("Pie chart")
##plt.show()
##
###4.Histogram
##plt.figure()
##plt.hist(y)
##plt.title("Histogram")
##plt.xlabel("Values")
##plt.ylabel("Frequency")
##plt.show()
##
###5.Scatter Plot
##plt.figure()
##plt.scatter(x,y)
##plt.title("Scatter plot")
##plt.xlabel("X values")
##plt.ylabel("Y values")
##plt.show()
##
###6.Subplot 
##plt.figure()
##
##plt.subplot(2,1,1)
##plt.plot(x,y)
##plt.title("Line plot")
##
##plt.subplot(2,1,2)
##plt.bar(x,y)
##plt.title("Bar chart")
##
##plt.tight_layout()
##plt.show()



###TASK 12:
from PIL import Image, ImageFilter
i=Image.open("image.jpg")
##
##i.show()
##
###Resize
##resized=i.resize((300,300))
##resized.show()
##
###grayscale
##gray=i.convert("L")
##gray.show()

#Rotate
rotated=i.rotate(45)
rotated.show()

#Crop
cropped=i.crop((50,50,200,200))
cropped.show()

#blur filter
blurred = i.filter(ImageFilter.BLUR)
blurred.show()
##
###Save
##blurred.save("modified_image.jpg")
##
###Convert
##i.save("converted_image.png")























