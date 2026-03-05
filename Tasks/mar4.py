##-------------------------TASK 1---------------------------
import tkinter as tk
import random

def generate():
    l=int(e.get())
    c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    pw=""
    for i in range(l):
        pw=pw+random.choice(c)

    l2.config(text="Password: "+pw)

root=tk.Tk()
root.title("Password generator")
root.geometry("300x200")

l1=tk.Label(root,text="Enter Password Length")
l1.pack()

e=tk.Entry(root)
e.pack()

b=tk.Button(root,text="Generate",command=generate)
b.pack()

l2=tk.Label(root,text="")
l2.pack()
root.mainloop()


##-------------------------TASK 2---------------------------
import tkinter as tk

def table():
    n=int(e.get())
    res=""

    for i in range(1,11):
        res=res+str(n)+" x "+ str(i)+" = "+str(n*i)+"\n"
    l2.config(text=res)

root= tk.Tk()
root.title("Multiplication Table")
root.geometry("300x200")

l1=tk.Label(root,text="Enter a Number")
l1.pack()

e=tk.Entry(root)
e.pack()

b=tk.Button(root,text="Generate Table",command=table)
b.pack()

l2=tk.Label(root,text="")
l2.pack()

root.mainloop()


##-------------------------TASK 3---------------------------
import tkinter as tk
import random

def dice():
    n=random.randint(1,6)
    l2.config(text="Dice Number: " + str(n))

root=tk.Tk()
root.title("Dice roll")
root.geometry("300x200")

l1=tk.Label(root,text="Click to roll the dice")
l1.pack()

b=tk.Button(root,text="Roll Dice",command=dice)
b.pack()

l2=tk.Label(root,text="")
l2.pack()

root.mainloop()

##-------------------------TASK 4---------------------------
import tkinter as tk
import random

n=random.randint(1,10)

def check():
    g=int(e.get())

    if g==n:
        l2.config(text="Correct guess")
    else:
        l2.config(text="Wrong guess")

root=tk.Tk()
root.title("Number guessing game")
root.geometry("300x200")

l1=tk.Label(root,text="Guess a number between 1 and 10")
l1.pack()

e=tk.Entry(root)
e.pack()

b=tk.Button(root,text="Check",command=check)
b.pack()

l2=tk.Label(root,text="")
l2.pack()
root.mainloop()


##-------------------------TASK 5---------------------------
import tkinter as tk

def Count():
    t=txt.get("1.0",tk.END)

    words=t.split()
    w_count=len(words)

    char_count=len(t)

    l2.config(text="Words: " + str(w_count) + "   Characters: " + str(char_count))

root=tk.Tk()
root.title("Word counter")
root.geometry("300x200")

l1=tk.Label(root,text="Enter text")
l1.pack()

txt=tk.Text(root,height=5,width=30)
txt.pack()

b=tk.Button(root,text="Count",command=Count)
b.pack()

l2=tk.Label(root,text="")
l2.pack()
root.mainloop()
