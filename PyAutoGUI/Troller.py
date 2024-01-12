import pyautogui, time, webbrowser, random

def losowa_strona():
	number = random.randint(1, 3)
	if number == 1:
		webbrowser.open('https://attachment.zip/')
	if number == 2:
		webbrowser.open('https://guthib.com/')
	if number == 3:
		webbrowser.open('https://steve78392.github.io/')
	
def klawiatura_cyfry():
	cyfra = random.randint(824014, 9999999999999)
	pyautogui.write(str(cyfra))
	
def usuwanie_tekstu():
	pyautogui.hotkey('ctrl', 'a')
	time.sleep(0.1)
	pyautogui.press('backspace')
	
def zamykanie_programow():
	for i in range(10):
		pyautogui.hotkey('alt', 'f4')
	
def klawisz_windows():
	for i in range(100):
		pyautogui.press('win')
		time.sleep(0.1)

def otwieranie_i_zamykanie_programow():
	for i in range(15):
		liczbaprogram = random.randint(1, 9)
		pyautogui.hotkey('win', str(liczbaprogram))
		pyautogui.sleep(random.randint(1, 2))

def cmd_rickroll():
    pyautogui.hotkey('winleft', 'r')
    pyautogui.write('cmd\n')
    time.sleep(0.7)
    pyautogui.press('f11')
    pyautogui.write('curl ascii.live/rick\n')

while True:
	zadanie = random.randint(1, 7)
	if zadanie == 1:
		losowa_strona()
	if zadanie == 2:
		klawiatura_cyfry()
	if zadanie == 3:
		usuwanie_tekstu()
	if zadanie == 4:
		zamykanie_programow()
	if zadanie == 5:
		klawisz_windows()
	if zadanie == 6:
		otwieranie_i_zamykanie_programow()
	if zadanie == 7:
		cmd_rickroll()
	time.sleep(15)
