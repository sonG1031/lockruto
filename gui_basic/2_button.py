from tkinter import *       # tkinter는 자동으로 모듈에 포함되어 있기 때문에 따로 설치하지 않아도 됨.

root = Tk()
root.title("sex") # 프로그램 타이틀

btn1 = Button(root, text="버튼1") # 어디에 넣을지, 버튼 위에 적힐 글씨
btn1.pack() # pack을 호출함으로써 root에 포함됨

btn2 = Button(root, padx=5, pady=10, text="버튼2") # padx, pady 는 padding임
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼의 고정 크기, 텍스트가 길면 잘림
btn4.pack()

btn5 = Button(root, fg="red", bg="blue", text="버튼5") # fg: 글자색, bg: 버튼 배경(맥북은 안바뀜)
btn5.pack()

# photo = PhotoImage(file="img.png")
# btn6 = Button(root, image=photo)  # 이미지 버튼
# btn6.pack()

def btncmd():
    print("click")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()