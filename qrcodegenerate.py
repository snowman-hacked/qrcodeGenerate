import tkinter
import tkinter.font
import random
import qrcode
from PIL import Image, ImageTk
from io import BytesIO

def buttonClick():
     qr_data = url_entry.get() # 입력받은 URL 주소를 qr_data에 저장
     qr_img = qrcode.make(qr_data) # QR코드 생성

     # QR코드를 메모리에 저장
     # 배운대로 파일에 저장하면 저장경로이슈가 생길거같아
     # GPT에게 물어봤다..
     qr_buffer = BytesIO()
     qr_img.save(qr_buffer, format='PNG')
     qr_buffer.seek(0)

     # QR코드를 tkinter Label에 표시
     qr_img = Image.open(qr_buffer)
     qr_img = qr_img.resize((200, 200))
     qr_photo = ImageTk.PhotoImage(qr_img)
     qr_label.config(image=qr_photo)
     qr_label.image = qr_photo

# 다른 컴퓨터에서 열면 화면이 이상한데 나오는 문제 해결
def center_window(window, width, height):
    # 화면의 너비와 높이 가져오기
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 창의 위치 계산
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # 창의 크기와 위치 설정
    window.geometry(f'{width}x{height}+{x}+{y}')

#여기는 배운대로 똑같음
window=tkinter.Tk()
window.title('QRCode Generation')
center_window(window, 400, 300)  # 창을 화면 중앙에 배치
window.resizable(False, False)

button = tkinter.Button(window,             
                        overrelief="solid", 
                        text="QR생성",      
                        width=15,           
                        command=buttonClick,
                        repeatdelay=1000,
                        repeatinterval=100)
url_label = tkinter.Label(text="URL=")  # URL= 텍스트 표시해주는 부분
url_entry = tkinter.Entry()             # URL 입력받는 부분
qr_label = tkinter.Label(window)        # QR코드 표시 부분

url_label.pack()
url_entry.pack()
button.pack()
qr_label.pack()

window.mainloop()