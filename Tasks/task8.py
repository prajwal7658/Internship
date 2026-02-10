###1. Write a function to multiply two numbers and return the result and print it in the function call. 
##def mul(a,b):
##    return a*b
##print(mul(10,5))
##print()
##
###2. Create a function to check whether a number is even or odd.
##def Check(x):
##    if x%2==0:
##        print("Number is odd")
##    else:
##        print("Number is even")
##Check(11)
##print()
##
###3. Write a function to find the maximum of three numbers.
##def Max(a,b,c):
##    if a>b>c:
##        print("a is greater")
##    elif b>a>c:
##        print("b is greater")
##    else:
##        print("c is greater")
##Max(10,4,17)
##print()   
##
###4. Create a function to calculate the factorial of a number.
##def fact(n):
##    f=1
##    for i in range(1,n+1):
##        f = f*i
##    print(f)
##fact(int(input("Enter a number: ")))
##print()
##
###5. Write a function to count vowels in a given string.
##def vow(s):
##    count=0
##    for x in s:
##        if x in "aeiouAEIOU":
##            count+=1
##    return count
##print(vow("Hello from Prajwal"))
##print()
##
###6. Define a function to reverse a string.
##def rev(s):
##    return s[::-1]
##print(rev("Internship Program"))
##print()
##
###7. Write a function to check if a number is prime.
##def prime(n):
##    if n<=1:
##        return False
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    return True
##prime(7)
##print()
##
###8. Write a function using default arguments.
##def greet(name="Prajwal"):
##    print("Hello", name)
##greet()
##print()
##
###9. Create a function using keyword arguments.
##def student(name, age):
##    print(name, age)
##student(age=21,name="Prajwal")
##print()
##
###10. Write a recursive function to calculate Fibonacci series. 
##def fib(n):
##    if n <= 1:
##        return n
##    return fib(n-1) + fib(n-2)
##fib(10)
##print()
##
###11.Write a lambda function to find the square of a number.
##a=lambda x:x*x
##print(a(4))




#1.Handle ZeroDivisionError.
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
print()

#2.Handle ValueError when converting input to integer.
try:
    s=input("Enter a string: ")
    print(s)
    int(s)
except ValueError:
    print("String cannot be converted to int")
print()
 
#3.Write a program using try and except.
try:
    print(10/x)
except:
    print("Error occurred.No variable found")
print()

#4.Write a program using try, except, else.
try:
    x=int(input("Enter number: "))
    print(10/x)
except:
    print("Error occurred")
else:
    print("Operation successful")
print()

#5.Write a program using try, except, finally.
try:
    print(10/x)
except:
    print("Error occurred.No variable found")
finally:
    print("Finally block executed")
print()
   
#6.Handle TypeError.
try:
    a=5+"10"
except TypeError:
    print("Type mismatch error")
print()

#7.Handle multiple exceptions in a single try block.
try:
    x=int(input("Enter number: "))
    print(10/x)
except (ValueError,ZeroDivisionError):
    print("Invalid input or division by zero")
print()

#8.Raise an exception using raise keyword.
age=int(input("Enter age: "))
if age<0:
    raise ValueError("Age cannot be negative")
else:
    print("Valid age")


