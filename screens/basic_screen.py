from tkinter import *


from screens.start_screen import StartScreen
from screens.files_screen import FilesScreen

class Screen:
    def __init__(self, root):

        self.colors = {
            "background": "#000000",
            "button": "#332F2E",
            "box": "#1F1C1C",
        }

        self.frames = {
            "start_screen": Frame(root, relief="solid", bg=self.colors["background"]),
            "files_screen": Frame(root, relief="solid", bg=self.colors["background"]),
        }

        self.root = root
        self.root.title("Lockruto")
        self.root.resizable(False, False)
        self.root.geometry("720x720")
        self.root.config(bg=self.colors['background'])

    def show_screen(self):
        st_screen = StartScreen(self.root, self.frames, self.colors)
        st_screen.create_frame()
        # self.frames["start_screen"].pack(pady=230)
        #
        # f_screen = FilesScreen(self.root, self.frames, self.colors)
        # f_screen.create_frame()

        self.root.mainloop()



