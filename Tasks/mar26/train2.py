import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib

df=pd.read_csv("house.csv")
df=df.replace({"yes":1,"no":0})

df=df.replace({
    "furnished":2,
    "semi-furnished":1,
    "unfurnished":0
})

x=df.drop(columns=["price"])
y=df["price"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

models={
    "Linear Regression":LinearRegression(),
    "Decision Tree":DecisionTreeRegressor(),
    "Random Forest":RandomForestRegressor()
}

best_model2=None
best_score=0
best_name=""

print("Model Performance:")

for name, model in models.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    score=r2_score(y_test,y_pred)

    print(f"{name}: {score}")

    if score>best_score:
        best_score=score
        best_model2=model
        best_name=name

print(f"Best Model: {best_name} ({best_score})")

joblib.dump(best_model2, "house_model.pkl")
print("Model saved as house_model.pkl")