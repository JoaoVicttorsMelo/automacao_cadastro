import pyautogui as gui
import time


gui.PAUSE = 1
gui.press('win')
gui.write('opera')
gui.press('enter')
time.sleep(2)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
gui.write(link)
gui.press('enter')
time.sleep(6)
gui.click(x=447, y=390)

gui.write('teste@gmail.com')
time.sleep(4)
gui.press('tab')
gui.write('1234')
gui.press('tab')
gui.press('enter')
time.sleep(4)
gui.press('tab')


#print(gui.position())


