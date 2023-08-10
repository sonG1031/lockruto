from tkinter import *


class LockScreen:
    def __init__(self, root, frames, colors):
        self.root = root
        self.frames = frames
        self.colors = colors

    def create_frame(self):
        self.frames["lock_screen"].pack(pady=20)

        title = Label(
            self.frames["lock_screen"],
            text="Lock With Jutsu",
            bg=self.colors["background"],
            font=("Arial", 50, "bold"),
        )
        title.pack(side="top")

        list_frame = Frame(
            self.frames["lock_screen"],
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

        btns_frame = Frame(
            self.frames["lock_screen"],
            padx=100,
            pady=20,
            bg=self.colors["background"],
        )
        btns_frame.pack()

        select_btn = Button(
            btns_frame,
            text="SELECT",
            width=10,
            height=2,
            fg=self.colors["button"],
        )
        select_btn.pack(side="left", padx=10)

        jutsu_btn = Button(
            btns_frame,
            text="JUTSU",
            width=10,
            height=2,
            fg=self.colors["button"],
            # command=self.unlock_cmd
        )
        jutsu_btn.pack(side="left", padx=10)

        home_btn = Button(
            btns_frame,
            text="HOME",
            width=10,
            height=2,
            fg=self.colors["button"],
            command=self.home_cmd
        )
        home_btn.pack(side="left", padx=10)

        bg_photo = PhotoImage(file="./images/bg2.png")
        bg = Label(self.frames['lock_screen'], image=bg_photo, bg=self.colors["background"],
        )
        bg.image = bg_photo
        bg.pack(side="bottom")

        print("lock_screen created")

    def home_cmd(self):
        from screens.start_screen import StartScreen
        # 잠금화면 삭제 후 빈화면 할당
        self.frames['lock_screen'].destroy()
        self.frames['lock_screen'] = Frame(self.root, relief="solid", bg=self.colors["background"])

        StartScreen(self.root, self.frames, self.colors).create_frame()