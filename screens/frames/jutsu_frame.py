from tkinter import *

from PIL import ImageTk,Image

from screens import ScreenFrame
import cv2

class JutsuFrame(ScreenFrame):

    def __init__(self, root, frames, frame_name, colors, lst_files=None):
        super().__init__(root, frames, frame_name, colors)
        self.lst_files = lst_files

    def create_frame(self):
        self.pack_frame((20, 0))

        self.create_title("./images/lock_screen_title.png", (500, 127))


        cam_label = Label(self.frame[self.frame_name], bg=self.colors['background'])
        cam_label.pack()

        btns_info = [
            {
                "btn_path": "./images/cancel_btn.png",
                "btn_size": (90, 30),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.cancel_cmd,
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

        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, img = cap.read()
            img = cv2.resize(img, dsize=(320,180), interpolation=cv2.INTER_LINEAR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(img))
            cam_label['image'] = img

            self.root.update()
        cap.release()
        cv2.destroyAllWindows()
    def cancel_cmd(self):
        self.move_window("lock_screen", self.lst_files)