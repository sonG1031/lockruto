from tkinter import Tk
from screens import Screen
from utils import playSound

if __name__ == "__main__":
    root = Tk()
    screen = Screen(root)
    playSound("./utils/sounds/narutoKun.mp3")
    screen.show_screen()
