import tkinter as tk
import joblib
import pandas as pd

try:
    model=joblib.load("best_model.pkl")
except:
    print("Please run train.py first")
    
df=pd.read_csv("iris.csv")

def predict():
    values=[
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get())
            ]
    
    prediction=model.predict([values])[0]
    result.configure(text=f"Prediction: {prediction}")

root=tk.Tk()
root.title("Iris Prediction App")
root.geometry("350x400")

tk.Label(root,text="Enter Iris Features",font=("Arial",14,"bold italic")).pack(pady=5)
labels=["Sepal Length","Sepal Width","Petal Length","Petal Width"]
entries=[]

for label in labels:
    tk.Label(root,text=label).pack()
    entry=tk.Entry(root)
    entry.pack()
    entries.append(entry)
    
entry1, entry2, entry3, entry4=entries 

tk.Button(root,text="Predict",command=predict).pack(pady=10)

result=tk.Label(root,text="",font=("Arial",12))
result.pack()

root.mainloop()