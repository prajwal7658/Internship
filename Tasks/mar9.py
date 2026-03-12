##TASK 1:
print("---------------------TASK 1-----------------------")
prod={
    "laptop": 60000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000
}

print("Available products:",prod.keys())

p=input("Enter product name: ")

if p in prod:
    print("Price:", prod[p])
else:
    print("Product not found")
print()




#TASK 2:
print("---------------------TASK 2-----------------------")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

while True:
    print("1-> Red")
    print("2-> Green")
    print("3-> Blue")
    print("4-> Exit")
    print()
    
    c=int(input("Enter your choice: "))

    if c==1:
        print("code for red:",red)
        print()
    elif c==2:
        print("code for green:",green)
        print()
    elif c==3:
        print("code for blue:",blue)
        print()
    elif c==4:
        print("Program ended")
        break
        print()
    else:
        print("Invalid Choice")
        print()



#TASK 3:
print("---------------------TASK 3-----------------------")
inf1={"Alice","Bob","Charlie","David","Eva"}
inf2={"Charlie","David","Frank","George","Alice"}

print(f"Mutual followers :{inf1 & inf2}")
print(f"All followers :{inf1 | inf2}")
print(f"Follows only one influencer :{inf1 ^ inf2}")



#TASK 4:
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Text display")
window.resize(400,300)

label=QLabel("Hello Prajwal",window)
label.setAlignment(Qt.AlignCenter)

layout=QVBoxLayout()
layout.addWidget(label)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())


#TASK 5:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def message():
    result.setText("Button Clicked")

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Button click")
window.resize(300,200)

button=QPushButton("Click Me")
result=QLabel("")

layout=QVBoxLayout()
layout.addWidget(button)
layout.addWidget(result)

window.setLayout(layout)

button.clicked.connect(message)

window.show()
sys.exit(app.exec_())


#TASK 6:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def add():
    n1=int(num1.text())
    n2=int(num2.text())
    result.setText("Sum = " + str(n1+n2))

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Calculator")
window.resize(300,300)

l1=QLabel("Enter first number:")
num1=QLineEdit()

l2=QLabel("Enter second number:")
num2=QLineEdit()

button=QPushButton("Add")

result=QLabel("")

layout=QVBoxLayout()
layout.addWidget(l1)
layout.addWidget(num1)
layout.addWidget(l2)
layout.addWidget(num2)
layout.addWidget(button)
layout.addWidget(result)

window.setLayout(layout)

button.clicked.connect(add)

window.show()
sys.exit(app.exec_())



#TASK 7:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def change_color():
    window.setStyleSheet("background-color:lightblue")

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Change background color")
window.resize(300,200)

button=QPushButton("Change color")

layout=QVBoxLayout()
layout.addWidget(button)

window.setLayout(layout)

button.clicked.connect(change_color)

window.show()
sys.exit(app.exec_())


#TASK 8:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def increase():
    c=int(label.text())
    c=c+1
    label.setText(str(c))

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Counter")
window.resize(300,200)

label=QLabel("0")
button=QPushButton("Increase")

layout=QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)

button.clicked.connect(increase)

window.show()
sys.exit(app.exec_())


#TASK 9:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Language Selection")
window.resize(300,200)

label=QLabel("Select Language:")

dropdown=QComboBox()
dropdown.addItems(["English","Hindi","Kannada","Tamil","Telugu"])

layout=QVBoxLayout()
layout.addWidget(label)
layout.addWidget(dropdown)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())


#TASK 10:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def submit():
    name=name_box.text()
    usn=usn_box.text()
    branch=branch_box.text()
    
    result.setText("Registered: " + name)

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Student registration form")
window.resize(300,300)

name_label=QLabel("Enter Name:")
name_box=QLineEdit()

usn_label=QLabel("Enter USN:")
usn_box=QLineEdit()

branch_label=QLabel("Enter Branch:")
branch_box=QLineEdit()

button=QPushButton("Submit")

result=QLabel("")

layout=QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_box)
layout.addWidget(usn_label)
layout.addWidget(usn_box)
layout.addWidget(branch_label)
layout.addWidget(branch_box)
layout.addWidget(button)
layout.addWidget(result)

window.setLayout(layout)
button.clicked.connect(submit)

window.show()
sys.exit(app.exec_())



















