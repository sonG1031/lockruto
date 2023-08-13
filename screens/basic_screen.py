from tkinter import *

class Screen:
    def __init__(self, root):

        self.colors = {
            "background": "#000000",
            "button": "#332F2E",
            "box": "#1F1C1C",
            "activeBtn": "#D941A4"
        }

        self.frames = {
            "start_screen": Frame(root, relief="solid", bg=self.colors["background"]),
            "files_screen": Frame(root, relief="solid", bg=self.colors["background"]),
            "lock_screen": Frame(root, relief="solid", bg=self.colors["background"]),
            "jutsu_screen": Frame(root, relief="solid", bg=self.colors["background"]),
        }

        self.root = root
        self.root.title("Lockruto")
        self.root.resizable(False, False)
        self.root.geometry("720x720")
        self.root.config(bg=self.colors['background'])

    def show_screen(self):
        from screens.frames import StartFrame

        st_screen = StartFrame(self.root, self.frames, "start_screen", self.colors)
        st_screen.create_frame()

        self.root.mainloop()



