from tkinter import *
from PIL import Image, ImageTk
from utils import playSound
from tkmacosx import Button


class FilesScreen:
    def __init__(self, root, frames, colors):
        self.root = root
        self.frames = frames
        self.colors = colors
    def create_frame(self):
        self.frames['files_screen'].pack(pady=(20,0))

        title_img = Image.open("./images/files_screen_title.png")
        title_img = title_img.resize((500, 146), Image.ANTIALIAS)
        title_photo = ImageTk.PhotoImage(title_img)
        title = Label(self.frames['files_screen'], image=title_photo, bg=self.colors["background"], )
        title.image = title_photo
        title.pack(side="top")

        list_frame = Frame(
            self.frames['files_screen'],
            padx=100,
            pady=20,
            bg=self.colors["background"],
        )
        list_frame.pack(side="top", fill="both")

        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        list_file = Listbox(
            list_frame,
            selectmode="extended",
            height=15,
            width=200,
            bg=self.colors["box"],
            yscrollcommand=scrollbar.set)
        list_file.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=list_file.yview)

        btns_frame =  Frame(
            self.frames['files_screen'],
            padx=100,
            pady=20,
            bg=self.colors["background"],
        )
        btns_frame.pack()

        open_btn_img = Image.open("./images/open_btn.png")
        open_btn_img = open_btn_img.resize((70, 32), Image.ANTIALIAS)
        open_btn_photo = ImageTk.PhotoImage(open_btn_img)

        open_btn = Button(
            btns_frame,
            # text="OPEN",
            image=open_btn_photo,
            width=120,
            height=35,
            fg = self.colors["button"],
            activebackground=self.colors["activeBtn"],
            bg=self.colors["background"],

            borderless=1,
        )
        open_btn.image = open_btn_photo
        open_btn.pack(side="left", padx=10)

        unlock_btn_img = Image.open("./images/unlock_btn.png")
        unlock_btn_img = unlock_btn_img.resize((90, 30), Image.ANTIALIAS)
        unlock_btn_photo = ImageTk.PhotoImage(unlock_btn_img)

        unlock_btn = Button(
            btns_frame,
            # text="UNLOCK",
            image=unlock_btn_photo,
            width=120,
            height=35,
            fg=self.colors["button"],
            command=self.unlock_cmd,
            activebackground=self.colors["activeBtn"],
            bg=self.colors["background"],

            borderless=1,
        )
        unlock_btn.image = unlock_btn_photo
        unlock_btn.pack(side="left", padx=10)

        home_btn_img = Image.open("./images/home_btn.png")
        home_btn_img = home_btn_img.resize((70, 32), Image.ANTIALIAS)
        home_btn_photo = ImageTk.PhotoImage(home_btn_img)

        home_btn = Button(
            btns_frame,
            # text="HOME",
            image=home_btn_photo,
            width=120,
            height=35,
            fg=self.colors["button"],
            bg=self.colors["background"],
            command=self.home_cmd,
            activebackground=self.colors["activeBtn"],
            borderless=1,
        )
        home_btn.image = home_btn_photo
        home_btn.pack(side="left", padx=10)

        bg_photo = PhotoImage(file="./images/bg2.png")
        bg = Label(self.frames['files_screen'], image=bg_photo, bg=self.colors["background"],
        )
        bg.image = bg_photo
        bg.pack(side="bottom")

        print("file_screen created")


    def home_cmd(self):
        playSound("./utils/sounds/HEUA.mp3")

        from screens.start_screen import StartScreen
        self.frames['files_screen'].destroy()

        self.frames['files_screen'] = Frame(self.root, relief="solid", bg=self.colors["background"])

        StartScreen(self.root, self.frames, self.colors).create_frame()

    def unlock_cmd(self):
        from screens.lock_screen import LockScreen
