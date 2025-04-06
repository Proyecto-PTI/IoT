import time
import os

while True:
    os.system('fswebcam -r 1920x1080 --save ~/Documents/image.jpeg')

    time.sleep(1)
