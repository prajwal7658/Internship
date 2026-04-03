##print("--------------------------TASK 1----------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##food=[]
##cal=[]
##n=int(input("No of food items:  "))
##
##for i in range(n):
##    item=input("Enter food item: ")
##    c=int(input("Enter calories: "))
##    
##    food.append(item)
##    cal.append(c)
##
##df=pd.DataFrame({
##    "Food": food,
##    "Calories": cal
##})
##
##print(df)
##
##total=np.sum(df["Calories"])
##print("\nTotal Calories:",total)
##
##plt.pie(df["Calories"],labels=df["Food"],autopct="%1.1f%%")
##plt.title("Calorie distribution")
##plt.show()
##
##
##
##
##print("--------------------------TASK 2----------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##product=[]
##qty=[]
##
##n=int(input("No of products:"))
##
##for i in range(n):
##    p=input("Enter product name: ")
##    q=int(input("Enter quantity: "))
##    
##    product.append(p)
##    qty.append(q)
##
##df=pd.DataFrame({
##    "Product": product,
##    "Quantity": qty
##})
##
##print(df)
##
##total=np.sum(df["Quantity"])
##print("Total stock:",total)
##
##plt.bar(df["Product"],df["Quantity"])
##plt.title("Stock Levels")
##plt.xlabel("Products")
##plt.ylabel("Quantity")
##plt.show()
##
##
##
##
##print("--------------------------TASK 3----------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##player=[]
##score=[]
##
##n=int(input("No of players:  "))
##
##for i in range(n):
##    p=input("Enter player name: ")
##    s=int(input("Enter score: "))
##    
##    player.append(p)
##    score.append(s)
##
##df=pd.DataFrame({
##    "Player": player,
##    "Score": score
##})
##
##print(df)
##
##highest=np.max(df["Score"])
##print("Highest score:",highest)
##
##plt.bar(df["Player"],df["Score"])
##plt.title("Player score comparison")
##plt.xlabel("Players")
##plt.ylabel("Scores")
##plt.show()
##
##
##
##
##print("--------------------------TASK 4----------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##hour=[]
##count=[]
##
##n=int(input("No of entries:  "))
##
##for i in range(n):
##    h=input("Enter hour: ")
##    c=int(input("Enter vehicle count: "))
##    
##    hour.append(h)
##    count.append(c)
##
##df=pd.DataFrame({
##    "Hour": hour,
##    "Count": count
##})
##
##print(df)
##
##peak=np.max(df["Count"])
##print("Peak Traffic Count:",peak)
##
##plt.plot(df["Hour"],df["Count"],marker='o')
##plt.title("Traffic analysis")
##plt.xlabel("Hour")
##plt.ylabel("Vehicle count")
##plt.grid()
##plt.show()



##print("--------------------------TASK 5----------------------------")
##TP=50, FN=10, FP=5, TN=35
##Total=50+10+5+35=100
##
##Accuracy=(TP+TN)/Total
##Precision=TP/(TP+FP)
##Recall=TP/(TP+FN)
##F1 Score=2×(Precision×Recall)/(Precision+Recall)
##
##
##Accuracy=(50+35)/100 = 85/100=0.85
##
##Precision=50/(50+5) = 50/55=0.91
##
##Recall=50/(50+10) = 50/60=0.83
##
##F1 Score=2×(0.91×0.83)/(0.91+0.83) =2×0.7553/1.74 =1.5106/1.74=0.87
##
##
##
##
##
##print("--------------------------TASK 6----------------------------")
##
##Accuracy=(TP+TN)/Total
##Precision=TP/(TP+FP)
##Recall=TP/(TP+FN)
##f1 score=2*TP/(2*TP+FP+FN)
##
##
###A
##TP=40, FN=10, FP=15, TN=85, Total=150
##
##Accuracy=(40+85)/150 = 125/150 = 0.83
##Precision=40/(40+15) = 40/55 = 0.73
##Recall=40/(40+10) = 40/50 = 0.80
##
##f1 score=2*40/(2*40+15+10) =80/105 =0.76
##
##
###B
##TP=30, FN=20, FP=10, TN=90, Total=150
##
##Accuracy=(30+90)/150 = 120/150 = 0.80
##Precision=30/(30+10) = 30/40 = 0.75
##Recall=30/(30+20) = 30/50 = 0.60
##
##f1 score=2*30/(2*30+10+20) =60/90 =0.67
##
##
### C
##TP=40, FN=10, FP=15, TN=85, Total=150
##
##Accuracy=(40+85)/150 = 125/150 = 0.83
##Precision=40/(40+15) = 40/55 = 0.73
##Recall=40/(40+10) = 40/50 = 0.80
##
##f1 score=2*40/(2*40+15+10) =80/105 =0.76
##
##
##
##
##print("--------------------------TASK 7----------------------------")
##
##TP=45, FN=5, FP=15, TN=35
##
##Total=45+5+15+35=100
##
##Accuracy=(45+35)/100 = 80/100 = 0.80
##Precision=45/(45+15) = 45/60 = 0.75
##Recall=45/(45+5) = 45/50 = 0.90
##
##F1_Score=2*45/(2*45+15+5) =90/110 =0.82




##print("--------------------------TASK 8----------------------------")
##import numpy as np
##
##arr1=np.arange(1,11)
##print(arr1)
##print()
##
##arr2=np.array([10,20,30,40,50])
##print("Mean:",np.mean(arr2))
##print("Median:",np.median(arr2))
##print("Standard Deviation:",np.std(arr2))
##print()
##
##arr3=np.random.rand(10)
##print("Random numbers:",arr3)
##print()
##
##arr4=np.arange(1,7)
##reshaped=arr4.reshape(2,3)
##print("Reshaped: ",reshaped)
##print()
##
##arr5=np.array([5,10,15,20,25])
##print("Max:",np.max(arr5))
##print("Min:",np.min(arr5))
##print()
##
##z=np.zeros(5)
##o=np.ones(5)
##print("Zeros:",z)
##print("Ones:",o)
##print()
##
##
##
##
##print("--------------------------TASK 9----------------------------")
##import pandas as pd
##import numpy as np
##
##df=pd.DataFrame({
##    "Name":["A","B","C","D"],
##    "Marks":[80,70,90,60]
##})
##print(df)
##print()
##
##df["Grade"]=["B","C","A","D"]
##print(df)
##print()
##
##sorted=df.sort_values(by="Marks")
##print(sorted)
##print()
##
##df2=pd.read_csv("iris.csv")
##print(df2.head(25))
##
##df3=pd.DataFrame({
##    "A":[1,2,np.nan,4],
##    "B":[5,np.nan,7,8]
##})
##print(df3.dropna())
##print()
##
##df4=pd.DataFrame({
##    "A":[1,2,np.nan,4,5]
##})
##
##median=df4["A"].median()
##df4["A"]=df4["A"].fillna(median)
##print(df4)
##print()
##
##
##
##
##print("--------------------------TASK 10----------------------------")
##import matplotlib.pyplot as plt
##import numpy as np
##
### Line graph
##months=["May","Jun","Jul","Aug"]
##sales=[120,180,160,220]
##
##plt.plot(months,sales)
##plt.title("Monthly sales")
##plt.xlabel("Months")
##plt.ylabel("Sales")
##plt.show()
##
##
### Bar chart
##students=["P","Q","R","S"]
##marks=[75,85,65,95]
##
##plt.bar(students,marks)
##plt.title("Student marks")
##plt.xlabel("Students")
##plt.ylabel("Marks")
##plt.show()
##
##
### Scatter plot
##height=[155,165,175,185]
##weight=[52,62,72,82]
##
##plt.scatter(height,weight)
##plt.title("Height vs Weight")
##plt.xlabel("Height")
##plt.ylabel("Weight")
##plt.show()
##
##
### Histogram
##ages=[19,21,23,21,20,22,24,23]
##
##plt.hist(ages)
##plt.title("Age distibution")
##plt.show()
##
##
### Title, Labels, Legend
##x=[2,4,6,8]
##y=[15,25,35,45]
##
##plt.plot(x,y,label="Line1")
##plt.title("Example graph")
##plt.xlabel("X")
##plt.ylabel("Y")
##plt.legend()
##plt.show()
##
##
### Multiple lines
##y1=[12,22,32]
##y2=[18,28,38]
##
##plt.plot(x[:3],y1,label="One")
##plt.plot(x[:3],y2,label="Two")
##plt.legend()
##plt.show()
##
##
### Customize
##plt.plot(x,y,color="green",marker="s")
##plt.grid()
##plt.show()




##print("--------------------------TASK 11----------------------------")
##import tkinter as tk
##from tkinter import messagebox
##
###1
##root=tk.Tk()
##root.title("Tkinter")
##root.geometry("400x500")
##
##
### 2
##l=tk.Label(root,text="Welcome",font=("Arial",14))
##l.pack(pady=5)
##
##def click():
##    messagebox.showinfo("Message","Button clicked")
##
##b=tk.Button(root,text="Click",command=click)
##b.pack(pady=5)
##
##
### 3
##e1=tk.Entry(root)
##e2=tk.Entry(root)
##e1.pack(pady=2)
##e2.pack(pady=2)
##
##def add():
##    print("Add:",int(e1.get())+int(e2.get()))
##def sub():
##    print("Sub:",int(e1.get())-int(e2.get()))
##def mul():
##    print("Mul:",int(e1.get())*int(e2.get()))
##def div():
##    print("Div:",int(e1.get())/int(e2.get()))
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Sub",command=sub).pack()
##tk.Button(root,text="Mul",command=mul).pack()
##tk.Button(root,text="Div",command=div).pack()
##
##
### 4
##tk.Label(root,text="Username").pack()
##user=tk.Entry(root)
##user.pack()
##
##tk.Label(root,text="Password").pack()
##pwd=tk.Entry(root,show="*")
##pwd.pack()
##
##
### 5
##def login():
##    messagebox.showinfo("Login","Login success")
##
##tk.Button(root,text="Login",command=login).pack(pady=5)
##
##
### 6
##txt=tk.Text(root,height=3,width=25)
##txt.pack(pady=5)
##
##
### 7
##def show():
##    print(txt.get("1.0",tk.END))
##
##tk.Button(root,text="Show text",command=show).pack(pady=5)
##
##
### 8
##menu=tk.Menu(root)
##root.config(menu=menu)
##
##file=tk.Menu(menu)
##menu.add_cascade(label="File",menu=file)
##file.add_command(label="Exit",command=root.quit)
##
##root.mainloop()




##print("# ---------------------- TASK 12 ----------------------")
###1
##import sys
##from PyQt5.QtWidgets import QApplication, QWidget
##
##app=QApplication(sys.argv)
##
##window=QWidget()
##window.setWindowTitle("Basic window")
##window.resize(300,200)
##
##window.show()
##app.exec_()
##
##
##
###2
##from PyQt5.QtWidgets import QLabel, QPushButton
##
##window=QWidget()
##window.resize(300,200)
##
##label=QLabel("Welcome",window)
##label.move(100,50)
##
##button=QPushButton("Click",window)
##button.move(100,80)
##
##window.show()
##app.exec_()
##
##
##
###3
##from PyQt5.QtWidgets import QLineEdit, QVBoxLayout
##
##window=QWidget()
##
##e1=QLineEdit()
##e2=QLineEdit()
##
##b1=QPushButton("Add")
##b2=QPushButton("Sub")
##b3=QPushButton("Mul")
##b4=QPushButton("Div")
##
##result=QLabel("")
##
##def add():
##    result.setText(str(int(e1.text())+int(e2.text())))
##
##def sub():
##    result.setText(str(int(e1.text())-int(e2.text())))
##
##def mul():
##    result.setText(str(int(e1.text())*int(e2.text())))
##
##def div():
##    result.setText(str(int(e1.text())/int(e2.text())))
##
##layout=QVBoxLayout()
##layout.addWidget(e1)
##layout.addWidget(e2)
##layout.addWidget(b1)
##layout.addWidget(b2)
##layout.addWidget(b3)
##layout.addWidget(b4)
##layout.addWidget(result)
##
##window.setLayout(layout)
##
##b1.clicked.connect(add)
##b2.clicked.connect(sub)
##b3.clicked.connect(mul)
##b4.clicked.connect(div)
##
##window.show()
##app.exec_()
##
##
###4
##window=QWidget()
##
##user=QLineEdit()
##user.setPlaceholderText("Username")
##
##pwd=QLineEdit()
##pwd.setPlaceholderText("Password")
##
##btn=QPushButton("Login")
##res=QLabel("")
##
##def login():
##    if user.text()=="admin" and pwd.text()=="123":
##        res.setText("Login success")
##    else:
##        res.setText("Invalid")
##
##layout=QVBoxLayout()
##layout.addWidget(user)
##layout.addWidget(pwd)
##layout.addWidget(btn)
##layout.addWidget(res)
##
##window.setLayout(layout)
##
##btn.clicked.connect(login)
##
##window.show()
##app.exec_()
##
##
###5
##window=QWidget()
##
##btn=QPushButton("Click",window)
##btn.move(100,50)
##
##label=QLabel("",window)
##label.move(100,80)
##
##def show():
##    label.setText("Button clicked")
##
##btn.clicked.connect(show)
##
##window.show()
##app.exec_()
##
##
###6
##from PyQt5.QtWidgets import QTextEdit
##window=QWidget()
##
##text=QTextEdit(window)
##text.resize(200,100)
##
##window.show()
##app.exec_()
##
##
##
###7
##window=QWidget()
##
##text=QTextEdit()
##btn=QPushButton("Show text")
##
##def show_text():
##    print(text.toPlainText())
##
##layout=QVBoxLayout()
##layout.addWidget(text)
##layout.addWidget(btn)
##
##window.setLayout(layout)
##
##btn.clicked.connect(show_text)
##
##window.show()
##app.exec_()
##
##
###8
##from PyQt5.QtWidgets import QMenuBar
##window=QWidget()
##
##menu=QMenuBar()
##file=menu.addMenu("File")
##file.addAction("Exit",window.close)
##
##layout=QVBoxLayout()
##layout.setMenuBar(menu)
##
##window.setLayout(layout)
##
##window.show()
##app.exec_()




print("--------------------------TASK 13----------------------------")

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sentence tokenization
from nltk.tokenize import sent_tokenize

text="Online learning is growing fast. Students prefer flexible education."

sent=sent_tokenize(text)

print("Sentence tokens:")
print(sent)


# Word tokenization
from nltk.tokenize import word_tokenize

w1=word_tokenize(text)

print("Word tokens:")
print(w1)


# Stopwords remove
from nltk.corpus import stopwords

sw=set(stopwords.words('english'))

filt=[]

for w in w1:
    if w.lower() not in sw:
        filt.append(w)

print("Filtered words:")
print(filt)


# Stemming
from nltk.stem import PorterStemmer

ps=PorterStemmer()

w2=["running","studies","playing","learning"]

for w in w2:
    print(w,"->",ps.stem(w))


# Lemmatization
from nltk.stem import WordNetLemmatizer

lm=WordNetLemmatizer()

w3=["running","better","studies"]

for w in w3:
    print(w,"->",lm.lemmatize(w))


# POS tagging
from nltk import pos_tag

sentence="Students are learning new skills"

w4=word_tokenize(sentence)

pos=pos_tag(w4)

print(pos)
