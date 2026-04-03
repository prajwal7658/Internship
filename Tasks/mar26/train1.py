import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv("email.csv")

x = df["Message"]
y = df["Category"]

vect=TfidfVectorizer()
x = vect.fit_transform(x)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)

models={
    "KNN":KNeighborsClassifier(),
    "SVM":SVC(),
    "Decision Tree":DecisionTreeClassifier()
}

best_model1=None
best_accuracy1=0
best_name1=""

print("Model Accuracy:")

for name, model in models.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)

    print(f"{name}: {accuracy*100}%")

    if accuracy > best_accuracy1:
        best_accuracy1=accuracy
        best_model1=model
        best_name1=name

print(f"Best Model: {best_name1} ({best_accuracy1 * 100}%)")

joblib.dump(best_model1,"best_model1.pkl")
joblib.dump(vect,"vectorizer.pkl")

print("Model and vectorizer saved")