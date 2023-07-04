from tkinter import *

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

menu = Menu(root)


def create_new_file():
    print("create_new_file")

# 메뉴에 등록된 항목의 세부 항목
menu_file = Menu(menu, tearoff=0) # root가 아닌 menu에 추가하기 위해서
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 메뉴 구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator() # 메뉴 구분자
menu_file.add_command(label="Save All", state="disabled") # 비활성화
menu_file.add_separator() # 메뉴 구분자
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file) # 메뉴에 등록

# 세부 메뉴 없이
menu.add_cascade(label="Edit", menu=Menu(menu, tearoff=0))

# radio button
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# check button
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu) # 메뉴를 화면에 포함시키기 위해서
root.mainloop()