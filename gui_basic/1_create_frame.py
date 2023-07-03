from tkinter import *       # tkinter는 자동으로 모듈에 포함되어 있기 때문에 따로 설치하지 않아도 됨.

root = Tk()
root.title("GUI Practice") # 프로그램 타이틀
root.geometry("640x640") # 창 크기 : 가로 * 세로
root.resizable(False, False) # 화면 크기 조절 : 가로, 세로
root.mainloop()