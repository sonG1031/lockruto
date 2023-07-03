from tkinter import *

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burget_var = IntVar()
btn_burget1 = Radiobutton(root, text="햄버거", value=1, variable=burget_var)
btn_burget1.select()
btn_burget2 = Radiobutton(root, text="치즈 햄버거", value=2, variable=burget_var)
btn_burget3 = Radiobutton(root, text="치킨 햄버거", value=3, variable=burget_var)

btn_burget1.pack()
btn_burget2.pack()
btn_burget3.pack()

Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
def btncmd():
    print(burget_var.get()) # 라디오 버튼중에 선택된 항목의 값(value의 인자)
    print(drink_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()