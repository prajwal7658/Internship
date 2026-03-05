#1
print("------------TASK 1-------------")
n=int(input("Enter a number: "))
a,b=0,1

for i in range(n):
    print(a,end=" ")
    temp=a+b
    a=b
    b=temp
print()
    
#2.
print("------------TASK 2-------------")
def Prime(n):
    print()
    if n<=1:
        print("Not prime")
        return
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            return
    print("Prime number")
Prime(10)
print()

#3.
print("------------TASK 3-------------")
n=int(input("Enter a number:"))
temp=n
total=0
s=str(n)
l=len(s)

while n>0:
    rem=n%10
    total=total+rem**l
    n=n//10
if total==temp:
    print("amstrong")
else:
    print("not amstrong")
print()

#4.
print("------------TASK 4-------------")
def swap(a,b):
    print(f"numbers before swap: a={a}, b={b}")
    a=a+b      
    b=a-b      
    a=a-b
    print(f"After swap: a={a}, b={b}")
swap(10,15)
print()

#5.
print("------------TASK 5-------------")
s=input("Enter sentence: ")
count=0
word=s.split(" ")
count=len(word)

print("Count of words :",count)
print()

#6.
print("------------TASK 6-------------")
y=int(input("Enter year: "))

if (y%4==0 and y%100!=0) or (y%400==0):
    print("Leap year")
else:
    print("Not leap year")
print()

#7
print("------------TASK 7-------------")
l=[1,4,3,6,8,12,22,2,3]
m=l[0]
for i in l:
    if i>m:
        m=i
    else:
        continue
print("Max = ",m)
print()

#8.
print("------------TASK 8-------------")
def pal(s):
    rev=""
 
    for i in s:
        rev=i+rev
    
    if s==rev:
        print("Palindrome")
    else:
        print("Not palindrome")

pal(input("Enter a string: "))
print()

#9.
print("------------TASK 9-------------")
s=input("Enter a sentence: ")

upper=0
lower=0
digit=0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1

print("Upper count:", upper)
print("Lower count:", lower)
print("Digit count:", digit)
print()

#10.
print("------------TASK 10-------------")
for n in range(2,101):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    
    if prime:
        print(n,end=" ")
print()

#11.
print("------------TASK 11-------------")
l=[1,4,3,6,8,12,22,2,3]
l.sort()
print(l[1])
print()


#12.
print("------------TASK 12-------------")
l1=[1,2,5,4,7,3]
l2=[3,6,9,5,7,0]

for i in l1:
    if i in l2:
        print(i,end=" ")
print()

#13.
print("------------TASK 13-------------")
s=input("Enter a sentence :")
word=s.split(" ")

for i in word:
    print(i[::-1],end=" ")
print()

#14.
print("------------TASK 14-------------")
print("1 for Celsius to Fahrenheit")
print("2 for Fahrenheit to Celsius")

c=int(input("Enter your choice: "))

if c==1:
    cel=float(input("Enter temperature in Celsius: "))
    far=(cel*9/5)+32
    print("Temperature in Fahrenheit:", far)

elif c==2:
    far= float(input("Enter temperature in Fahrenheit: "))
    cel=(far-32)*5/9
    print("Temperature in Celsius:", cel)

else:
    print("Invalid Choice")
print()

#15.
print("------------TASK 15-------------")
n=int(input("Enter a number: "))

Sum=0
product=1
temp=n

while n>0:
    rem=n%10
    Sum+=rem
    product*=rem
    n=n//10

if Sum==product:
    print("Spy number")
else:
    print("Not a spy number")
print()

#16.
print("------------TASK 16-------------")
s=input("Enter a sentence: ")
s1=""

for i in s:
    if i!=" ":
        s1+=i

print("After removing spaces:", s1)
print()

#17.
print("------------TASK 17-------------")
n=[10,20,30,40,50]

count=0

for i in n:
    count+=1

print("Length of list:", count)
print()

#18.
print("------------TASK 18-------------")
s=input("Enter a sentence: ")

words=s.split()
count=0

for word in words:
    if word[0].lower() in "aeiou":
        count+=1

print("Words starting with vowel:", count)
print()

#19.
print("------------TASK 19-------------")
s1=input("Enter first string: ")
s2=input("Enter second string: ")

s1=s1.replace(" ", "").lower()
s2=s2.replace(" ", "").lower()

if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")
print()

#20.
print("------------TASK 20-------------")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

while b!=0:
    a,b=b,a%b

print("GCD is:", a)
print()







