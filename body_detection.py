import cv2
from pynput.keyboard import Key, Controller
import time

# Checks for objects and sees if its a person or not, add in face feature aswell 
# This script stops media / plays media if it detects a person

# Se keyboard as a controller 
keyboard = Controller()

# Get the default detector for people
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Get camera video feed 
camera_feed = cv2.VideoCapture(0)

# Set how long to wait before seconds 
wait_time = 3

pause = False
while True:
    check, frame = camera_feed.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)

    people = weights
    # print(frame)

    # If there is more than one person on screen
    if len(people) > 0:
        if pause == True:
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause) 
        pause = False
    else:
        if pause == False:
            time.sleep(wait_time)
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause) 
        pause = True

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
        
camera_feed.release()


