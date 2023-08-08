from tkinter import *

class StartScreen:

    def __init__(self, root, frames, colors):
        self.root = root
        self.frames = frames
        self.colors = colors
    def create_frame(self):
        self.frames["start_screen"].pack(pady=230)

        title = Label(
            self.frames["start_screen"],
            text="Lockruto",
            bg=self.colors["background"],
            font=("Arial", 100, "bold"),
        )
        title.pack(side="top")

        btns_frame = Frame(
            self.frames["start_screen"],
            bg=self.colors["background"],
        )
        btns_frame.pack()

        files_btn = Button(
            btns_frame,
            text="FILES",
            width=10,
            height=2,
            fg=self.colors["button"],
            command=self.files_cmd
        )
        files_btn.pack(side="left", padx=10)

        lock_btn = Button(
            btns_frame,
            text="LOCK",
            width=10,
            height=2,
            fg=self.colors["button"],
            command=self.lock_cmd
        )
        lock_btn.pack(side="right", padx=10)

        print("start_screen created")



    def files_cmd(self):
        from screens.files_screen import FilesScreen
        self.frames['start_screen'].destroy() # 화면에서 삭제
        # self.frames['files_screen'].pack(pady=20)

        self.frames['start_screen'] = Frame(self.root, relief="solid", bg=self.colors["background"])

        FilesScreen(self.root, self.frames, self.colors).create_frame() # 파일 목록 화면으로 이동

    def lock_cmd(self):
        pass
