s="MachineLearningispowerful"
print(s[:7])
print(s[-8::])
print()
l1=[250,120,450,300,180,500]

for i in l1:
    if i>300:
        print(i)
print()

l2=l1.copy()
print(l2)
print()

l1[1]=200
print(l1)
print()

l1.clear()
print(l1)
print()

n=5
i=1
while i<=10:
    print(f"{n} * {i} = {n*i}")
    i=i+1
print()

import sys
print("Enter name:")
a=sys.stdin.readline()
print("Hello ",a)
