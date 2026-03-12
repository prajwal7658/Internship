####TASK 1:
##import numpy as np
##print("-------------------TASK 1--------------------")
###Create array 
##a=np.arange(1,11)
##print("Array:",a)
##print()
##
###Mean, median and standard Deviation
##print("Mean:",np.mean(a))
##print("Median:",np.median(a))
##print("Standard Deviation:",np.std(a))
##print()
##
###Generate 10 random numbers
##r=np.random.rand(10)
##print("Random Numbers:",r)
##print()
##
###Reshape
##b=np.arange(1,7)
##c=b.reshape(2,3)
##print(c)
##print()
##
###Max and min
##print("Maximum:",np.max(a))
##print("Minimum:",np.min(a))
##print()
##
###Zeros and ones
##z=np.zeros(5)
##o=np.ones(5)
##print("Zeros:",z)
##print("Ones:",o)
##print()
##
##
##
####TASK 2:
##import pandas as pd
##print("-------------------TASK 2--------------------")
##
###dataframe with student names and marks
##data={
##    "Name":["Prajwal","Pradeep","Sushan","Rahul"],
##    "Marks":[85,72,90,65]
##}
##df=pd.DataFrame(data)
##print(df)
##print()
##
##
###Add new column 
##df["Grade"]=["A","B","A","C"]
##print(df)
##print()
##
##
###Sort based on marks
##sorted_df=df.sort_values("Marks")
##print(sorted_df)
##print()
##
##
###Read CSV file and display first 25 rows
##d=pd.read_csv("data.csv")
##print(d.head(25))
##print()
##
##
###Remove missing values
##clean=d.dropna()
##print(clean)
##print()
##
##
###Replace missing values using median
##num=d.select_dtypes(include=['number'])
##d[num.columns]=num.fillna(num.median())
##print(d)
##print()



####TASK 3:
##import matplotlib.pyplot as plt
##print("-------------------TASK 3--------------------")
##
###Line graph
##months=["Jan","Feb","Mar","Apr","May"]
##sales=[100,150,200,180,220]
##
##plt.plot(months,sales)
##plt.title("Monthly Sales")
##plt.xlabel("Months")
##plt.ylabel("Sales")
##plt.show()
##
###Bar chart
##students=["A","B","C","D"]
##marks=[80,65,90,75]
##
##plt.bar(students,marks)
##plt.title("Student Marks")
##plt.xlabel("Students")
##plt.ylabel("Marks")
##plt.show()
##
###Scatter plot 
##height=[150,160,170,180]
##weight=[50,60,65,75]
##
##plt.scatter(height,weight)
##plt.title("Height vs Weight")
##plt.xlabel("Height")
##plt.ylabel("Weight")
##plt.show()
##
###Histogram 
##print("\nPART 4")
##age=[18,19,20,21,22,20,19,23,21]
##
##plt.hist(age,bins=5)
##plt.title("Age Distribution")
##plt.xlabel("Age")
##plt.ylabel("Frequency")
##plt.show()
##
###Add title, labels and legend
##x=[1,2,3,4]
##y=[10,20,25,30]
##
##plt.plot(x,y,label="Sales")
##plt.title("Simple Graph")
##plt.xlabel("X axis")
##plt.ylabel("Y axis")
##plt.legend()
##plt.show()
##
###Multiple lines on same graph
##y1=[10,20,30]
##y2=[30,20,10]
##
##plt.plot(y1,label="Line 1")
##plt.plot(y2,label="Line 2")
##plt.legend()
##plt.show()
##
###Customize 
##plt.plot([1,2,3],[5,15,25],color="red",marker="o")
##plt.grid(True)
##plt.title("Customized plot")
##plt.show()



####TASK 4:
##import tkinter as tk
##from tkinter import messagebox
##print("-------------------TASK 4--------------------")
##root=tk.Tk()
##root.title("Tkinter Tasks")
##root.geometry("400x400")
##
##label=tk.Label(root,text="Hello from Tkinter")
##label.pack()
##
##def message():
##    messagebox.showinfo("Message","Button clicked!")
##
##button=tk.Button(root,text="Click Me",command=message)
##button.pack()
##textbox=tk.Entry(root)
##textbox.pack()
##
##
##def show_text():
##    messagebox.showinfo("User Input",textbox.get())
##
##
##button2=tk.Button(root,text="Show Input",command=show_text)
##button2.pack()
##
##username=tk.Entry(root)
##username.insert(0,"Username")
##username.pack()
##
##password=tk.Entry(root)
##password.insert(0,"Password")
##password.pack()
##
##def login():
##    if username.get()=="admin" and password.get()=="123":
##        messagebox.showinfo("Login","Login Successful")
##    else:
##        messagebox.showinfo("Login","Invalid Login")
##
##login_btn=tk.Button(root,text="Login",command=login)
##login_btn.pack()
##
##n1=tk.Entry(root)
##n1.pack()
##
##n2=tk.Entry(root)
##n2.pack()
##
##def add():
##    result=int(n1.get())+int(n2.get())
##    messagebox.showinfo("Result",result)
##
##def sub():
##    result=int(n1.get())-int(n2.get())
##    messagebox.showinfo("Result",result)
##
##def mul():
##    result=int(n1.get())*int(n2.get())
##    messagebox.showinfo("Result",result)
##
##def div():
##    result=int(n1.get())/int(n2.get())
##    messagebox.showinfo("Result",result)
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Sub",command=sub).pack()
##tk.Button(root,text="Mul",command=mul).pack()
##tk.Button(root,text="Div",command=div).pack()
##root.mainloop()



####TASK 5:
##import sys
##from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
##print("-------------------TASK 5--------------------")
##app=QApplication(sys.argv)
##
##window=QWidget()
##window.setWindowTitle("PyQt")
##window.resize(300,300)
##
##label=QLabel("Enter name")
##username=QLineEdit()
##
##password=QLineEdit()
##password.setPlaceholderText("Enter password")
##
##result=QLabel("")
##
##def login():
##    user=username.text()
##    pwd=password.text()
##    if user=="admin" and pwd=="123":
##        result.setText("Login successful")
##    else:
##        result.setText("Invalid login")
##
##button=QPushButton("Login")
##button.clicked.connect(login)
##
##layout=QVBoxLayout()
##layout.addWidget(label)
##layout.addWidget(username)
##layout.addWidget(password)
##layout.addWidget(button)
##layout.addWidget(result)
##
##window.setLayout(layout)
##
##window.show()
##sys.exit(app.exec_())



##TASK 6:
#Word tokenization
print("-------------------TASK 6--------------------")
import nltk
from nltk.tokenize import word_tokenize

text="The boys are playing happily in the playground."

words=word_tokenize(text)
print("Word Tokens:",words)
print()


#Sentence tokenization
from nltk.tokenize import sent_tokenize
sentences=sent_tokenize(text)
print("Sentence Tokens:",sentences)
print()


#Remove stopwords
from nltk.corpus import stopwords

stop_words=set(stopwords.words('english'))
filtered=[]

for w in words:
    if w.lower() not in stop_words:
        filtered.append(w)
print("Filtered Words:",filtered)
print()


#Stemming
from nltk.stem import PorterStemmer
ps=PorterStemmer()

for w in words:
    print(w,"->",ps.stem(w))
print()


#Lemmatization
from nltk.stem import WordNetLemmatizer

l=WordNetLemmatizer()
for w in words:
    print(w,"->",l.lemmatize(w))
print()


#POS Tagging
from nltk import pos_tag
pos=pos_tag(words)
print("POS Tags:",pos)
print()
























