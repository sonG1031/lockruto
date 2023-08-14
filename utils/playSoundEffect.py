from playsound import playsound
import threading
# "./utils/sounds/jutsuFinished.mp3" 잠금 완료, 잠금 해제
# "./utils/sounds/jutsu.mp3" 잠금 설정
# "./utils/sounds/HEUA.mp3" 버튼 눌렀을때
def playSound(path):
    threading.Thread(target=playsound, args=(path,), daemon=True).start()