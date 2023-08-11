from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

class LockScreen:
    def __init__(self, root, frames, colors):
        self.root = root
        self.frames = frames
        self.colors = colors

    def create_frame(self):
        self.frames["lock_screen"].pack(pady=20)

        title_img = Image.open("./images/lock_screen_title.png")
        title_img = title_img.resize((500, 127), Image.ANTIALIAS)
        title_photo = ImageTk.PhotoImage(title_img)
        title = Label(self.frames["lock_screen"], image=title_photo, bg=self.colors["background"], )
        title.image = title_photo
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

        self.list_file = Listbox(
            list_frame,
            selectmode="extended",
            height=15,
            width=200,
            bg=self.colors["box"],
            yscrollcommand=scrollbar.set)
        self.list_file.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.list_file.yview)

        btns_frame = Frame(
            self.frames["lock_screen"],
            # padx=100,
            pady=20,
            bg=self.colors["background"],
        )
        btns_frame.pack()

        select_btn_img = Image.open("./images/select_btn.png")
        select_btn_img = select_btn_img.resize((90, 30), Image.ANTIALIAS)
        select_btn_photo = ImageTk.PhotoImage(select_btn_img)

        select_btn = Button(
            btns_frame,
            # text="SELECT",
            image=select_btn_photo,
            width=120,
            height=35,
            fg=self.colors["button"],
            command=self.select_cmd
        )
        select_btn.image = select_btn_photo
        select_btn.pack(side="left", padx=10)

        delete_btn_img = Image.open("./images/delete_btn.png")
        delete_btn_img = delete_btn_img.resize((90, 30), Image.ANTIALIAS)
        delete_btn_photo = ImageTk.PhotoImage(delete_btn_img)

        delete_btn = Button(
            btns_frame,
            # text="SELECT",
            image=delete_btn_photo,
            width=120,
            height=35,
            fg=self.colors["button"],
            command=self.delete_cmd
        )
        delete_btn.image = delete_btn_photo
        delete_btn.pack(side="left", padx=10)


        jutsu_btn_img = Image.open("./images/jutsu_btn.png")
        jutsu_btn_img = jutsu_btn_img.resize((90, 33), Image.ANTIALIAS)
        jutsu_btn_photo = ImageTk.PhotoImage(jutsu_btn_img)

        jutsu_btn = Button(
            btns_frame,
            # text="JUTSU",
            image=jutsu_btn_photo,
            width=120,
            height=35,
            fg=self.colors["button"],
            # command=self.unlock_cmd
        )
        jutsu_btn.image = jutsu_btn_photo
        jutsu_btn.pack(side="left", padx=10)

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
            command=self.home_cmd
        )
        home_btn.image = home_btn_photo
        home_btn.pack(side="left", padx=10)

        bg_photo = PhotoImage(file="./images/bg2.png")
        bg = Label(self.frames['lock_screen'], image=bg_photo, bg=self.colors["background"],
        )
        bg.image = bg_photo
        bg.pack(side="bottom")

        print("lock_screen created")

    def select_cmd(self):
        files = filedialog.askopenfilenames(
            title="봉인할 파일을 선택하라니깐!",
            filetypes=(("PNG", "*.png"), ("모든 파일", "*.*")),
            initialdir="/Users/pulledsub"
        )
        for file in files:  # 사용자가 선택한 파일
            self.list_file.insert(END, file)

    def delete_cmd(self):
        # 뒤집는 이유: 끝 인덱스부터 지워야 지우고 난 후 다음에 지울 인덱스에 영향이 없음
        for idx in reversed(self.list_file.curselection()):
            self.list_file.delete(idx)

    def home_cmd(self):
        from screens.start_screen import StartScreen
        # 잠금화면 삭제 후 빈화면 할당
        self.frames['lock_screen'].destroy()
        self.frames['lock_screen'] = Frame(self.root, relief="solid", bg=self.colors["background"])

        StartScreen(self.root, self.frames, self.colors).create_frame()