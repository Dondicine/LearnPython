import pyautogui as pg
import time

txt = '''123 '''
pg.moveTo(890, 300)
pg.click()
time1 = time.time()
for t in txt:
    time2 = time.time()
    if time2 - time1 < 15:
        pg.press(t)
        time.sleep(0.00001)
    elif 15 <= time2 - time1 < 30:
        pg.press(t)
        time.sleep(0.01)
    elif 30 <= time2 - time1 < 61:
        pg.press(t)
        time.sleep(0.001)
    elif time2 - time1 >= 61:
        break
