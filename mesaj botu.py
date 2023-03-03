import pyautogui
import time 

süre = int(input("mesajınızın aralığı kaç saniye olsun istersiniz? :\t"))
time.sleep(3)

while True:
    f = open("mesaj.txt","r",encoding="utf-8")
    for word in f:
        time.sleep(süre)
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    f.close()
    time.sleep(1)
