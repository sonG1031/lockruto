import time
from PIL import ImageGrab

time.sleep(5) # 5초 대기

for i in range(1, 11): # 2초 간격 10개 이미지 저장
    img = ImageGrab.grab()
    img.save(f"image{i}.png")
    time.sleep(2)