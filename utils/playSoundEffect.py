from playsound import playsound
import threading

def playFinishedEffect():
    threading.Thread(target=playsound, args=("./utils/sounds/jutsuFinished.mp3",), daemon=True).start()

def playEffect():
    threading.Thread(target=playsound, args=("./utils/sounds/jutsu.mp3",), daemon=True).start()


def playSound(path):
    threading.Thread(target=playsound, args=(path,), daemon=True).start()