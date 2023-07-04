from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정장적으로 예매 완료") # title, description

def warn():
    msgbox.showwarning("경고","매진")

def error():
    msgbox.showerror("에러", "오류발생")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "예매하시겠습니가!")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "다시?")


def yesno():
    msgbox.askyesno("예 / 아니오", "INTP??")

def yesnocancel():
    res = msgbox.askyesnocancel(title=None, message="맞아 아니야 취소야?")
    # yes : True
    # no : Falss
    # cancel : None

    if res:
        print("예")
    elif res is None:
        print("취소")
    else:
        print("아니오")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()

Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop()