from tkinter import *

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=2) # 여러 가지 값들을 관리하는 목록 위젯
# selectmode를 통해 선택을 한개만 할 수 있게 할 수도, 여러개 할 수도 있음.
# height를 0으로 하면 전체가 화면에 나오지만, 다른 수를 주면 그 수에 맞는 개수에 맞춰 화면에 나옴
# 목록 삽입
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "GRAPE")
listbox.pack()

def btncmd():
    # listbox.delete(0) # 삭제

    # print(listbox.size()) # 리스트 개수

    # print("1~3 items of list : ", listbox.get(0,2)) # 항목 확인

    # 선택된 항목 확인
    print("selected items : ", listbox.curselection()) # 선택된 항목의 인덱스 값을 반환함
    for idx in listbox.curselection():
        print(listbox.get( ))

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()