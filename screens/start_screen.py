from tkinter import *
from PIL import Image, ImageTk

class StartScreen:

    def __init__(self, root, frames, colors):
        self.root = root
        self.frames = frames
        self.colors = colors


    def create_frame(self):

        self.frames["start_screen"].pack(pady=(50,0))
        title_img = Image.open("./images/start_screen_title.png")
        title_img = title_img.resize((500,187), Image.ANTIALIAS)
        title_photo = ImageTk.PhotoImage(title_img)
        title = Label(self.frames['start_screen'], image=title_photo, bg=self.colors["background"],)
        title.image = title_photo
        title.pack(side="top")

        btns_frame = Frame(
            self.frames["start_screen"],
            bg=self.colors["background"],
        )
        btns_frame.pack(pady=(0,10))

        files_btn_img = Image.open("./images/files_btn.png")
        files_btn_img = files_btn_img.resize((100,38), Image.ANTIALIAS)
        files_btn_photo = ImageTk.PhotoImage(files_btn_img)

        files_btn = Button(
            btns_frame,
            # text="FILES",
            image=files_btn_photo,
            width=100,
            height=43,
            fg=self.colors["button"],
            bg=self.colors["background"],
            command=self.files_cmd
        )
        files_btn.image = files_btn_photo
        files_btn.pack(side="left", padx=10)

        lock_btn_img = Image.open("./images/lock_btn.png")
        lock_btn_img = lock_btn_img.resize((100, 43), Image.ANTIALIAS)
        lock_btn_photo = ImageTk.PhotoImage(lock_btn_img)

        lock_btn = Button(
            btns_frame,
            # text="LOCK",
            image=lock_btn_photo,
            width=100,
            height=43,
            fg=self.colors["button"],
            bg=self.colors["background"],
            command=self.lock_cmd
        )
        lock_btn.image = lock_btn_photo
        lock_btn.pack(side="right", padx=10)

        bg_photo = PhotoImage(file="./images/bg.png")
        bg = Label(self.frames['start_screen'], image=bg_photo, bg=self.colors["background"],
        )
        bg.image = bg_photo
        bg.pack(side="bottom")

        print("start_screen created")



    def files_cmd(self):
        from screens.files_screen import FilesScreen
        self.frames['start_screen'].destroy() # 화면에서 삭제
        self.frames['start_screen'] = Frame(self.root, relief="solid", bg=self.colors["background"])

        FilesScreen(self.root, self.frames, self.colors).create_frame() # 파일 목록 화면으로 이동

    def lock_cmd(self):
        from screens.lock_screen import LockScreen
        self.frames['start_screen'].destroy()  # 화면에서 삭제
        self.frames['start_screen'] = Frame(self.root, relief="solid", bg=self.colors["background"])

        LockScreen(self.root, self.frames, self.colors).create_frame() # 파일 잠금 화면
