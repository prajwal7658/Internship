from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog
import cv2

model = YOLO('best.pt')

def upload_and_detect():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image files","*.jpg *jpeg *.png")]
    )
    
    if not file_path:
        return
    
    img=cv2.imread(file_path)
    results=model(img)
    
    annotated=results[0].plot()
    
    cv2.imshow("Pothole Detection",annotated)
    cv2.waitKey()
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("Pothole Detection")

tk.Label(root, text = "Road Pothole Detection").pack()

btn = tk.Button(root, text = "upload Image", command = upload_and_detect)

btn.pack(pady = 30)
root.mainloop()


# from ultralytics import YOLO
# import tkinter as tk
# from tkinter import filedialog
# import cv2

# model = YOLO('best.pt')

# def start_camera():
#     cap=cv2.VideoCapture(0)
#     while True:
#         ret,frame=cap.read()
#         if not ret:
#             break
        
#         results=model(frame)
#         annotated=results[0].plot()
#         cv2.imshow("Pothole Detection",annotated)
#         if cv2.waitKey(1) & 0xFF==ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# root = tk.Tk()
# root.title("Pothole Detection")

# tk.Label(root, text = "Road Pothole Detection").pack()

# btn = tk.Button(root, text = "upload Image", command = start_camera)

# btn.pack(pady = 30)

# root.mainloop()