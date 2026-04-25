import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import json
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("bone.h5")

with open("labels.json", "r") as f:
    class_indices = json.load(f)

labels = [None] * len(class_indices)
for key, value in class_indices.items():
    labels[value] = key

img_path = ""

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    result = model.predict(img)
    idx = np.argmax(result)

    return labels[idx]

def open_image():
    global img_path, panel

    img_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    if not img_path:
        return

    try:
        img = Image.open(img_path)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)

        panel.config(image=img_tk)
        panel.image = img_tk

        result.config(text="")
    except Exception as e:
        messagebox.showerror("Error", f"Cannot open image:\n{e}")

def classify():
    if img_path:
        try:
            label = predict_image(img_path)
            result.config(text=f"Prediction: {label}")
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed:\n{e}")
    else:
        messagebox.showwarning("Warning", "Please load an image first")

root = tk.Tk()
root.title("Bone breakage")
root.geometry('400x500')

panel = tk.Label(root)
panel.pack(pady=10)

btn_load = tk.Button(root, text="Load Image", command=open_image)
btn_load.pack(pady=10)

btn_predict = tk.Button(root, text='Classify', command=classify)
btn_predict.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 20))
result.pack(pady=20)

root.mainloop()