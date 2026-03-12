##TASK 1:
print("-------------------TASK 1---------------------")
l=[1,2,3,4,6,7]
n=7

total=sum(l)

actual=(n*(n+1))//2
missing=actual-total

print(missing)
print()


#TASK 2:
print("-------------------TASK 2---------------------")
s1=input("Enter first string :").lower()
s2=input("Enter second string :").lower()

s1=sorted(s1)
s2=sorted(s2)

if s1==s2:
    print("anagrams")
else:
    print("not anagrams")
print()


#TASK 3:
print("-------------------TASK 3---------------------")
n=int(input("Enter N: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
print()


#TASK 4:
print("-------------------TASK 4---------------------")
n=int(input("Enter a number: "))

if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
print()


#TASK 5:
print("-------------------TASK 5---------------------")
n=589
Sum=0
while n>0:
    rem=n%10
    Sum=Sum+rem
    n=n//10
print(Sum)
print()


#TASK 6:
print("-------------------TASK 6---------------------")
n=213
prod=1
while n>0:
    rem=n%10
    prod=prod*rem
    n=n//10
print(prod)
print()


#TASK 7:
print("-------------------TASK 7---------------------")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

Max=max(a,b)
while True:
    if Max%a==0 and Max%b==0:
        print("LCM:",Max)
        break
    Max=Max+1
print()


#TASK 8:
print("-------------------TASK 8---------------------")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
gcd=1

Min=min(a,b)
for i in range(1,Min+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD:",gcd)
print()


#TASK 9:
print("-------------------TASK 9---------------------")
l1=[2,4,6,8,5,10]
l2=[2,3,5,9,7,6]

for i in l1:
    if i in l2:
        print(i,end=" ")
print()


#TASK 10:
print("-------------------TASK 10---------------------")
l1=[2,5,4,8,1,9]
l1=sorted(l1)

print("second smallest: ",l1[1])
print()


#TASK 11:
print("-------------------TASK 11---------------------")
s="abcdefabcab"
m_len=0
for i in range(len(s)):
    ss=""
    for j in range(len(s)):
        if s[j] not in ss:
            ss=ss+s[j]
        else:
            break

    if len(ss)>m_len:
        m_len=len(ss)
    
print(m_len)      
print()


#TASK 12:
print("-------------------TASK 12---------------------")
s="abbbc"
f={}

for i in s:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1

for i in s:
    if f[i]==1:
        print(i)
        break













