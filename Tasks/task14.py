##TASK 1:
import tkinter as tk

root=tk.Tk()
root.title("Basic Tkinter page")
root.geometry("400x300")
root.configure(bg="lightblue")

root.mainloop()


##TASK 2:
import tkinter as tk

root=tk.Tk()
root.title("Label")
root.geometry("300x200")

l=tk.Label(root,text="Welcome to Tkinter")
l.pack()

root.mainloop()


##TASK 3:
import tkinter as tk

root=tk.Tk()
root.title("My fist TKinter app")
root.geometry("300x200")

l=tk.Label(root,text="Prajwal",font=("Arial",20))
l.pack()

root.mainloop()


##TASK 4:
import tkinter as tk

root=tk.Tk()
root.title("Multiple Labels")
root.geometry("300x200")

l1=tk.Label(root,text="First label",fg="red")
l1.pack(pady=10)

l2=tk.Label(root,text="Second label",fg="green")
l2.pack(pady=10)

l3=tk.Label(root,text="Third label",fg="blue")
l3.pack(pady=10)

root.mainloop()


##TASK 5:
import tkinter as tk
root=tk.Tk()
root.title("Button")
root.geometry("300x200")

b=tk.Button(root,text="Submit")
b.pack(pady=10)

root.mainloop()


##TASK 6:
import tkinter as tk
def change():
    l.config(text="Button clicked",fg="red")

root=tk.Tk()
root.title("Button action")
root.geometry("300x200")

l=tk.Label(root,text="Hii")
l.pack(pady=10)

b=tk.Button(root,text="Click",command=change)
b.pack(pady=10)

root.mainloop()


##TASK 7:
import tkinter as tk

root=tk.Tk()
root.title("Entry")
root.geometry("300x200")

e=tk.Entry(root,bg="yellow",fg="blue")
e.pack(pady=20)

root.mainloop()


##TASK 8:
import tkinter as tk

def show():
    l.config(text=e.get())
root=tk.Tk()
root.title("Reading input")
root.geometry("300x200")

e=tk.Entry(root)
e.pack(pady=10)
b=tk.Button(root,text="Show",command=show)
b.pack(pady=10)

l=tk.Label(root,text="")
l.pack(pady=10)
root.mainloop()


##TASK 9:
import tkinter as tk

root=tk.Tk()
root.title("Grid Layout")
root.geometry("300x150")

l1=tk.Label(root,text="Name")
l1.grid(row=0,column=0)
e1=tk.Entry(root)
e1.grid(row=0,column=1)

l2=tk.Label(root,text="Age")
l2.grid(row=1,column=0)
e2=tk.Entry(root)
e2.grid(row=1,column=1)
root.mainloop()


##TASK 10:
import tkinter as tk
def red():
    root.configure(bg="red")

def green():
    root.configure(bg="green")

def blue():
    root.configure(bg="blue")
root=tk.Tk()
root.title("Color Buttons")
root.geometry("300x200")

b1=tk.Button(root,text="Red",command=red)
b1.pack(pady=5)

b2=tk.Button(root,text="Green",command=green)
b2.pack(pady=5)

b3=tk.Button(root,text="Blue",command=blue)
b3.pack(pady=5)
root.mainloop()


##TASK 11:
import tkinter as tk
def click():
    l.config(text="Mouse clicked")

root=tk.Tk()
root.title("Mouse click")
root.geometry("300x200")

b=tk.Button(root,text="Click me",command=click)
b.pack(pady=10)

l=tk.Label(root,text="")
l.pack(pady=10)
root.mainloop()


##TASK 12:
import tkinter as tk
def show():
    l.config(text="Selected: " + v.get())

root=tk.Tk()
root.title("Radio button")
root.geometry("300x200")

v=tk.StringVar()

r1=tk.Radiobutton(root,text="male",variable=v,value="male")
r1.pack()

r2=tk.Radiobutton(root,text="female",variable=v,value="female")
r2.pack()

b=tk.Button(root,text="submit",command=show)
b.pack(pady=5)

l=tk.Label(root,text="")
l.pack()
root.mainloop()


##TASK 13:
import tkinter as tk
from tkinter import messagebox
def info():
    messagebox.showinfo("Info","This is information")

def warn():
    messagebox.showwarning("Warning","This is warning")

def error():
    messagebox.showerror("Error","This is error")

root=tk.Tk()
root.title("Message Box")
root.geometry("300x200")

b1=tk.Button(root,text="Info",command=info)
b1.pack(pady=5)

b2=tk.Button(root,text="Warning",command=warn)
b2.pack(pady=5)

b3=tk.Button(root,text="Error",command=error)
b3.pack(pady=5)
root.mainloop()


##TASK 14:
import tkinter as tk
from tkinter import messagebox

def show_msg():
    messagebox.askyesno("Confirm","Do you want to exit?")

root=tk.Tk()
root.title("Message box")
root.geometry("200x100")

b=tk.Button(root, text="Show message",command=show_msg)
b.pack(pady='20')

root.mainloop()

##TASK 15:
import tkinter as tk
def light():
    root.configure(bg="white")
def dark():
    root.configure(bg="black")

root=tk.Tk()
root.title("Theme change")
root.geometry("300x200")

b1=tk.Button(root,text="Light mode",command=light)
b1.pack(pady=10)

b2=tk.Button(root,text="Dark mode",command=dark)
b2.pack(pady=10)
root.mainloop()


































