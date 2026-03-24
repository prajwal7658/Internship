####TASK 1:
##print("-----------------------TASK 1-------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##subjects=[]
##hours=[]
##
##n=int(input("Enter number of subjects: "))
##
##for i in range(n):
##    sub=input("Enter subject name: ")
##    subjects.append(sub)
##    
##    hr=float(input("Enter hours studied: "))
##    hours.append(hr)
##
##df=pd.DataFrame({"Subject": subjects,
##                 "Hours": hours
##                 })
##
##total=np.sum(hours)
##avg=np.mean(hours)
##
##print("Total study time:", total)
##print("Average study time:", avg)
##
##plt.bar(subjects,hours)
##plt.title("Study time per subject")
##plt.xlabel("Subjects")
##plt.ylabel("Hours")
##plt.show()
##
##
##
####TASK 2:
##print("-----------------------TASK 2-------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##food=[]
##calories=[]
##
##n=int(input("Enter number of food items: "))
##
##for i in range(n):
##    f=input("Enter food item: ")
##    food.append(f)
##    
##    c=int(input("Enter calories: "))
##    calories.append(c)
##
##df=pd.DataFrame({"Food": food,
##                 "Calories": calories
##                 })
##
##total=np.sum(calories)
##
##print("Total calories:", total)
##
##plt.pie(calories,labels=food,autopct='%1.1f%%')
##plt.title("Calorie distribution")
##plt.show()
##
##
##
####TASK 3:
##print("-----------------------TASK 3-------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##products=[]
##quantity=[]
##
##n=int(input("Enter number of products: "))
##
##for i in range(n):
##    p=input("Enter product name: ")
##    products.append(p)
##    
##    q=int(input("Enter quantity: "))
##    quantity.append(q)
##
##df=pd.DataFrame({"Product": products,
##                 "Quantity": quantity
##                 })
##
##total=np.sum(quantity)
##
##print("Total stock:", total)
##
##plt.bar(products,quantity)
##plt.title("Stock levels")
##plt.xlabel("Products")
##plt.ylabel("Quantity")
##plt.show()
##
##
##
####TASK 4:
##print("-----------------------TASK 4-------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##num=list(map(int,input("Enter numbers separated by space: ").split()))
##
##df=pd.DataFrame({"Numbers": num})
##
##print("Max:", np.max(num))
##print("Min:", np.min(num))
##print("Average:", np.mean(num))
##
##plt.plot(num,marker='o')
##plt.title("Number comparison")
##plt.xlabel("Index")
##plt.ylabel("Value")
##plt.show()
##
##
##
##
####TASK 5:
##print("-----------------------TASK 5-------------------------")
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##players=[]
##scores=[]
##
##n=int(input("Enter number of players: "))
##
##for i in range(n):
##    name=input("Enter player name: ")
##    players.append(name)
##    
##    score=int(input("Enter score: "))
##    scores.append(score)
##
##df=pd.DataFrame({"Player":players,
##                 "Score":scores
##                 })
##
##print("Highest score:",np.max(scores))
##
##plt.bar(players,scores)
##plt.title("Player scores")
##plt.xlabel("Players")
##plt.ylabel("Scores")
##plt.show()




##TASK 6:
print("-----------------------TASK 6-------------------------")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hours=[]
vehicles=[]

n=int(input("Enter number of hours: "))

for i in range(n):
    h=input("Enter hour: ")
    hours.append(h)  
    v=int(input("Enter vehicle count: "))
    vehicles.append(v)

df=pd.DataFrame({"Hour": hours,
                 "Vehicles": vehicles
                 })

peak=hours[np.argmax(vehicles)]
print("Peak traffic time:", peak)

plt.plot(hours,vehicles,marker='o')
plt.title("Traffic analysis")
plt.xlabel("Hours")
plt.ylabel("Vehicle count")
plt.show()





##Accuracy=(TP+TN)/(TP+TN+FP+FN)
##Precision=TP/(TP+FP)
##Recall=TP/(TP+FN)
##F1 Score=2×(Precision×Recall)/(Precision+Recall)
##
##
##1:
##TP=50,FN=10,FP=5,TN=35
##
##Accuracy=(50+35)/(50+35+10+5)=0.85
##Precision=50/(50+5)=0.91
##Recall=50/(50+10)=0.83
##F1 Score=0.87
##
##
##
##
##2:
##Correct=40+30+40=110
##Total=150
##Accuracy=110/150=0.73
##
##A:
##TP=40
##FP=10+5=15
##FN=5+5=10
##
##Precision=40/(40+15)=0.73
##Recall=40/(40+10)=0.80
##F1Score=0.76
##
##B:
##TP=30
##FP=5+5=10
##FN=10+10=20
##
##Precision=30/(30+10)=0.75
##Recall=30/(30+20)=0.60
##F1Score=0.67
##
##C:
##TP=40
##FP=5+10=15
##FN=5+5=10
##
##Precision=40/(40+15)=0.73
##Recall=40/(40+10)=0.80
##F1Score=0.76
##
##
##
##3:
##TP=20,FN=80,FP=10,TN=890
##
##Accuracy=(20+890)/1000=0.91
##Precision=20/(20+10)=0.67
##Recall=20/(20+80)=0.20
##F1Score=0.31
##
##
##4:
##TP=45,FN=5,FP=15TN=35
##,
##Accuracy=(45+35)/100=0.80
##Precision=45/(45+15)=0.75
##Recall=45/(45+5)=0.90
##F1Score=0.82









