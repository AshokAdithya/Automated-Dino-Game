# Automated dino game using pyautogui in Dark Mode

import pyautogui as pa
from PIL import Image,ImageGrab
import time

def hit(key):
    pa.keyDown(key)

def collide(data):
    for i in range(300,415):
        for j in range(563,650):
            if data[i,j]<100 and data[i,j]>10:
                hit("up")
                return 
    for i in range(300,415):
        for j in range(410,563):
            if data[i,j]<100 and data[i,j]>10:
                hit("down")
                return
    return 


if __name__=="__main__":
    time.sleep(3)
    hit("up")
    while True:
        image=ImageGrab.grab().convert("L")
        data=image.load()
        collide(data)
