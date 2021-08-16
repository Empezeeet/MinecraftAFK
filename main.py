#Script for safe afking in Minecraft survival.
#If you lose 0.5 heart of HP script will automatically disconnect you from server (if on server) or save and quit to main menu

import time
import keyboard
import mouse
import PIL.ImageGrab
import winsound as sound


startHotkey = 'ctrl + shift + F7'
stopHotkey = 'ctrl + shift + F8'

status = False #FALSE = Disabled, TRUE = Enabled


no_heartColor_RED, no_heartColor_GREEN, no_heartColor_BLUE = 40, 40, 40

#heartColor_RED, heartColor_GREEN, heartColor_BLUE = 255, 19, 19

heartPos_x, heartPos_y = 920, 931

logoutButton_x, logoutButton_y = 962, 618






def logout():
    print("Deteted Risk!")
    keyboard.press_and_release('escape')
    time.sleep(0.05)
    mouse.move(logoutButton_x, logoutButton_y)
    mouse.click()
    sound.PlaySound('warning3.wav', sound.SND_FILENAME)
    exit()


print('Watching!')
while True:
    pixel = PIL.ImageGrab.grab().load()[heartPos_x, heartPos_y]
    if (pixel[0] == 40) and (pixel[1] == 40) and (pixel[2] == 40):
        logout()
    else:
        pass

#End of scirpt