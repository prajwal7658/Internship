####TASK 1
##print("-------------------TASK 1--------------------")
##
##import sys
##from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
##
##def message():
##    print("Hello Student!")
##    print()
##    
##app=QApplication(sys.argv)
##
##window=QWidget()
##window.setWindowTitle("PyQt page")
##window.resize(300,200)
##
##label=QLabel("This is a label",window)
##label.move(100,50)
##
##button=QPushButton("Button",window)
##button.move(100,80)
##
##button.clicked.connect(message)
##
##window.show()
##sys.exit(app.exec_())



##TASK 2:
##PART 1
print("-------------------TASK 2: Part 1--------------------")
import nltk
from nltk.tokenize import sent_tokenize

text="Online shopping has become very convenient today. Customers expect fast delivery and good product quality."

sentence=sent_tokenize(text)

print("Sentence tokens:")
print(sentence)
print("\n\n")


##PART 2
print("-------------------TASK 2: Part 2--------------------")
from nltk.tokenize import word_tokenize

text="Online shopping has become very convenient today. Customers expect fast delivery and good product quality."

words=word_tokenize(text)

print("Word tokens:")
print(words)
print("\n\n")


##PART 3
print("-------------------TASK 2: Part 3--------------------")

from nltk.stem import PorterStemmer

ps=PorterStemmer()

words=["delivery","delivering","delivered","customers","shopping","quality"]

print("Original words:")
print(words)

print("Stemmed words:")

for w in words:
    print(ps.stem(w))
print("\n\n")


##PART 4
print("-------------------TASK 2: Part 4--------------------")

from nltk import pos_tag

sentence="Online shopping has become very convenient today."

words=word_tokenize(sentence)

pos=pos_tag(words)

print("POS tagged words:")
print(pos)
print("\n\n")


##PART 5
print("-------------------TASK 2: Part 5--------------------")

from nltk.corpus import stopwords
text="Online shopping has become very convenient today."

words=word_tokenize(text)

stop_words=set(stopwords.words('english'))

filtered_words=[]

for w in words:
    if w.lower() not in stop_words:
        filtered_words.append(w)

print("Original words:")
print(words)

print("Filtered words:")
print(filtered_words)

