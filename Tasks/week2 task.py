###1
##def calculate_bill(units):
##    if units<=100:
##        return units
##    elif units>100 and units<=200:
##        return units*2
##    else:
##        return units*3
##
##price=int(input("Enter your electricity unit: "))
##calculate_bill(price)
##print("Amount is ",calculate_bill(price), "Rs" )





###2
##def check_password(password):
##    digit=False
##    sc=False
##
##    special="!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"
##    if len(password)>=8:
##        for i in password:
##            if i.isdigit():
##                digit=True
##            if i in special:
##                sc=True
##
##        if digit and sc:
##            print("The password is strong")
##        else:
##            print("Not strong..add special char or digit")
##    else:
##        print("Weak password..length must be greater than 8")
##
##check_password("Hello@123")
##check_password("12345")
##check_password("Prajwal123")


###3
##def Rev(number):
##    rev=0
##    while number>0:
##        rem=number%10
##        rev=rev*10+rem
##        number=number//10
##    return rev
##
##reverse=Rev(int(input("Enter a number :")))
##print("The reveresed number is :",reverse)
##
##
##
###4
##st=input("Enter a string :")
##
##count=0
##for i in st:
##    if i in "aeiouAEIOU":
##        count+=1
##print("Number of vowels is :",count)



###5
##def Bank(balance,widtdraw_amount):
##    print("Original balance :",balance)
##    if widtdraw_amount>=100:
##        if widtdraw_amount%100==0 and widtdraw_amount<=balance:
##            print(f"Widtdraw of amount {widtdraw_amount} succesfull ")
##            balance=balance-widtdraw_amount
##            print("The remaining balance is ",balance)
##            print()
##        else:
##            print("Unable to widtdraw\n")
##    else:
##        print("Please enter amount greater than or equal to 100.\n")
##
##Bank(1000,500)
##Bank(1000,2000)




###6
##def Marks(marks):
##    if marks>=90 and marks<=100:
##        print("Grade is A .Excellent")
##    elif marks<90 and marks>=75:
##        print("Grade is B .Very good")
##    elif marks>=60 and marks<75:
##        print("Grade is C .Good")
##    else:
##        print("Fail")
##
##Marks(93)
##Marks(34)
    



###7
##class Mobile:
##    def __init__(self,brand,model,price):
##        self.brand=brand
##        self.model=model
##        self.price=price
##
##    def display(self):
##        print("Brand is ",self.brand)
##        print("model is ",self.model)
##        print("price is ",self.price)
##        print()
##
##c1=Mobile("Samsung","S25",750000)
##c2=Mobile("Apple","17 pro",120000)
##    
##c1.display()
##c2.display()




###8
##class Employee:
##    def __init__(self,name,eid):
##        self.name=name
##        self.eid=eid
##
##class Permenent(Employee):
##    def __init__(self,name,eid,salary):
##        Employee.__init__(self,name,eid)
##        self.salary=salary
##
##    def show(self):
##        print("Name is ",self.name)
##        print("Employee id is ",self.eid)
##        print("Salary is ",self.salary)
##
##e1=Permenent("Prajwal",10,30000)
##e1.show()




###9
##def palindrome(n):
##    temp=n
##    rev=0
##    while n>0:
##        rem=n%10
##        rev=rev*10+rem
##        n=n//10
##
##    if temp==rev:
##        print("Number is Palindrome\n")
##    else:
##        print("Number is Not Palindrome\n")
##
##def palindromeStr(s):
##    reve=s[::-1]
##    if s==reve:
##        print("String is Palindrome\n")
##    else:
##        print("String is Not Palindrome\n")
##
##
##val=input("Enter a number or string: ")
##
##if val.isdigit():
##    palindrome(int(val))
##else:
##    palindromeStr(val)













