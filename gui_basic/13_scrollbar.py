from tkinter import *

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

# 스크롤바는 원하는 위젯과 프레임으로 묶어서 관리하는 것이 편하다
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # fill="y"는 y축 방향을 꽉 채운다는 의미

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)
# listbox는 yscrollcommand=scrollbar.set
# scrollbar는 scrollbar.config(command=listbox.yview)
# 을 통해 서로 매핑, 동기가 됨

root.mainloop()