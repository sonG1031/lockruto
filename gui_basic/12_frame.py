from tkinter import *

root = Tk()
root.title("GUI Practice")
root.geometry("640x480")

Label(root, text="Choose the menu plz").pack(side="top")

Button(root, text="order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True) # side 매개변수를 통해 프레임을 패키징할때의 위치를 지정할 수 있다.
                                            # fill="both"는 화면을 꽉 채우게 해줌.
                                            # expand - "확장하다" 라는 의미로 남은 여백을 확장시킨다고 생각함

Button(frame_burger, text="ham burger").pack() # frame_burger에 버튼을 넣기위해 첫번째 인자값이 root가 아닌 frame_burger이다.
Button(frame_burger, text="cheese burger").pack()
Button(frame_burger, text="chicken burger").pack()

frame_drink = LabelFrame(root, text="drinks") # 제목이 있는 프레임
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="coca cola").pack()
Button(frame_drink, text="sprite").pack()

root.mainloop()