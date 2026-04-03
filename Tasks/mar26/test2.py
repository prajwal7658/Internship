import tkinter as tk
import joblib

try:
    model=joblib.load("house_model.pkl")
except:
    print("Run train2.py first")

def predict():
    values=[
        float(area.get()),
        int(bed.get()),
        int(bath.get()),
        int(stories.get()),
        int(mainroad.get()),
        int(guest.get()),
        int(basement.get()),
        int(hotwater.get()),
        int(ac.get()),
        int(parking.get()),
        int(pref.get()),
        int(furnish.get())
    ]

    prediction=model.predict([values])[0]
    result.config(text=f"Estimated Price: {int(prediction)}")

root = tk.Tk()
root.title("House Price Prediction")
root.geometry("400x700")

tk.Label(root, text="Area").pack()
area = tk.Entry(root)
area.pack()

tk.Label(root, text="Bedrooms").pack()
bed = tk.Entry(root)
bed.pack()

tk.Label(root, text="Bathrooms").pack()
bath = tk.Entry(root)
bath.pack()

tk.Label(root, text="Stories").pack()
stories = tk.Entry(root)
stories.pack()

tk.Label(root, text="Mainroad (1/0)").pack()
mainroad = tk.Entry(root)
mainroad.pack()

tk.Label(root, text="Guestroom (1/0)").pack()
guest = tk.Entry(root)
guest.pack()

tk.Label(root, text="Basement (1/0)").pack()
basement = tk.Entry(root)
basement.pack()

tk.Label(root, text="Hotwater (1/0)").pack()
hotwater = tk.Entry(root)
hotwater.pack()

tk.Label(root, text="Airconditioning (1/0)").pack()
ac = tk.Entry(root)
ac.pack()

tk.Label(root, text="Parking").pack()
parking = tk.Entry(root)
parking.pack()

tk.Label(root, text="Prefarea (1/0)").pack()
pref = tk.Entry(root)
pref.pack()

tk.Label(root,text="Furnishing (2/1/0)").pack()
furnish=tk.Entry(root)
furnish.pack()

tk.Button(root,text="Predict Price",command=predict).pack(pady=10)

result=tk.Label(root,text="",font=("Arial",12))
result.pack()

root.mainloop()