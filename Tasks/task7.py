##a,b=10,6
##s=a+b
##diff=a-b
##pro=a*b
##div=a/b
##
##print(s, diff, pro, div)
##
##rem=a%b
##print(rem)
##
##P,T,R=1000,5,3
##SI=(P*T*R)/100
##print(SI)
##
##minutes=40
##hours=minutes//60
##minu=minutes%60
##print(f"Time is {hours} : {minu}")
##
##n=int(input("Enter a number: "))
##print("Square root :",n**2)
##print("Cube root :",n**3)
##
##marks=int(input("Enter marks :"))
##if marks>=35:
##    print("Pass")
##else:
##    print("Failed")
##
##age1=int(input("Enter age 1: "))
##age2=(int(input("Enter age 2: ")))
##if age1>age2:
##    print("Peson 1 is older")
##elif age2>age1:
##    print("Person 2 is older")
##else:
##    print("Both are same aged")
##
##num=int(input("Enter a nimber:"))
##if num>=100:
##    print("Number is greater than or equal to 100")
##else:
##    print("Number is less than 100")
##
##if num>0 or num==0:
##    print("Number is positive or zero")
##else:
##    print("Number is negative")
##
##if not(num<0):
##    print("Number is not negative")
##else:
##    print("Number is negative")



##a,b=20,45
##if a>b:
##    print("a is greater than b")
##else:
##    print("b is greater than a")
##
##age=int(input("Enter the age: "))
##if age>=18:
##    print("Person is eligible to vote")
##else:
##    print("Person cant vote")
##
##n=int(input("Enter a number: "))
##if n%2==0:
##    print("The number is even")
##else:
##    print("Number is odd")
##
##marks = int(input("Enter the marks: "))
##if marks >= 90:
##    print("Grade A")
##elif marks >= 75:
##    print("Grade B")
##elif marks >= 50:
##    print("Grade C")
##else:
##    print("Fail")

##for i in range(1, 11):
##    print(i)
##print("\n")
##
##for i in range(1, 51):
##    if i % 2 == 0:
##        print(i)
##print("\n")
##
##n = int(input("Enter a number : "))
##for i in range(1, 11):
##    print(n, "*", i, "=", n * i)
##print("\n")
##
##st = "S V Prajwal"
##for i in st:
##    print(i)
##print("\n")
##
##num = int(input("Enter a number : "))
##total = 0
##for i in range(1, num + 1):
##    total += i
##print("Sum is :", total)
##print("\n")
##
##text = input("Enter a string: ")
##count = 0
##for i in text:
##    if i in "aeiouAEIOU":
##        count += 1
##print("Number of vowels =", count)


i=10
while i>=1:
    print(i)
    i=i-1
print("\n")

n=int(input("Enter a number: "))
Sum=0
while n>0:
    dig=n%10
    Sum=Sum+dig
    n=n//10
print("Sum of digit :",Sum)
print("\n")

num=int(input("Enter a number: "))
count=0
while num>0:
    count=count+1
    num=num//10
print("Number of digits =",count)
















    
