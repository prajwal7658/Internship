#Task 1:
print("##TASK 1:")
s="Artificial Intelligence"

print(s[:11])
print(s[-5:])
print(s[1::2])
print(s[::-1])
print(s[11::])
print()

#Task 2:
print("##TASK 2:")
email="student@gmail.com"
print("username :",email[:7])
print("domain name :",email[8:13])
print("domain extension:",email[-4:])
print()

#Task 3:
print("##TASK 3:")
n=[10,20,30,40,50]
n.append(60)
print(n)

n.remove(30)
print(n)

n.insert(2,25)
print(n)

print("Max =",max(n))
print("Min =",min(n))

print(n[::-1])
print()

#Task 4:
print("##TASK 4:")
d=[12,45,67,23,89,45,12,90]
d1=[]
for i in d:
    if i not in d1:
        d1.append(i)
print(d1)
d1.sort()
print(d1)

d1.sort(reverse=True)
print(d1)
print()

#Task 5:
print("##TASK 5:")
t=(10,20,30,40,50)
print(t[0],t[-1])

print(len(t))

if 30 in t:
    print("30 is present")
else:
    print("not present")
l1=list(t)
print(l1)
print()

#Task 6:
print("##TASK 6:")
s={"name":"Prajwal",
    "age":21,
    "marks":85
    }

print(s.keys())
print(s.values())

s["grade"]="A"
print(s)

s["marks"]=100
print(s)

del s["age"]
print(s)
print()

#Task 7:
print("##TASK 7:")
def add(a,b):
    return a+b
print(add(10,50))


def check(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
        
print(check(int(input("Enter a number :"))))


def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
print(fact(int(input("Enter a number: "))))   
print()

#Task 8:
print("TASK 8:")
for i in range(1,6):
    print(str(i)*i)
print()


#Task 9:
print("##TASK 9:")
def Sum(num):
    sum=0
    while num>0:
        last=num%10
        sum=sum+last
        num=num//10
    return sum

print(Sum(int(input("Enter a number: "))))
print()

#Task 10:
print("##TASK 10:")
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Student name: ",self.name)
        print("Student age: ",self.age)
        print("Student marks: ",self.marks)
        print()

s1=Student("Prajwal",21,87)
s2=Student("Rahul",22,76)

s1.display()
s2.display()
print()

#Task 11:
print("##TASK 11:")
class Bank:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.__bal=bal

    def deposit(self,amount):
        print("Initial amount: ",self.__bal)
        self.__bal=self.__bal+amount
        print("deposited: ",amount)
        print("Total balance after deposite: ",self.__bal)
        print()
        
    def withdraw(self,amount):
        if amount<=self.__bal:
            self.__bal=self.__bal-amount
            print("Withdrawn: ",amount)
            print("Balance after widtdraw: ",self.__bal)
        else:
            print("Insufficient balance")
        print()
        
    def display(self):
        print("Account Number:",self.acc_no)
        print("Current Balance:",self.__bal)

a1 = Bank(12345,1000)
a1.deposit(500)
a1.withdraw(200)
a1.display()
print()

#Task 12:
import pandas as pd
print("##TASK 12:")
d={ "Name":["A","B","C"],
    "Age":[20,21,19],
    "Marks":[85,90,78]
}

df=pd.DataFrame(d)
print(df)
print()

print("1st row:")
print(df.iloc[0])
print()

print("Marks:")
print(df["Marks"])
print()

##Task 13
print("##TASK 13:")
import pandas as pd
df=pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nColumn Names:")
print(df.columns)

df_no_null=df.dropna()
print("\nData after removing null values:")
print(df_no_null)

df_filled=df.fillna(df.mean(numeric_only=True))
print("\nData after replacing null with mean:")
print(df_filled)
print()

















