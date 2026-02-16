#TASK 1:
import csv

print("##Task 1:")
with open("employee.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["Name","Age","Department"])
    w.writerow(["Alice",25,"HR"])
    w.writerow(["Bob",30,"Finance"])
    w.writerow(["Charlie",28,"IT"])

print("Employee data written successfully")
print("Reading csv file")
with open("employee.csv","r") as f:
    r=csv.reader(f)
    for row in r:
        print(row)

data=[{"Name":"Prajwal",
       "Age":21,
       "Department":"sales"}]
with open("employee_dict.csv","w",newline="") as f:
    field_names=["Name","Age","Department"]
    w=csv.DictWriter(f,fieldnames=field_names)
    w.writeheader()
    w.writerows(data)
print("Dictionary CSV file created\n")


#TASK 2:
from datetime import datetime

print("##Task 2:")
c_t = datetime.now()

print("System date: ",c_t.date())
print("System time: ",c_t.time().strftime("%H:%M:%S"))
print("Year : ",c_t.year)
print("Month: ",c_t.month)
print("Day :",c_t.day)
print("Formatted date & time:", c_t.strftime("%Y-%m-%d %H:%M:%S"))
print()

#TASK 3:
import time as t

print("##Task 3:")

print("Current timestamp:", t.time())
print("Readable time:", t.ctime())

print("Waiting for 2 seconds")
t.sleep(2)

print("Continuing execution\n")


#TASK 4:
import zipfile as zp
import tarfile as tf

print("##Task 4:")

print("Creating backup.zip")
with zp.ZipFile("backup.zip","w") as z:
    z.write("employee.csv")
    z.write("employee_dict.csv")

print("Creating backup.tar.gz")
with tf.open("backup.tar.gz","w:gz") as t:
    t.add("employee.csv")
    t.add("employee_dict.csv")

print("Files inside backup.zip:")
with zp.ZipFile("backup.zip","r") as z:
    print(z.namelist())

print("Files inside backup.tar.gz:")
with tf.open("backup.tar.gz","r:gz") as t:
    print(t.getnames())

print("Backup completed successfully\n")


#TASK 5:
import threading as td
import time

print("##Task 5:")

def backup():
    for i in range(3):
        print("Backup running in background")
        time.sleep(2)

t=td.Thread(target=backup)
t.start()

time.sleep(0.1)
print("Main program continues working")

t.join()

print("Main thread finished")
print("Program completed successfully")





