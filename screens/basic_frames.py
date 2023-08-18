from tkinter import *
from tkinter import Listbox

from PIL import Image, ImageTk
from tkmacosx import Button

from utils import playSound
class ScreenFrame:
    def __init__(self, root, frames, frame_name, colors):
        self.root = root
        self.frame = frames
        self.frame_name = frame_name
        self.colors = colors
        self.list_file = None

    def create_frame(self):
        pass

    def pack_frame(self, frame_pady): # frame_pady: tuple(top: int, bottom: int)
        self.frame[self.frame_name].pack(pady=frame_pady)

    def create_title(self, title_path, title_size): # titleSize: tuple(int, int)
        title_img = Image.open(title_path)
        title_img = title_img.resize(title_size, Image.ANTIALIAS)
        title_photo = ImageTk.PhotoImage(title_img)
        title = Label(self.frame[self.frame_name], image=title_photo, bg=self.colors["background"], )
        title.image = title_photo
        title.pack(side="top")

    def create_list(self):
        list_frame = Frame(
            self.frame[self.frame_name],
            padx=100,
            pady=20,
            bg=self.colors["background"],
        )
        list_frame.pack(side="top", fill="both")

        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.list_file = Listbox(
            list_frame,
            selectmode="extended",
            height=15,
            width=200,
            bg=self.colors["box"],
            yscrollcommand=scrollbar.set)
        self.list_file.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.list_file.yview)

        self.list_file.focus_set()

    def create_btns(self, btns_info):
        btns_frame = Frame(
            self.frame[self.frame_name],
            bg=self.colors["background"],
        )
        btns_frame.pack(pady=(0,20))

        for btn_info in btns_info:
            self.create_btn(btns_frame, **btn_info)


    def create_btn(
            self,
            btns_frame,
            btn_path,
            btn_size, # btn_size: tuple(int, int)
            btn_w,
            btn_h,
            btn_cmd,
            btn_side):
        btn_img = Image.open(btn_path)
        btn_img = btn_img.resize(btn_size, Image.ANTIALIAS)
        btn_photo = ImageTk.PhotoImage(btn_img)

        btn = Button(
            btns_frame,
            image=btn_photo,
            width=btn_w,
            height=btn_h,
            fg=self.colors["button"],
            activebackground=self.colors["activeBtn"],
            bg=self.colors["background"],
            borderless=1,
            command=btn_cmd
        )
        btn.image = btn_photo
        btn.pack(side=btn_side, padx=10)

    def create_bg(self, bg_path):
        bg_photo = PhotoImage(file=bg_path)
        bg = Label(self.frame[self.frame_name], image=bg_photo, bg=self.colors["background"],)
        bg.image = bg_photo
        bg.pack(side="bottom")


    def move_window(self, move_frame_name, lst_files=None):
        from screens.frames import StartFrame, FilesFrame, LockFrame, JutsuFrame, OpenFrame, UnlockFrame
        playSound("./utils/sounds/HEUA.mp3")

        self.frame[self.frame_name].destroy()
        self.frame[self.frame_name] = Frame(self.root, relief="solid", bg=self.colors["background"])
        print(f"{self.frame_name} destroyed")

        if move_frame_name == "start_screen":
            StartFrame(self.root, self.frame, "start_screen", self.colors).create_frame()
        elif move_frame_name == "files_screen":
            FilesFrame(self.root, self.frame, "files_screen", self.colors).create_frame()
        elif move_frame_name == "lock_screen":
            LockFrame(self.root, self.frame, "lock_screen", self.colors, lst_files).create_frame()
        elif move_frame_name == "jutsu_screen":
            JutsuFrame(self.root, self.frame, "jutsu_screen", self.colors, lst_files).create_frame()
        elif move_frame_name == "open_screen":
            OpenFrame(self.root, self.frame, "open_screen", self.colors, lst_files).create_frame()
        elif move_frame_name == "unlock_screen":
            UnlockFrame(self.root, self.frame, "unlock_screen", self.colors, lst_files).create_frame()