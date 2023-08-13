from screens import ScreenFrame

class StartFrame(ScreenFrame):
    def create_frame(self):
        self.pack_frame((60,0))

        self.create_title("./images/start_screen_title.png", (500,187))

        btns_info = [
            {
                "btn_path": "./images/files_btn.png",
                "btn_size": (100,38),
                "btn_w": 100,
                "btn_h": 43,
                "btn_cmd":lambda:  self.move_window("files_screen"),
                "btn_side":"left"
            },
            {
                "btn_path": "./images/lock_btn.png",
                "btn_size": (100, 43),
                "btn_w": 100,
                "btn_h": 43,
                "btn_cmd":lambda:  self.move_window("lock_screen"),
                "btn_side": "left"
            },
        ]

        self.create_btns(btns_info)

        self.create_bg("./images/bg.png")

        print("start_frame created")