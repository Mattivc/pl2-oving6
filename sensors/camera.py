import os
from PIL import Image
import picamera
import time
import io
import sensors.sensor as sensor

class Camera(sensor.Sensor):

    def __init__(self, img_width=128, img_height=96, img_rot=0):
        '''img_rot is one of (0, 90, 180, 270)'''
        super().__init__()
        
        self.value = None
        self.img_width = img_width
        self.img_height = img_height
        self.img_rot = img_rot

    def get_value(self):
        return self.value

    def update(self):
        self.sensor_get_value()
        return self.value

    def reset(self):
        self.value = None

    def sensor_get_value(self):
        # This is a OS call that takes a image and makes it accessible to PIL operations in the same directory
        #os.system('raspistill -t 1 -o image.png -w "' + str(self.img_width) + '" -h "' + str(self.img_height) + '" -rot "' + str(self.img_rot) + '"')
        # Open the image just taken by raspicam
        # Stores the RGB array in the value field
        #self.value = Image.open('image.png').convert('RGB')

        # Nei takk, keith.
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
                camera.resolution = (self.img_width, self.img_height)
                camera.rotation = self.img_rot
                #camera.start_preview()
                #time.sleep(0.1)
                camera.capture(stream, format="jpeg")
        stream.seek(0)
        self.value = Image.open(stream)

# Just testing the camera in python

# os.system('raspistill -t 1 -o image.png -w "' + str(200) + '" -h "' + str(200) + '" -rot "' + str(0) + '"')