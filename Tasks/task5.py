t1=(10,20,"Python","Code")
t2=("A","B")

print(t1[0])
#10

print(t2[-1])
#B

t=list(t1)
t[-1]="Program"
t1=tuple(t)
print(t1)
#(10, 20, 'Python', 'Program')

(a,b,c,d)=t1
print(a ,b ,c ,d)
#10 20 Python Program

t=t1+t2
print(t)
#(10, 20, 'Python', 'Program', 'A', 'B')

print(t[1:4])
#(20, 'Python', 'Program')

t1=(1,2,3)
t=t1*3
print(t)
#(1, 2, 3, 1, 2, 3, 1, 2, 3)

#*******************************************************************

my_set={10,20,30,40}

print(my_set)
#{40, 10, 20, 30}

print(20 in my_set)
#True

print(len(my_set))
#4

my_set.add(50)
print(my_set)
#{40, 10, 50, 20, 30}

my_set.remove(30)
print(my_set)
#{40, 10, 50, 20}

my_set.discard(20)
print(my_set)
#{40, 10, 50}

my_set.pop()
print(my_set)
#{10, 50}

for x in my_set:
    print(x)
#10 50

my_set.clear()
print(my_set)
#set()

#***********************************************************

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

s=set1.difference(set2)
print(s)
#{1, 2}

s=set1.symmetric_difference(set2)
print(s)
#{1, 2, 4, 5, 6}

set1.update(set2)
print(set1)
#{1, 2, 3, 4, 5, 6}
 
s=set1|set2
print(s)
#{1, 2, 3, 4, 5, 6}

set1.add(7)
print(set1)
#{1, 2, 3, 4, 5, 6, 7}

#***********************************************************
student = {
"name": "Anu",
"age": 20,
"course": "Python"
}

print(student.keys())
print(student.values())
print(student.items())
#dict_keys(['name', 'age', 'course'])
#dict_values(['Anu', 20, 'Python'])
#dict_items([('name', 'Anu'), ('age', 20), ('course', 'Python')])

print(student["name"])
#Anu

print(student.get("course"))
#Python

student["marks"] = 85
print(student)
#{'name': 'Anu', 'age': 20, 'course': 'Python', 'marks': 85}

student["age"] = 21
print(student)
#{'name': 'Anu', 'age': 21, 'course': 'Python', 'marks': 85}

student.pop("course")
print(student)
#{'name': 'Anu', 'age': 21, 'marks': 85}

student.popitem()
print(student)
#{'name': 'Anu', 'age': 21}

for key, value in student.items():
    print(key, "-",value)
#name - Anu
#age - 21

#*********************************************************************
students = {
"student1": {"name": "Anu", "age": 20},
"student2": {"name": "Ravi", "age": 21}
}

print(students)
#{'student1': {'name': 'Anu', 'age': 20}, 'student2': {'name': 'Ravi', 'age': 21}}

c=students.copy()
print(c)
#{'student1': {'name': 'Anu', 'age': 20}, 'student2': {'name': 'Ravi', 'age': 21}}

#*********************************************************************
employee = {
"emp_id": 101,
"name": "Kiran",
"department": "HR",
"salary": 35000
}

print(employee.keys())
#dict_keys(['emp_id', 'name', 'department', 'salary'])

print(employee.values())
#dict_values([101, 'Kiran', 'HR', 35000])

print(employee.items())
#dict_items([('emp_id', 101), ('name', 'Kiran'), ('department', 'HR'), ('salary', 35000)])

print(employee["name"])
#Kiran

employee["salary"]=40000
print(employee["salary"])
#40000
























