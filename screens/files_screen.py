from tkinter import *
class FilesScreen:
    def __init__(self, root, frames, colors):
        self.root = root
        self.frames = frames
        self.colors = colors
    def create_frame(self):
        self.frames['files_screen'].pack(pady=20)
        title = Label(
            self.frames['files_screen'],
            text="Locked Files",
            bg=self.colors["background"],
            font=("Arial", 50, "bold"),
        )
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

        open_btn = Button(
            btns_frame,
            text="OPEN",
            width=10,
            height=2,
            fg = self.colors["button"],
        )
        open_btn.pack(side="left", padx=10)

        unlock_btn = Button(
            btns_frame,
            text="UNLOCK",
            width=10,
            height=2,
            fg=self.colors["button"],
        )
        unlock_btn.pack(side="left", padx=10)

        home_btn = Button(
            btns_frame,
            text="HOME",
            width=10,
            height=2,
            fg=self.colors["button"],
            command=self.home_cmd
        )
        home_btn.pack(side="left", padx=10)
        print("file_screen created")


    def home_cmd(self):
        from screens.start_screen import StartScreen
        self.frames['files_screen'].destroy()
        # self.frames['start_screen'].pack(pady=230)

        self.frames['files_screen'] = Frame(self.root, relief="solid", bg=self.colors["background"])

        StartScreen(self.root, self.frames, self.colors).create_frame()
