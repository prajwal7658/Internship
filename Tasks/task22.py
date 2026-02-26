TASK 1
import seaborn as sns
data=sns.load_dataset("tips")
print(data)


TASK 2a
import matplotlib.pyplot as plt

d=sns.load_dataset("tips")
sns.scatterplot(x='total_bill',y='tip',hue='sex',data=d)

plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()


TASK 2b
d=sns.load_dataset("tips")
sns.lineplot(x='day',y='tip',data=d)

plt.title("Average tip per day")
plt.xlabel("Day")
plt.ylabel("Average tip")
plt.show()


TASK 2c
d=sns.load_dataset("tips")
sns.barplot(x='day',y='total_bill',data=d)

plt.title("Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()


TASK 2d
d=sns.load_dataset("tips")
sns.histplot(d['total_bill'],bins=10,kde=True)

plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()



TASK 3
d=sns.load_dataset('iris')
plt.figure(figsize=(6,8))

plt.subplot(2,1,1)
sns.scatterplot(x='sepal_length',y='sepal_width',hue='species',data=d)
plt.title("Iris sepal length vs Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal width")

plt.subplot(2,1,2)
sns.scatterplot(x='petal_length',y='petal_width',hue='species',data=d)
plt.title("Iris petal length vs petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.tight_layout()
plt.show()


TASK 4
d=sns.load_dataset("tips")
num=d.select_dtypes(include=['number'])

cor=num.corr()
sns.heatmap(cor,annot=True,cmap="coolwarm",linewidth=1)

plt.title("Correlation Heatmap")
plt.show()


TASK 5
d=sns.load_dataset('titanic')

Plot survival count
plt.figure()
sns.countplot(x='survived',data=d)
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

Plot age distribution
plt.figure()
sns.histplot(d['age'],bins=10,kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

Plot survival by gender
plt.figure()
sns.countplot(x='sex',hue='survived',data=d)
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

Create heatmap
num=d.select_dtypes(include=['number'])
cor=num.corr()

plt.figure()
sns.heatmap(cor,annot=True,cmap="coolwarm",linewidth=1)
plt.title("Titanic Correlation Heatmap")
plt.show()



PILLOW TASK

TASK 1:
from PIL import Image
i=Image.open("C:\\Users\\Hp\\Desktop\\Internship Program\\task\\car.jpeg")
i.show()

TASK 2:
i.show()

print("Image Format :", i.format)
print("Image Size   :", i.size)
print("Image Mode   :", i.mode)

TASK 3:
resized=i.resize((300,300))
resized.show()

TASK 4:
gray=i.convert("L")
gray.show()

TASK 5:
bw=i.convert("1")
bw.show()

TASK 6:
rotated=i.rotate(90)
rotated.show()

TASK 7:
cropped=i.crop((50,50,300,300))
cropped.show()

TASK 8:
resized=i.resize((300,300))
resized.save("new_car.jpg")
print("Saved ")

TASK 9:
i.thumbnail((150,150))
i.show()

TASK 10:
from PIL import Image, ImageFilter
blur=i.filter(ImageFilter.BLUR)
blur.show()

TASK 11:
sharp=i.filter(ImageFilter.SHARPEN)
sharp.show()

TASK 12:
edge=i.filter(ImageFilter.FIND_EDGES)
edge.show()

TASK 13:
resized=i.resize((200,200))
resized.show()

gray=resized.convert("L")
gray.show()

rotated=gray.rotate(90)
rotated.show()

rotated.save("final_output.jpg")















