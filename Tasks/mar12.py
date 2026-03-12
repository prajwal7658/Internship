#-----------------------TASK 1-------------------------
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyse_marks():
    Name=name.get()
    Python=int(python.get())
    Java=int(java.get())
    C=int(c.get())
    SQL=int(sql.get())

    data={
        "Subject":["Python","Java","C","SQL"],
        "Marks":[Python,Java,C,SQL]
        }
    df=pd.DataFrame(data)

    total=np.sum(df["Marks"])
    average=np.mean(df["Marks"])
    highest=np.max(df["Marks"])
    lowest=np.min(df["Marks"])

    result.config(text=f"Total Marks: {total}\n Average Marks: {average}\n Highest Marks: {highest}\n Lowest Marks: {lowest}\n")

    plt.bar(df["Subject"],df["Marks"])
    plt.title(f"{Name}-Subject wise Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()

root=tk.Tk()
root.title("Student Result Analysis System")
root.geometry("500x500")
root.configure(bg="beige")

heading=tk.Label(root, text="STUDENT RESULT ANALYSIS SYSTEM", font=("Calibri",20,"bold"),fg="red",bg="white")
heading.pack()

tk.Label(root, text="Student Name").pack()
name=tk.Entry(root)
name.pack()

tk.Label(root, text="Python Marks").pack()
python=tk.Entry(root)
python.pack()

tk.Label(root, text="Java Marks").pack()
java=tk.Entry(root)
java.pack()

tk.Label(root, text="C Marks").pack()
c=tk.Entry(root)
c.pack()

tk.Label(root, text="SQL Marks").pack()
sql=tk.Entry(root)
sql.pack()

tk.Button(root, text="Analyze Result",command=analyse_marks).pack()

result=tk.Label(root, text="")
result.pack()

root.mainloop()



#-----------------------TASK 2-------------------------
import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

def track_expense():
    Name=name.get()
    Hr=int(hr.get())
    Cab=int(cab.get())
    Food=int(food.get())
    Extra=int(ext.get())

    data={
        "Category":["Home Rent","Cab","Food","Extra"],
        "Expenses":[Hr,Cab,Food,Extra]
        }
    df=pd.DataFrame(data)

    total=np.sum(data["Expenses"])
    Avg=np.mean(data["Expenses"])

    result.config(text=f"Name :{Name}\n Total Marks: {total}\n Average: {Avg}\n ")
    
    plt.pie(df["Expenses"],
            labels=df["Category"],
            autopct="%1.1f%%",
            startangle=90,shadow=True,)

    plt.title(f"{Name} - Expense Distribution")
    plt.show()
    
root=tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("600x600")
root.config(bg="lightblue")

heading=tk.Label(root, text="PERSONAL EXPENSE TRACKER", font=("AERIAL",23,"bold"),fg="white",bg="black")
heading.pack(pady=10)

tk.Label(root,text="Name").pack()
name=tk.Entry(root)
name.pack(pady=10)

tk.Label(root,text="Home rent").pack()
hr=tk.Entry(root)
hr.pack(pady=10)

tk.Label(root,text="Cab").pack()
cab=tk.Entry(root)
cab.pack(pady=10)

tk.Label(root,text="Food").pack()
food=tk.Entry(root)
food.pack(pady=10)

tk.Label(root,text="Extra").pack()
ext=tk.Entry(root)
ext.pack(pady=10)


tk.Button(root,text="Track Expense",command=track_expense).pack()

result=tk.Label(root,text="")
result.pack()

root.mainloop()



#-----------------------TASK 3-------------------------
import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

books=[]
categories=[]
copies=[]

def add_book():
    Book=bn.get()
    Category=bc.get()
    Copies=int(noc.get())

    books.append(Book)
    categories.append(Category)
    copies.append(Copies)

    result.configure(text="Book added")
def analyse():
    data={
        "Book":books,
        "Category":categories,
        "Copies":copies
        }

    df=pd.DataFrame(data)

    total=np.sum(df["Copies"])
    average=np.mean(df["Copies"])

    result.config(text=f"Total Copies: {total}\n Average Copies: {average}")

    category_sum=df.groupby("Category")["Copies"].sum()

    plt.bar(category_sum.index,category_sum.values)
    plt.title("Library Book Category Distribution")
    plt.xlabel("Category")
    plt.ylabel("Number of Copies")
    plt.show()


root=tk.Tk()
root.title("Library Book Data Analyzer")
root.geometry("500x600")
root.config(bg="lightyellow")

heading=tk.Label(root,text="LIBRARY BOOK DATA ANALYZER",font=("Helvetica",20,"bold italic"),fg="blue",bg="white")
heading.pack(pady=10)

tk.Label(root,text="Book Name").pack()
bn=tk.Entry(root)
bn.pack(pady=5)

tk.Label(root,text="Category").pack()
bc=tk.Entry(root)
bc.pack(pady=5)

tk.Label(root,text="Number of Copies").pack()
noc=tk.Entry(root)
noc.pack(pady=5)

tk.Button(root,text="Add Book",command=add_book).pack(pady=5)

tk.Button(root,text="Analyze Library Data",command=analyse).pack(pady=5)

result=tk.Label(root,text="")
result.pack()

root.mainloop()



#-----------------------TASK 4-------------------------
import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

def analyse_quiz():
    Name=name.get()
    Q1=int(q1.get())
    Q2=int(q2.get())
    Q3=int(q3.get())
    Q4=int(q4.get())

    data={
        "Question":["Q1","Q2","Q3","Q4"],
        "Score":[Q1,Q2,Q3,Q4]
        }

    df=pd.DataFrame(data)

    total=np.sum(df["Score"])
    average=np.mean(df["Score"])
    highest=np.max(df["Score"])
    lowest=np.min(df["Score"])

    result.config(text=f"Total Score: {total}\nAverage Score: {average}\nHighest Score: {highest}\nLowest Score: {lowest}")

    plt.bar(df["Question"],df["Score"])
    plt.title(f"{Name} - Quiz Result Analysis")
    plt.xlabel("Questions")
    plt.ylabel("Score")
    plt.show()


root=tk.Tk()
root.title("Quiz Result Analyzer")
root.geometry("500x500")
root.config(bg="lavender")

heading=tk.Label(root,text="QUIZ RESULT ANALYZER",
                 font=("Helvetica",20,"bold italic"),
                 fg="purple",bg="white")
heading.pack(pady=10)

tk.Label(root,text="Student Name").pack()
name=tk.Entry(root)
name.pack(pady=5)

tk.Label(root,text="Question 1 Score").pack()
q1=tk.Entry(root)
q1.pack(pady=5)

tk.Label(root,text="Question 2 Score").pack()
q2=tk.Entry(root)
q2.pack(pady=5)

tk.Label(root,text="Question 3 Score").pack()
q3=tk.Entry(root)
q3.pack(pady=5)

tk.Label(root,text="Question 4 Score").pack()
q4=tk.Entry(root)
q4.pack(pady=5)

tk.Button(root,text="Analyze Quiz Result",command=analyse_quiz).pack(pady=10)

result=tk.Label(root,text="")
result.pack()

root.mainloop()
