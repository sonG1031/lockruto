from tkinter import Tk
from screens import Screen
from utils import playSound
import os


home_path = os.path.expanduser('~')
def init():
    encrypt_folde_path = f"{home_path}/.Lockruto"

    if not os.path.exists(encrypt_folde_path):
        os.mkdir(encrypt_folde_path)

if __name__ == "__main__":
    init()
    root = Tk()
    screen = Screen(root)
    playSound("./utils/sounds/narutoKun.mp3")
    screen.show_screen()
