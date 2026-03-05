##TASK 1:
##PART 1:
import cv2

img=cv2.imread("student_id.jpg")

cv2.imwrite("backup.jpg",img)

resized=cv2.resize(img,(300,300))
print("Image resized to 300x300")

crop=resized[50:200,80:220]
cv2.imshow("Cropped Region",crop)
print("Cropped region displayed")

gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
print("Converted to grayscale")

hsv=cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)
print("Converted to HSV")

blur=cv2.GaussianBlur(resized,(7,7),0)
print("Blur Applied")

cv2.imshow("Original",resized)
cv2.imshow("Gray Image",gray)
cv2.imshow("HSV Image",hsv)
cv2.imshow("Blurred Image",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()


##PART 2:
import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()   
    if not ret:
        print("Failed")
        break
    cv2.imshow("Camera",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#############################################################

TASK 2:
PART 1:
import pyautogui as gui
import time

print("Opening Calculator")
gui.hotkey('win','r')
time.sleep(2)

gui.write('calc')

gui.press('enter')
time.sleep(2)
print("Calculator Opened")


##PART 2:
gui.write("1234+5678")
gui.press("enter")

time.sleep(2)

result=gui.screenshot(region=(500,300,400,200))
result.save("calculator.png")


##PART 3:
print("Mouse movement started")
gui.moveTo(300,300,duration=1)

gui.click()
gui.doubleClick()
gui.rightClick()
print("Click actions completed")

gui.dragTo(600,400,duration=2)
print("Drag operation completed")


##PART 4:
gui.hotkey('win','r')
time.sleep(1)

gui.write("notepad")
gui.press("enter")

time.sleep(2)

gui.write("Daily automation report generated")
gui.press("enter")

gui.write("03-03-2026")

gui.hotkey("ctrl","s")
time.sleep(1)

gui.write("report.txt")
gui.press("enter")


##PART 5:
print("Capturing full screen...")

full=gui.screenshot()
full.save("full.png")

print("Full screen captured")

part=gui.screenshot(region=(100,100,600,400))
part.save("part.png")

print("Partial screen captured")
print("Screenshots saved successfully")















