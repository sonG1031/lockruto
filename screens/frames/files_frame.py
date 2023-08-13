from tkinter import *
from screens import ScreenFrame

class FilesFrame(ScreenFrame):
    def create_frame(self):
        self.pack_frame((20,0))

        self.create_title("./images/files_screen_title.png", (500, 146))

        self.create_list()

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
        pass

    def unlock_cmd(self):
        pass