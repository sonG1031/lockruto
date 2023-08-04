import os
from tkinter import *
import tkinter.messagebox  as msgbox
import tkinter.ttk as ttk
from tkinter import filedialog # 파일 탐색기
from PIL import Image

root = Tk()
root.title("GUI")

# 파일 추가
def add_file():
    # 파일 탐색기가 떠야함
    files = filedialog.askopenfilenames( # 선택된 파일의 절대경로를 리스트로 반환함
        title="이미지 파일을 선택하세요",
        filetypes=(("PNG", "*.png"), ("모든 파일", "*.*")),
        initialdir="/Users/pulledsub/Pictures/"
    )
    for file in files: # 사용자가 선택한 파일
        list_file.insert(END, file)

# 선택된 파일 삭제
def del_file():
    # print(list_file.curselection()) 선택된 파일

    for idx in reversed(list_file.curselection()): # 뒤집는 이유: 끝 인덱스부터 지워야 지우고 난 후 다음에 지울 인덱스에 영향이 없음
        list_file.delete(idx)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': # 사용자가 취소를 눌렀을때
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합
def merge_image():

    try:
        # 가로 넓이 처리
        img_width = combo_width.get()
        if img_width == "원본유지":
            img_width = -1 # -1일때 원본 기준
        else:
            img_width = int(img_width)

        # 간격 처리
        img_space = combo_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        # 포맷
        img_format = combo_format.get().lower() # 확장자 소문자로 변경

        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈 처리
        images_sizes = []
        if img_width > -1:
            # 계산식
            # 원본 width : 원본 height = 변경 width : 변경 height
            #     x     :     y     =     x'     :    y'
            # xy' = x'y
            # y' = x'y / x => 이 식을 적용해서 width 비율과 맞게 height 변경
            images_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본
            images_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*images_sizes)

        max_width, total_height = max(widths), sum(heights)

        # 스케치북, 합칠 이미지들의 전체 body
        if img_space > 0: # 이미지 간격
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height), (255,255,255))
        y_offset = 0 # y 위치 업데이트

        for idx, img in enumerate(images):
            # width가 원본이 아닐때 resize
            if img_width > -1:
                img = img.resize(images_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += img.size[1] + img_space # y 위치 업데이트 (사진 높이 + 간격)

            progress = (idx + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = entry_filename.get()+ "." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)

        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as e:
        msgbox.showerror("에러", str(e))

# 시작 버튼
def start():
    # 각 옵션들 값 확인
    # print("가로 넓이 : ", combo_width.get())
    # print("간격 : ", combo_space.get())
    # print("포맷 : ", combo_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 파일 이름 확인
    if len(entry_filename.get()) == 0:
        msgbox.showwarning("경고", "파일 이름을 추가하세요")
        return

    # 이미지 통합 작업
    merge_image()

# 레이아웃을 구분하기 위해 프레임을 단위로 쪼갠다

# 파일 프레임 (파일 추가, 삭제)
file_frame = Frame(root, padx=5, pady=5)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, padx=5, pady=5, width=10, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=10, text="선택삭제", command=del_file)
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
path_frame.pack(fill="x", padx=10, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # ipad는 안쪽 패딩

btn_dest_path = Button(path_frame, text="찾아보기",  padx=5, pady=5, width=10, command=browse_dest_path)
btn_dest_path.pack(side="right")

#
filename_frame = LabelFrame(root, text="파일이름", padx=5, pady=5)
filename_frame.pack(fill="x", padx=10, pady=5, ipady=5)
entry_filename = Entry(filename_frame)
entry_filename.pack(side="left", fill="x", expand=True, ipady=4)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션", padx=5, pady=5)
frame_option.pack(padx=10, pady=5, ipady=5)

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
frame_progress.pack(fill="x", padx=10, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", expand=True)

# 실행 프레임 (시작, 닫기 버튼)
frame_run = Frame(root, padx=5, pady=5)
frame_run.pack(fill="x")

btn_close = Button(frame_run, padx=5, pady=5, width=10, text="닫기", command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, width=10, text="시작", command=start)
btn_start.pack(side="right", padx=5, pady=5)


# root.geometry("640x480") 따로 지정하지 않으면 위젯에 맞게 알아서 창의 크기가 정해짐
root.resizable(False, False)
root.mainloop()