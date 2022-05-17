import pyautogui as pg
import pyperclip
import time
pg.PAUSE=1
pg.press('win')
pg.write('chrome')
pg.press('enter')
time.sleep(8)
pg.click(x=761, y=533) #selecionar meu perfil no chrome
pg.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pg.hotkey('ctrl', 'v')
pg.press('enter')
time.sleep(20)
pg.click(x=349, y=272, clicks=2) #clicar para abrir a pasta
time.sleep(10)
pg.click(x=347, y=449)
time.sleep(10)
pg.click(x=1161, y=163)
time.sleep(10)
pg.click(x=956, y=558)
time.sleep(5)

'''time.sleep(5)
pos = pg.position()
print(pos)'''  #achar a posição do mouse


