import os
from tkinter import *
import tkinter.messagebox as msgbox

from PIL import ImageTk,Image

from screens import ScreenFrame
import cv2

import csv
import copy
import time
from model.yolox.yolox_onnx import YoloxONNX
from utils import playSound

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

class OpenFrame(ScreenFrame):

    def __init__(self, root, frames, frame_name, colors, lst_files=None):
        super().__init__(root, frames, frame_name, colors)
        self.tmp_class_id = 1
        self.pw_frame = Frame(self.frame[self.frame_name], relief="solid", bg=self.colors["background"])
        self.pw_idx = 0
        self.pw_lst = []
        self.pw = []
        self.is_pw_done = False
        self.cap = cv2.VideoCapture(0)
        self.lst_files = lst_files

        # pbkdf2에 사용되는 것으로 이런식의 하드 코딩으로 하면 안됨. 그러나 서버, Auth, db 없이 간단한 프로그램을 만들것이기에 박아둠
        self.salt = b"co\x90w\xc0\x01&\xb6\xb8\xae\x16\x9fA*\xa2\xe6\xfdd}(\xaa\xcb\x94b\x1e\xe6\x93'\x1e\x88_Y" # 32bit


    def create_frame(self):
        self.pack_frame((20, 0))

        self.create_title("./images/files_screen_title.png", (500, 146))

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
                "btn_path": "./images/reset_btn.png",
                "btn_size": (70, 33),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.reset_cmd,
                "btn_side": "left"
            },
            {
                "btn_path": "./images/open_btn.png",
                "btn_size": (90, 32),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.open_cmd,
                "btn_side": "left"
            },
            {
                "btn_path": "./images/home_btn.png",
                "btn_size": (70, 32),
                "btn_w": 120,
                "btn_h": 35,
                "btn_cmd": self.home_cmd,
                "btn_side": "left"
            },
        ]

        self.create_btns(btns_info)

        self.pw_frame.pack()

        sharingan_img = Image.open("./images/sharingan.png")
        sharingan_img = sharingan_img.resize((60, 60), Image.ANTIALIAS)
        self.sharingan_photo = ImageTk.PhotoImage(sharingan_img)

        mangekyo_img = Image.open("./images/mangekyo.png")
        mangekyo_img = mangekyo_img.resize((60,60), Image.ANTIALIAS)
        self.mangekyo_photo = ImageTk.PhotoImage(mangekyo_img)

        for _ in range(6): # 패스워드 자릿 수 표시
            sharingan = Label(self.pw_frame, image=self.sharingan_photo, bg=self.colors['background'])
            sharingan.image = self.sharingan_photo
            sharingan.pack(side="left", padx=10)
            self.pw_lst.append(sharingan)


        self.create_bg("./images/bg2.png")

        print("open_frame created")

        ############################################ 기초 변수 설정
        model_path = "model/yolox/yolox_nano.onnx"
        input_shape = (416, 416)
        score_th = 0.75
        nms_th = 0.45
        nms_score_th = 0.1
        with_p6 = False

        frame_count = 0
        fps = 60
        skip_frame = 0
        play_effect_count = 0

        ############################################ .onnx 모델 가져오기
        yolox = YoloxONNX(
            model_path=model_path,
            input_shape=input_shape,
            class_score_th=score_th,
            nms_th=nms_th,
            nms_score_th=nms_score_th,
            with_p6=with_p6,
            providers=['CPUExecutionProvider'],
        )

        ############################################ 바운딩 박스와 같이 띄어줄 텍스트
        with open('setting/labels.csv', encoding='utf8') as f:
            labels = csv.reader(f)
            labels = [row for row in labels]

        while self.cap.isOpened():
            start_time = time.time()
            ret, img = self.cap.read()

            if not ret:  # 캡처가 안됬을때
                continue

            debug_img = copy.deepcopy(img)

            frame_count += 1
            if (frame_count % (skip_frame + 1)) != 0:  # 스킵할 프레임 범위에 있다면
                continue

            ############################################ 모델에 웹캡으로 입력받은 사진 -> 예측값 받아오기
            if not self.is_pw_done:
                bboxes, scores, class_ids = yolox.inference(img)

                ############################################ 반복문을 통해 가장 높은 점수의 클래스 찾기
                for bbox, score, class_id in zip(bboxes, scores, class_ids):
                    class_id = int(class_id) + 1
                    if score < score_th:  # score_th(threshold)보다 높지 않으면 넘김
                        continue

                    ############################################ 바운딩 박스 좌표
                    x1, y1 = int(bbox[0]), int(bbox[1])
                    x2, y2 = int(bbox[2]), int(bbox[3])

                    cv2.putText(
                        debug_img, 'ID:' + str(class_id) + ' ' +
                                     labels[class_id][0] + ' ' + '{:.3f}'.format(score),
                        (x1, y1 - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2,
                        cv2.LINE_AA)  # 예측한 클래스를 바운딩 박스 위에 그리기
                    cv2.rectangle(debug_img, (x1, y1), (x2, y2), (255, 255, 0), 2)  # 바운딩 박스

                    # 각 인술 당 한번의 소리를 내기 위해서
                    if play_effect_count == 0:
                        playSound("./utils/sounds/jutsu.mp3")
                        play_effect_count += 1
                        self.tmp_class_id = class_id

                        if self.pw_idx < len(self.pw_lst):
                            self.pw_lst[self.pw_idx]['image'] = self.mangekyo_photo
                            self.pw_idx += 1
                            # self.root.update()
                        if self.pw_idx == len(self.pw_lst):
                            self.is_pw_done = True

                        self.pw.append(labels[class_id][0])

                    elif self.tmp_class_id != class_id: # 새로운 인술을 했을때
                        play_effect_count = 0

            ############################################ FPS 계산
            elapsed_time = time.time() - start_time  # 경과 시간
            sleep_time = max(0, int((1.0 / fps) - elapsed_time))  # 프레임 조정을 위해
            time.sleep(sleep_time)

            cv2.putText(
                debug_img,
                "FPS:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

            debug_img = cv2.resize(debug_img, dsize=(320,180), interpolation=cv2.INTER_LINEAR)
            debug_img = cv2.cvtColor(debug_img, cv2.COLOR_BGR2RGB)
            debug_img = ImageTk.PhotoImage(Image.fromarray(debug_img))
            cam_label['image'] = debug_img

            self.root.update()
        self.cap.release()
        cv2.destroyAllWindows()


    def cancel_cmd(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.move_window("files_screen", self.lst_files)

    def home_cmd(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.move_window("start_screen")

    def reset_cmd(self):
        self.is_pw_done = False
        for pw in self.pw_lst:  # 패스워드 자릿 수 표시
            pw['image'] = self.sharingan_photo

        self.pw_idx = 0
        self.tmp_class_id = 1
        self.pw = []
        self.frame[self.frame_name].update()

    def open_cmd(self):
        if len(self.pw) < 6:
            playSound("./utils/sounds/HEUA.mp3")
            msgbox.showwarning("WAIT!", "You have to finish your Jutsu!!")
            return
        print(self.pw)

        BS = 16 # padding
        PW = "".join(self.pw)
        PW = PBKDF2(PW, self.salt, dkLen=32)

        home_path = os.path.expanduser('~')

        try:
            for lst_file in self.lst_files:
                    file_name = lst_file.split('.lockruto')[0]
                    file_path = f"{home_path}/.Lockruto/{lst_file}"

                    with open(file_path, 'rb') as f:
                        iv = f.read(16)  # 16bit
                        decrypt_file = f.read()
                    cipher = AES.new(PW, AES.MODE_CBC, iv=iv)
                    og_file = unpad(cipher.decrypt(decrypt_file), BS)

                    decrypt_path = f"{home_path}/Downloads/{file_name}"
                    print(file_name)
                    with open(decrypt_path, 'wb+') as f:
                        f.write(og_file)

        except Exception as e:
            msgbox.showerror("Error", str(e))
            return

        playSound("./utils/sounds/jutsuFinished.mp3")
        msgbox.showinfo("Opened", f"{len(self.lst_files)} files are opened")

        self.home_cmd()