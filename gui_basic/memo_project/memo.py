from tkinter import *
import os

root = Tk()
root.title("제목 없음 - Minsub 메모장")
root.geometry("640x480")

menu = Menu(root)

frame = Frame(root)
frame.pack(fill="both", expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
txt = Text(frame, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True, side="left")

scrollbar.config(command=txt.yview)

filename = 'mynote.txt'
def file_open():
    if os.path.isfile(filename): # 파일이 있으면 True, 없으면 False (인자값은 경로)
        with open(filename, 'r') as f:
            memo = f.read()
            txt.delete("1.0", END)
            txt.insert(END, memo)

def file_save():
    with open(filename, 'w') as f:
        memo = txt.get("1.0", END)
        f.write(memo)


menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=file_open)
menu_file.add_command(label="저장", command=file_save)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=Menu(menu, tearoff=0))
menu.add_cascade(label="서식", menu=Menu(menu, tearoff=0))
menu.add_cascade(label="보기", menu=Menu(menu, tearoff=0))
menu.add_cascade(label="도움말", menu=Menu(menu, tearoff=0))

root.config(menu=menu)

root.mainloop()