'''Contains sensors.
The base sensor class Sensor is available as sensors.
Submodules are automatically imported as following:
* camera 		: cam
* reflectance_sensors 	: ir
* ultrasonic 		: sonic

To use, say camera, write:
	import sensors
	cam = sensors.cam.Camera()
'''

# All files in this directory is now in the package sensor

from sensor.sensor import *
import sensor.camera as cam
import sensor.reflectance_sensors as ir
import sensor.ultrasonic as sonic