from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 로딩 느낌
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 무언가 설치시 진행 척도
# progressbar.start(10) # 10ms 마다 움직임, 맥북은 속도가 일정
# progressbar.pack()
# def btncmd():
#     progressbar.stop() # 작동 중지
#
# btn = Button(root, text="STOP", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2) # length : 바 길이
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var2.set(i) # Progressbar의 범위 안에 값
        progressbar2.update() # UI UPDATE, p_var2의 값이 변경될때마다 바뀐 척도를 보여주기 위해서
        # update를 하지 않으면 모든 set이 끝난 후 한번만 update됨.
        print(p_var2.get())
    p_var2.set(0)

btn = Button(root, text="START", command=btncmd2)
btn.pack()

root.mainloop()