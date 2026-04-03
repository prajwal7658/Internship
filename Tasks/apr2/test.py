import tkinter as tk
import joblib
import pandas as pd

try:
    model=joblib.load("best_model.pkl")
except:
    print("Please run train.py first")

df=pd.read_csv("iris.csv")

def predict():
    try:
        values=[
        float(sl.get()),
        float(sw.get()),
        float(pl.get()),
        float(pw.get())
        ]

        prediction=model.predict([values])[0]
        result.config(text=f"Prediction:{prediction}",fg="green")

    except:
        result.config(text="Enter valid values",fg="red")


root=tk.Tk()
root.title("Iris Prediction")
root.geometry("400x450")
root.configure(bg="black")

tk.Label(root,text="Iris Flower Predictor",font=("Arial",16,"bold"),bg="black",fg="white").pack(pady=10)

tk.Label(root,text="Sepal Length",font=("Arial",11),bg="black",fg="white").pack()
sl=tk.Entry(root,font=("Arial",11))
sl.pack(pady=5)

tk.Label(root,text="Sepal Width",font=("Arial",11),bg="black",fg="white").pack()
sw=tk.Entry(root,font=("Arial",11))
sw.pack(pady=5)

tk.Label(root,text="Petal Length",font=("Arial",11),bg="black",fg="white").pack()
pl=tk.Entry(root,font=("Arial",11))
pl.pack(pady=5)

tk.Label(root,text="Petal Width",font=("Arial",11),bg="black",fg="white").pack()
pw=tk.Entry(root,font=("Arial",11))
pw.pack(pady=5)

tk.Button(root,text="Predict",command=predict,bg="green",fg="white",font=("Arial",12,"bold"),padx=10,pady=5).pack(pady=15)

result=tk.Label(root,text="",font=("Arial",12,"bold"),bg="black",fg="yellow")
result.pack()
root.mainloop()