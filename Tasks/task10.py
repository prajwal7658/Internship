import os

#1. Create a folder named "Intern_Data".
os.mkdir("Intern_Data")

#2. Inside that folder, create a file named "info.txt".
with open("Intern_Data/info.txt","w") as f:

#3. Write your Name and Course inside the file.
    f.write("Name: Prajwal\n")
    f.write("Course: AIML")

#4. Check whether the file exists or not.
print(os.path.exists("Intern_Data/info.txt"))

#5. Display the current working directory.
print(os.getcwd())

#6. List all files inside the "Intern_Data" folder.
print(os.listdir("Intern_Data"))

#7. Display the operating system type.
print("OS Type:", os.name)

#8. Rename the file from info.txt to student_info.txt.
os.rename("Intern_Data/info.txt","Intern_Data/student_info.txt")
print("Renamed")




import sys

#1. Print the script name using sys.argv.
print("Script name:",sys.argv[0])

#2. Print all command-line arguments entered.
print("Arguments list:",sys.argv[1:])

#3. Print the Python version.
print("Python version:",sys.version)

#4. Take user input using standard input .
name=input("Enter name: ")

#5. Display a welcome message using the entered name.
print("Welcome",name)

#6. Display output using standard output.
sys.stdout.write("Hello..")



import shutil

#1. Copies a file named "sample.txt"
#2. Pastes it as "copy_sample.txt"
shutil.copy("source.txt","destination.txt")

#3. Prints disk usage
total,used,free=shutil.disk_usage("/")

print("File copied successfully")
print(f"Total: {total//1024**3}GB")
print(f"Used: {used//1024**3}GB")
print(f"Free: {free//1024**3}GB")



import math

n=float(input("Enter a number: "))

print("Square root:", math.sqrt(n))
print("Factorial:", math.factorial(int(n)))
print("Floor value:", math.floor(n))
print("Ceiling value:", math.ceil(n))



import random

#1. Generate a random number between 1 and 6 (like rolling a dice).
dice = random.randint(1, 6)

#2. Print the dice result.
print("Dice rolled:",dice)

#3. Create a list of cards:["Ace", "King", "Queen", "Jack"]
cards = ["Ace","King","Queen","Jack"]

#4. Shuffle the cards randomly.
random.shuffle(cards)
print("Shuffled Cards:", cards)

#5. Generate and print one random card from the shuffled list.
print("Random Card:", random.choice(cards))



import statistics

#1. Create a list of student marks (example: 78, 85, 92, 88, 76).
marks=[75,45,82,98,76]

#2. Display all calculated results clearly.
print("Marks: ",marks)

#3. Calculate the average of the marks.
print("Mean: ",statistics.mean(marks))

#4. Calculate the median of the marks.
print("Median: ",statistics.median(marks))

#5. Calculate the standard deviation of the marks.
print("Standard Deviation: ",statistics.stdev(marks))



import json

#1. Take location and college name as input from the user.
location=input("Enter location: ")
college=input("Enter college name: ")

data={
    "Location": location,
    "College": college
}

#2. Store the data in a JSON file named data.json.
with open("data.json","w") as f:
    json.dump(data,f)

#3. Read the data from the JSON file.
with open("data.json","r") as f:
    stored_data=json.load(f)

#4. Print the stored data clearly.
print("Location:",stored_data["Location"])
print("College:",stored_data["College"])







































