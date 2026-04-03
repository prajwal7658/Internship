import tkinter as tk
import joblib

try:
    model=joblib.load("best_model1.pkl")
    vectorizer=joblib.load("vectorizer.pkl")
except:
    print("Please run train.py first")

def predict():
    message=entry.get()
    transformed=vectorizer.transform([message])
    prediction=model.predict(transformed)[0]

    result.configure(text=f"Prediction: {prediction}")

root=tk.Tk()
root.title("Email Spam Classifier")
root.geometry("400x300")

tk.Label(root,text="Enter email message",font=("Arial",14, "bold italic")).pack(pady=10)
entry=tk.Entry(root)
entry.pack(pady=10)

tk.Button(root,text="Predict",command=predict).pack(pady=10)

result=tk.Label(root,text="",font=("Arial",12))
result.pack()

root.mainloop()