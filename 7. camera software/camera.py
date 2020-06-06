from picamera import PiCamera
from time import sleep
from datetime import datetime
import os

#create the image directory if not exists
directory = "/home/pi/reef-mapping/"
if not os.path.exists(directory):
    os.makedirs(directory)

#start the camera
camera = PiCamera()
camera.start_preview()

try:
    while True:
        sleep(3)
        now = datetime.now()
        date_time = now.strftime("%Y%m%d_%H%M%S") #20200615_143050
        file_name = directory + date_time + '.jpg'
        # TODO check file doesnt exist before saving
        camera.capture(file_name) # save file inside directory, with timestamp
finally:
    # stop the preview on SIGINT (i.e. CTRL + C)
    camera.stop_preview()
