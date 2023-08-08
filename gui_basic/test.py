import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry("720x720")
root.config(bg="black")

Label(root, text="Lockruto", font=("arial", 30, "bold"), bg="black", fg="green").pack()

frame1 = LabelFrame(root, bg="green")
frame1.pack()

label1 = Label(frame1, bg="green")
label1.pack()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if ret:
        try:
            img = ImageTk.PhotoImage(Image.fromarray(img))
        except:
            root.quit()
            break
        label1['image'] = img
    else:
        root.quit()
        break
    root.update()

cap.release()
cv2.destroyAllWindows()
