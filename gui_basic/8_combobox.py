from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.set("카드 결제일") # 최초 목록 제목 설정, 버튼 클릭을 통한 값 설정
combobox.pack()

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 선택된 항목을 수정X
readonly_combobox.current(0)
readonly_combobox.pack()
def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()