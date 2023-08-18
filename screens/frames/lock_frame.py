from tkinter import *
from screens import ScreenFrame

from utils import playSound

from tkinter import filedialog
import tkinter.messagebox as msgbox

import os

class LockFrame(ScreenFrame):

    def __init__(self, root, frames, frame_name, colors, lst_files=None):
        super().__init__(root, frames, frame_name, colors)
        self.lst_files = lst_files
    def create_frame(self):
        self.pack_frame((20, 0))

        self.create_title("./images/lock_screen_title.png", (500, 127))

        self.create_list()

        if self.lst_files:
            for lst_file in self.lst_files:
                self.list_file.insert(END, lst_file)

        btns_info = [
            {
                "btn_path": "./images/select_btn.png",
                "btn_size": (90, 30),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.select_cmd,
                "btn_side": "left"
            },
            {
                "btn_path": "./images/delete_btn.png",
                "btn_size": (90, 30),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.delete_cmd,
                "btn_side": "left"
            },
            {
                "btn_path": "./images/jutsu_btn.png",
                "btn_size": (90, 33),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.jutsu_cmd,
                "btn_side": "left"
            },
            {
                "btn_path": "./images/home_btn.png",
                "btn_size": (70, 32),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": lambda: self.move_window("start_screen"),
                "btn_side": "left"
            },
        ]

        self.create_btns(btns_info)

        self.create_bg("./images/bg2.png")

        print("lock_frame created")


    def select_cmd(self):
        playSound("./utils/sounds/HEUA.mp3")

        files = filedialog.askopenfilenames(
            title="봉인할 파일을 선택하라니깐!",
            filetypes=(("TXT", "*.txt"), ("ALL", "*.*"),),
            initialdir=os.path.expanduser('~')
        )
        for file in files:  # 사용자가 선택한 파일
            self.list_file.insert(END, file)

    def delete_cmd(self):
        playSound("./utils/sounds/HEUA.mp3")

        # 뒤집는 이유: 끝 인덱스부터 지워야 지우고 난 후 다음에 지울 인덱스에 영향이 없음
        for idx in reversed(self.list_file.curselection()):
            self.list_file.delete(idx)


    def jutsu_cmd(self):
        if self.list_file.size() == 0:
            msgbox.showwarning("WAIT!", "Please select files first..")
            return

        res = msgbox.askyesno("Start Jutsu", "Lessgo Jutsu!")
        if res:
            # 암호 설정으로 넘어가기
            files = self.list_file.get(0, self.list_file.size())
            self.move_window("jutsu_screen", files)
            pass
        else:
            return