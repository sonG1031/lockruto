from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("GUI")

# 레이아웃을 구분하기 위해 프레임을 단위로 쪼갠다

# 파일 프레임 (파일 추가, 삭제)
file_frame = Frame(root, padx=5, pady=5)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, padx=5, pady=5, width=10, text="파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=10, text="선택삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root, padx=5, pady=5)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로", padx=5, pady=5)
path_frame.pack(fill="x", padx=10, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # ipad는 안쪽 패딩

btn_dest_path = Button(path_frame, text="찾아보기",  padx=5, pady=5, width=10)
btn_dest_path.pack(side="right")


# 옵션 프레임
frame_option = LabelFrame(root, text="옵션", padx=5, pady=5)
frame_option.pack(padx=10, pady=5)

# 가로 넓이 옵션
label_width = Label(frame_option, text="가로넓이", width=5)
label_width.pack(side="left")

opt_width = ["원본유지", "1024", "800", "640"]
combo_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
combo_width.current(0)
combo_width.pack(side="left")

# 간격 옵션
label_space = Label(frame_option, text="간격 ", width=5)
label_space.pack(side="left")

opt_space = ["없음", "좁게", "보통", "넓게"]
combo_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
combo_space.current(0)
combo_space.pack(side="left")

# 포맷 옵션
label_format = Label(frame_option, text="포맷", width=5)
label_format.pack(side="left")

opt_format = ["PNG", "JPG", "BMP"]
combo_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
combo_format.current(0)
combo_format.pack(side="left")

# 프로그레스바 프레임
frame_progress = LabelFrame(root, text="진행상황", padx=5, pady=5)
frame_progress.pack(fill="x", padx=10, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", expand=True)

# 실행 프레임 (시작, 닫기 버튼)
frame_run = Frame(root, padx=5, pady=5)
frame_run.pack(fill="x")

btn_close = Button(frame_run, padx=5, pady=5, width=10, text="닫기")
btn_close.pack(side="right")

btn_start = Button(frame_run, padx=5, pady=5, width=10, text="시작")
btn_start.pack(side="right")


# root.geometry("640x480") 따로 지정하지 않으면 위젯에 맞게 알아서 창의 크기가 정해짐
root.resizable(False, False)
root.mainloop()