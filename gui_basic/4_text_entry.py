from tkinter import *

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "input text ")


e = Entry(root, width=30)
e.pack()
e.insert(0, "put only one line") # 0 == END
# Text와 Entry 둘다 텍스트를 입력받을 수 있는 input field 이다.
# 차이점은 Entry는 Enter를 입력하지 못한다.


def btncmd():
    # 1.0 에서 1은 라인 1, 0은 컬럼 기준으로 0번째 위치
    print(txt.get("1.0", END)) # get("1.0", END) == 처음부터 끝까지 문자열 가져옴
    print(e.get())

    # 처음부터 끝까지 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()