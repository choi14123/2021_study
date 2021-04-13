from tkinter import *
from tkinter.filedialog import *


## 함수 선언 부분 ##
def func_open():
    global filename
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image = photo


def func_zoom():
    global photo
    value = 2
    photo = PhotoImage(file=filename)
    photo = photo.zoom(value, value)
    pLabel.configure(image=photo)
    pLabel.image = photo


def func_subsample():
    global photo
    value = 2
    photo = PhotoImage(file=filename)
    photo = photo.subsample(value, value)
    pLabel.configure(image=photo)
    pLabel.image = photo


def func_exit():
    window.quit()
    window.destroy()


## 메인 코드  부분 ##
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 효과", menu=fileMenu)
fileMenu.add_command(label="확대하기", command=func_zoom)
fileMenu.add_command(label="축소하기", command=func_subsample)
fileMenu.add_separator()
window.mainloop()
