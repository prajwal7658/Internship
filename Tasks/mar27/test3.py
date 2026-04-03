import tkinter as tk
import joblib

try:
    model=joblib.load("diabetes_model.pkl")
except:
    print("Run train.py first")

def predict():
        values=[
            int(prg.get()),
            int(glc.get()),
            int(bp.get()),
            int(st.get()),
            int(ins.get()),
            float(bmi.get()),
            float(dpf.get()),
            int(age.get())
        ]

        prediction=model.predict([values])[0]

        if prediction==1:
            result.configure(text="Diabetic")
        else:
            result.configure(text="Not Diabetic")


root=tk.Tk()
root.title("Diabetes Prediction")
root.geometry("400x500")

tk.Label(root,text="Enter Patient Details",font=("Arial",14,"bold italic")).pack(pady=5)

tk.Label(root,text="Pregnancies").pack()
prg=tk.Entry(root)
prg.pack()

tk.Label(root,text="Glucose").pack()
glc=tk.Entry(root)
glc.pack()

tk.Label(root,text="Blood Pressure").pack()
bp=tk.Entry(root)
bp.pack()

tk.Label(root,text="Skin Thickness").pack()
st=tk.Entry(root)
st.pack()

tk.Label(root,text="Insulin").pack()
ins=tk.Entry(root)
ins.pack()

tk.Label(root,text="BMI").pack()
bmi=tk.Entry(root)
bmi.pack()

tk.Label(root,text="Diabetes Pedigree Function").pack()
dpf=tk.Entry(root)
dpf.pack()

tk.Label(root,text="Age").pack()
age=tk.Entry(root)
age.pack()

tk.Button(root,text="Predict",command=predict).pack(pady=10)

result=tk.Label(root,text="",font=("Arial",12))
result.pack()

root.mainloop()