from tkinter import *
from screens import ScreenFrame
import os
import tkinter.messagebox as msgbox


class FilesFrame(ScreenFrame):
    def create_frame(self):
        self.pack_frame((20,0))

        self.create_title("./images/files_screen_title.png", (500, 146))

        self.create_list()
        home_path = os.path.expanduser('~')
        file_path = f"{home_path}/.Lockruto"
        file_list = os.listdir(file_path)
        if len(file_list):
            for file in file_list:
                if file == '.DS_Store':
                    continue
                self.list_file.insert(END, file)

        btns_info = [
            {
                "btn_path": "./images/open_btn.png",
                "btn_size": (70, 32),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.open_cmd,
                "btn_side": "left"
            },
            {
                "btn_path": "./images/unlock_btn.png",
                "btn_size": (90, 30),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.unlock_cmd,
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

        print("files_frame created")

    def open_cmd(self):
        lst_files = []
        for idx in self.list_file.curselection():
            lst_files.append(self.list_file.get(idx))
        if len(lst_files) == 0:
            msgbox.showwarning("WAIT!", "Please select files first..")
            return
        self.move_window("open_screen", lst_files)

    def unlock_cmd(self):
        lst_files = []
        for idx in self.list_file.curselection():
            lst_files.append(self.list_file.get(idx))
        if len(lst_files) == 0:
            msgbox.showwarning("WAIT!", "Please select files first..")
            return
        self.move_window("unlock_screen", lst_files)