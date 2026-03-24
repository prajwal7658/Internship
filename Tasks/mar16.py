# m=[[2,4,6],
#    [1,3,5],
#    [7,9,8]
#    ]
# print(m)
# print()

# print(m[1][2],m[0][2])
# print()

# m[2][0]=700
# print(m)
# print()

# s=0
# for r in m:
#     for c in r:
#         s=s+c
# print(s)
# print()

# d=[m[i][i] for i in range(len(m))]
# print(d)
#------------------------------------------------------------


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score

# df=pd.read_csv("iris.csv")
# x=df.drop(columns=["Species"])
# y=df["Species"]

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# knn=KNeighborsClassifier(n_neighbors=5)
# knn.fit(x_train,y_train)

# y_pred=knn.predict(x_test)
# accuracy=accuracy_score(y_test,y_pred)
# print(accuracy*100)

# y_p=knn.predict([[151,1.5,2.5,4.6,3.5]])
# print(y_p)


import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

data=load_wine()

x=data.data
y=data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)

accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy*100)

y_p=knn.predict([[13.2,2.7,2.4,15.0,100,2.5,2.3,0.3,1.7,5.0,1.0,3.0,1000]])
print("Prediction:", y_p)

