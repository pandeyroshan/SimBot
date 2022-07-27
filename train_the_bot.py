import os
import pyautogui
import time
import constants
import keyboard
from gtts import gTTS

def start_tracking_cursor():
    print("Inside tracking cursor")
    TRACK_MODE = constants.SCREEN_MODE
    
    while True:
        if TRACK_MODE == constants.SCREEN_MODE:
            while True:
                if keyboard.is_pressed(constants.KEYBOARD_CTRL):
                    cursor_location = pyautogui.position()
                    print(cursor_location)
                    time.sleep(0.3)
                elif keyboard.is_pressed(constants.KEYBOARD_ALT):
                    print("SWITCHED MODE TO KEYBOARD")
                    TRACK_MODE = constants.KEYBOARD_MODE
                    time.sleep(0.3)
                    break
        elif TRACK_MODE == constants.KEYBOARD_MODE:
            word = ""
            while True:
                recording = keyboard.record()
                print(recording)
                time.sleep(2)
                keyboard.play(recording)
                if keyboard.is_pressed(constants.KEYBOARD_ALT):
                    print("SWITCHED MODE TO SCREEN")
                    TRACK_MODE = constants.SCREEN_MODE
                    time.sleep(0.3)
                    print(word)
                    break

def train_the_bot():
    print("Inside Training Bot")
    os.system('notify-send "{}" "{}"'.format(constants.BOT_TRAINING, constants.BOT_TRAINING_MESSAGE))
    time.sleep(3)
    start_tracking_cursor()

if __name__=='__main__':
    # train_the_bot()
    HelloMessage = "Hello Roshan, I'm Symbot, your virtual assistant at your service"
    myobj = gTTS(text=HelloMessage, lang='en', slow=False)
    myobj.save("welcome.mp3")