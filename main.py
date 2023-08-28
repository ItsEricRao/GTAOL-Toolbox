'''
Import Modules
'''
import pydirectinput, time, keyboard, ctypes, os, threading, psutil
SendInput = ctypes.windll.user32.SendInput
from tkinter import *
from PIL import Image, ImageTk
'''
Global Variables
'''
pydirectinput.PAUSE = 0
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
PROCNAME = "GTA5.exe"

'''
Process Killer
'''
def kill():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()

'''
Tkinter GUI
'''

class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        self.root.call('tk', 'scaling', ScaleFactor/60)
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("GTAOL工具箱")
        img = Image.open("D:\Dev\GTAOL Toolbox\img.png")
        img = img.resize((219,216), Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        imglbl = Label(self.root, image=tk_img, border=20)
        imglbl.pack()
        title = Label(self.root, text="GTAOL工具箱", font=("Microsoft YaHei", 36), border=20)
        title.pack()
        text = Label(self.root, text="F4 快速零食", font=("Microsoft YaHei", 12))
        text2 = Label(self.root, text="F5 快速防弹衣", font=("Microsoft YaHei", 12))
        text3 = Label(self.root, text="F9 一键杀进程", font=("Microsoft YaHei", 12))
        text4 = Label(self.root, text="F11 进程断网", font=("Microsoft YaHei", 12))
        text5 = Label(self.root, text="F12 进程断网恢复", font=("Microsoft YaHei", 12))
        text.pack()
        text2.pack()
        text3.pack()
        text4.pack()
        text5.pack()
        # text6.pack()
        # text7.pack()
        self.root.mainloop()

gui = GUI()

'''
Network
'''
def block():
    print("LOG >> KeyPressed F11 -> Block Internet")
    os.system('netsh advfirewall firewall add rule name="GTAOL" protocol=UDP  dir=out localport=6672 action=block')
    time.sleep(0.1)

def unblock():
    print("LOG >> KeyPressed F22 -> Unblock Internet")
    os.system('netsh advfirewall firewall delete rule name="GTAOL"')
    time.sleep(0.1)

'''
Macro
'''

def snack():
    print("LOG >> KeyPressed F4 -> QuickSnack")
    pydirectinput.press('m')
    pydirectinput.press('down', presses=3)
    pydirectinput.press('enter')
    pydirectinput.press('down', presses=5)
    pydirectinput.press('enter')
    time.sleep(0.1)

# Quick Armor
def armor():
    print("LOG >> KeyPressed F6 -> QuickArmor")
    pydirectinput.press('m')
    pydirectinput.press('down', presses=3)
    pydirectinput.press('enter')
    pydirectinput.press('down', presses=4)
    pydirectinput.press('enter')
    pydirectinput.press('up', presses=3)
    time.sleep(0.1)

def mechanic():
    pydirectinput.press('up')
    time.sleep(0.5)
    pydirectinput.press('up')
    pydirectinput.press('right')
    pydirectinput.press('enter')
    time.sleep(0.5)
    pydirectinput.press('space')
    time.sleep(0.5)
    pydirectinput.press('right', presses=2)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down', presses=2)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('up')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down', presses=2)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down')
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.press('down')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.press('up')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('space')
    time.sleep(0.1)


'''
HotKey Detection
'''
keyboard.add_hotkey('f4', lambda: snack())
keyboard.add_hotkey('f5', lambda: armor())
keyboard.add_hotkey('f9', lambda: kill())
keyboard.add_hotkey('f12', lambda: unblock())
keyboard.add_hotkey('f11', lambda: block())
keyboard.wait()
