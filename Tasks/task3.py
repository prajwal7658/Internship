l1=["apple", "banana", "cherry"]
l1.append("orange")
print(l1)
#['apple', 'banana', 'cherry', 'orange']

l1.insert(1,"mango")
print(l1)
#['apple', 'mango', 'banana', 'cherry', 'orange']

l1.extend(["kiwi","grape"])
print(l1)
#['apple', 'mango', 'banana', 'cherry', 'orange', 'kiwi', 'grape']




l2=[10,20,30,40,50]
l2[2]=300
print(l2)
#[10, 20, 300, 40, 50]

l2[1]=200
l2[2]=3000
l2[3]=400
print(l2)
#[10, 200, 3000, 400, 50]




l3=[1,2,3]
l3.insert(1,100)
print(l3)
#[1, 100, 2, 3]

l3[3]=999
print(l3)
#[1, 100, 2, 999]



l4=[10,20,30,40,50]
l4.append(60)
print(l4)
#[10, 20, 30, 40, 50, 60]

l4.insert(0,5)
print(l4)
#[5, 10, 20, 30, 40, 50, 60]

l4.extend([70,80,90])
print(l4)
#[5, 10, 20, 30, 40, 50, 60, 70, 80, 90]




l5=[42,3.14,"Hello",True]

l5[0]=2.718
print(l5)
#[2.718, 3.14, 'Hello', True]

l5.append(1000)
print(l5)
#[2.718, 3.14, 'Hello', True, 1000]

l5.insert(1,False)
print(l5)
#[2.718, False, 3.14, 'Hello', True, 1000]

l5[0]=5
del l5[1]
print(l5)
#[5, 3.14, 'Hello', True, 1000]




l6=["Cat", "Dog", "Lion", "Tiger", "Rabbit", "Monkey"]

print(l6[2:3])
#['Lion']

print(l6[-1:-3:-1])
#['Monkey', 'Rabbit']

print(l6[3:0:-1])
#['Tiger', 'Lion', 'Dog']

print(l6[::3])
#['Cat', 'Tiger']

print(l6[3::-3])
#['Tiger', 'Cat']

print(l6[-1::-3])
#['Monkey', 'Lion']

print(l6[-2::-2])
#['Rabbit', 'Lion', 'Cat']

print(l6[::-1])
#['Monkey', 'Rabbit', 'Tiger', 'Lion', 'Dog', 'Cat']





l7=[50,"apple",True,"car",40.5]

print(len(l7))
#5

l7[2]=False
print(l7)
#[50, 'apple', False, 'car', 40.5]

l7[1:3]=["kiwi","boat",20]
print(l7)
#[50, 'kiwi', 'boat', 20, 'car', 40.5]

l7[0]=5000
print(l7)
#[5000, 'kiwi', 'boat', 20, 'car', 40.5]

l7.remove(5000)
print(l7)
#['kiwi', 'boat', 20, 'car', 40.5]

l7.pop(1)
print(l7)
#['kiwi', 20, 'car', 40.5]

del l7[-1]
print(l7)
#['kiwi', 20, 'car']

l7.append(100)
print(l7)
#['kiwi', 20, 'car', 100]

l7.insert(0,"banana")
print(l7)
#['banana', 'kiwi', 20, 'car', 100]

l7.insert(3,30.5)
print(l7)
#['banana', 'kiwi', 20, 30.5, 'car', 100]

l7.clear()
print(l7)
#[]





l8=[50, -1, 2, 100, -6, -3, 67, 79, -55]

l8.reverse()
print(l8)
#[-55, 79, 67, -3, -6, 100, 2, -1, 50]

l8.sort()
print(l8)
#[-55, -6, -3, -1, 2, 50, 67, 79, 100]

l8.sort(reverse=True)
print(l8)
#[100, 79, 67, 50, 2, -1, -3, -6, -55]





















































































