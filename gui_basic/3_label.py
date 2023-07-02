from tkinter import *       # tkinter는 자동으로 모듈에 포함되어 있기 때문에 따로 설치하지 않아도 됨.

root = Tk()
root.title("sex") # 프로그램 타이틀

# label은 글자나 이미지를 보여주는 정도, 실제로 뭔가를 할 수 있는 게 아님
label1 = Label(root, text="안냐세요")
label1.pack()

# photo = PhotoImage(file="img.png")
# label2 = Label(root, image=photo)
# label2.pack()

def change():
    label1.config(text="또 만나요")
btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()