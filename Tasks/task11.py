##import os
##
##name=input("Enter Customer Name: ")
##
###1.When a customer comes, the computer creates a new bill file .
##file=open("bill.txt","w")
##file.write(f"Costumer :{name}\n")
##file.close()
##
###2.It writes the customer details and first order .
##print("Bill created succesfully\n")
##
###3.If the customer orders more items, it adds them to the same bill .
##file=open("bill.txt","a")
##file.write("Latte - 2 cups - 200\n")
##file.write("Sandwich - 1 - 80\n")
##file.close()
##
##print("Item added successfully")
##print()
##
###4.When the customer wants to see the bill, the computer reads the file .
##file=open("bill.txt", "r")
##data=file.read()
##print(data)
##file.close()
##
###5.If the order is cancelled, the bill file is deleted .
##cancel=input("Cancel Order? (yes or no): ")
##if cancel=="yes":
##    os.remove("bill.txt")
##    print("Order cancelled")
##    print("Bill deleted successfully")



###1.Write a program to create a text file and write a message into it.
##f=open("test.txt", "w")
##f.write("Hello, Iam Prajwal. This is my text file")
##f.close()
##
###2 Open a file in read mode and display its contents.
##f=open("test.txt", "r")
##data=f.read()
##print(data)
##f.close()
##
###3.Write a program to append data to an existing file.
##f=open("test.txt", "a")
##f.write("\nThis line is appended.")
##f.close()
##
###4.Readafile and display each line.
##f=open("test.txt", "r")
##print("\nReading line by line:")
##print(f.readline())
##print(f.readline())
##f.close()



##class Shape:
##    def area(self):
##        print("Area")
##
##class Rectangle(Shape):
##    def area(self):
##        print("Area of rectangle is l*b")
##
##s=Shape()
##r=Rectangle()
##
##s.area()
##r.area()


##class Movie:
##    def __init__(self,title,rating):
##        self.title=title
##        self.rating=rating
##
##    def Check(self):
##        if self.rating>=8:
##            print(self.title,"Hit movie")
##        else:
##            print(self.title,"Average movie")
##
##
##m1=Movie("ABC", 8.5)
##m2=Movie("XYZ", 6)
##
##m1.Check()
##m2.Check()



##class BookStore:
##    def __init__(self,book_name,price):
##        self.book_name=book_name
##        self.price=price
##
##    def discount(self):
##        if self.price>500:
##            final_price=self.price-(self.price*0.10)
##            print(self.book_name, "Price after discount:",final_price)
##        else:
##            print(self.book_name, "No discount. Price:",self.price)
##
##
##b1=BookStore("Dinga",600)
##b2=BookStore("Baala mangala",400)
##
##b1.discount()
##b2.discount()


##class Account:
##    def __init__(self):
##        self.__password=""
##
##    def set(self,password):
##        if len(password)>6:
##            self.__password=password
##            print("Password is set")
##        else:
##            print("Password is short")
##
##    def validate(self):
##        if self.__password=="":
##            print("No password set")
##        else:
##            print("Valid")
##
##
##a=Account()
##a.set("Prajwal123")
##a.validate()


##class TempControl:
##    def __init__(self):
##        self.__temp=0
##
##    def set_temp(self,temp):
##        if temp >= 16 and temp <= 30:
##            self.__temp=temp
##            print("Temperature set: ",self.__temp)
##        else:
##            print("Invalid temperature\n")
##
##    def show_temp(self):
##        print("Current temperature: ",self.__temp)
##
##
##t = TempControl()
##t.set_temp(30)
##t.set_temp(70)
##t.show_temp()



##class ElectronicItem:
##    def __init__(self,brand):
##        self.brand = brand
##
##
##class WashingMachine(ElectronicItem):
##    def __init__(self,brand,capacity):
##        super().__init__(brand)
##        self.capacity=capacity
##
##    def display(self):
##        print("Brand: ",self.brand)
##        print("Capacity: ",self.capacity,"kg")
##
##w = WashingMachine("LG",7)
##w.display()


class AudioPlayer:
    def audio(self):
        print("Playing audio...")


class VideoPlayer:
    def video(self):
        print("Playing video")


class SmartPlayer(AudioPlayer,VideoPlayer):
    pass


s=SmartPlayer()

s.audio()
s.video()

























