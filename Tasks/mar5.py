print("----------------------TASK 1----------------------")
n=5
for i in range(1,n+1):
    print("*"*i)    
print()    


print("----------------------TASK 2----------------------")
n=4
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))
print()



print("----------------------TASK 3----------------------")
n=5
for i in range(n):
    print("*"*n)
print()



print("----------------------TASK 4----------------------")
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()
print()



print("----------------------TASK 5----------------------")
n=4
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for j in range(n-1,0,-1):
    print(" "*(n-j)+"*"*(2*j-1))
print()



print("----------------------TASK 6----------------------")
n=5
x=1
for i in range(n):
    for j in range(i+1):
        print(x,end=" ")
        x+=1
    print()
print()



print("----------------------TASK 7----------------------")
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
print()



print("----------------------TASK 8----------------------")
n=5
for i in range(n):
    x=1
    for j in range(n-i):
        print(" ",end="")
        
    for k in range(i+1):
        if k==0 or k==i:
            print(1,end=" ")
        else:
            x=x*(i-k+1)//k
            print(x,end=" ")
    print()
print()



print("----------------------TASK 9----------------------")
n=5
for i in range(1,n+1):
    x=i%2
    
    for j in range(1,i+1):
        print(x,end="")
        x=1-x 

    print()
print()



print("----------------------TASK 10----------------------")
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end=" ")
    print()
