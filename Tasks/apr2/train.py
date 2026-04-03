import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

df=pd.read_csv("iris.csv")

x=df.drop(columns=["Id","Species"])
y=df["Species"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

models={
"KNN":KNeighborsClassifier(),
"SVM":SVC(),
"Decision Tree":DecisionTreeClassifier(),
"Random Forest":RandomForestClassifier()
}

best_model=None
best_accuracy=0
best_name=""

print("Model Accuracy:\n")

for name,model in models.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)

    print(f"{name}:{accuracy*100:.2f}%")

    if accuracy>best_accuracy:
        best_accuracy=accuracy
        best_model=model
        best_name=name

print(f"\nBest Model:{best_name}({best_accuracy*100:.2f}%)")

joblib.dump(best_model,"best_model.pkl")
print("Model saved as best_model.pkl")