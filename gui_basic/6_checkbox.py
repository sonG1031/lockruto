from tkinter import *

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

chkvar = IntVar() # Int type 변수, Checkbutton의 variable의 인자로 쓰임.
chkbox = Checkbutton(root, text="Don't show again today", variable=chkvar)
chkbox.select() # 자동 선택 처리
chkbox.deselect() # 자동 선택 해제
chkbox.pack()
def btncmd():
    print(chkvar.get()) # 0 == deselected, 1 == selected

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()