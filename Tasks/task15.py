####TASK 1:
##import numpy as np
##
##salary=[25000,30000,28000,32000,29000,31000,27000,35000,26000]
##
##print("#1.Create a NumPy 1D array using the given list.")
##a=np.array(salary)
##print("1D Array :",a)
##print()
##
##print("#2.Convert it into a 2D array with 3 rows and 3 columns.")
##b=a.reshape(3,3)
##print("2D array :\n",b)
##print()
##
##print("#3.Find shape,data type,salary at row 2 column 1")
##print("shape: ",b.shape)
##print("datatype:", b.dtype)
##print("row 2 column 1:", b[1,0])
##print()
##
##print("#4.Slicing")
##print("index 2 to 6 :",a[2:7])
##print("last 3 elements:",a[-3:])
##print()
##
##print("#5.Sorting")
##print("ascending:", np.sort(a))
##print("descending:", np.sort(a)[::-1])
##print()
##
##print("#6.Reshape back to 1D")
##print("reshaped to 1D:", b.reshape(-1))
##print()
##
##print("#7.Concatenate with bonus")
##bonus=[2000,3000,2500,4000,1500,3500,2800,5000,1800]
##c=np.array(bonus)
##joined=np.concatenate((a,c))
##print("Concatenated:", joined)
##print()



#### TASK 2:
##import numpy as np
##
##stock=[45,60,30,80,55,90,20,70]
##a=np.array(stock)
##
##print("#1:create arrays")
##zero=np.zeros(8)
##one=np.ones(8)
##range=np.arange(10,50,5)
##print(zero, one, range)
##print()
##
##print("#2:Convert to 2d")
##b=a.reshape(4,2)
##print(b)
##print()
##
##print("#3:Access elements")
##element=b[2,0]
##first=b[0]
##print(element, first)
##print()
##
##print("#4:Slicing")
##s1=a[1:6]
##s2=a[-4:-1]
##print(s1, s2)
##print()
##
##print("#5:Search")
##ind=np.where(a==90)
##great=a[a>50]
##print(ind, great)
##print()
##
##print("#6:Split")
##sp=np.split(a,4)
##hs=np.hsplit(b,2)
##vs=np.vsplit(b,2)
##print(sp, hs, vs)
##print()



####TASK 3:
##import numpy as np
##temp=[30,32,31,29,35,36,33,34,28,27,26,25]
##a=np.array(temp)
##print("#1: Create 1d array")
##print(a)
##print()
##
##print("#2: Convert to 3d")
##b=a.reshape(2,2,3)
##print(b)
##print()
##
##print("#3: Access")
##value=b[0,1,2]
##print(value)
##print()
##
##print("#4: Check datatype and change to float")
##print("before:", a.dtype)
##a=a.astype(float)
##print("after:", a.dtype)
##print()
##
##print("#5: Slicing")
##s1=a[3:9]
##s2=a[::2]
##print(s1)
##print(s2)
##print()
##
##print("#6: Sorting")
##asc=np.sort(a)
##desc=np.sort(a)[::-1]
##print(asc)
##print(desc)
##print()
##
##print("#7: Reshape into 4x3 matrix")
##reshaped=a.reshape(4,3)
##print(reshaped)
##print()



##TASK 4:
import numpy as np
rollno=[101,102,103,104,105,106,107,108,109,110]
roll=np.array(rollno)
print("#1: array from 101 to 111")
a=np.arange(101,111)
print(a)
print()
print("#2: Create zeros and ones arrays")
zero=np.zeros(10)
one=np.ones(10)
print(zero)
print(one)
print()
print("#3: Convert rollnumber to 2d array(5x2)")
b=roll.reshape(5,2)
print(b)
print()
print("#4: Join rn with extra_roll")
extra_roll=np.array([111,112,113,114,115])
joined = np.concatenate((roll,extra_roll))
print(joined)
print()
print("#5: Search operations")
arr=roll
index=np.where(arr==105)
great=arr[arr>107]
print("Index of 105:", index)
print("Greater than 107:", great)
print()
print("#6: Split joined array into 3 equal parts")
sp=np.split(joined,3)
print(sp)
print()

print("#7: Check shape before and after reshaping")
original=roll
print("Before:", original.shape)
reshaped=original.reshape(2,5)
print("After:", reshaped.shape)
print()



