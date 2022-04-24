import time
import pyautogui

while True:
	screenWidth, screenHeight = pyautogui.size()
	screenWidth, screenHeight

	width_height = pyautogui.size()
	print(width_height)
	print(width_height[0])
	print(width_height[1])
	#pyautogui.mouseInfo()
	pyautogui.moveTo(10,10) # nex testination
	time.sleep(0.5)
	pyautogui.mouseDown()
	time.sleep(0.5) #or whatever you need, if even needed
	pyautogui.mouseUp()
