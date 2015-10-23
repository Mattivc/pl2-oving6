'''Contains sensors.
The base sensor class Sensor is available as sensors.
Submodules are automatically imported as following:
* camera 		: cam
* reflectance_sensors 	: ir
* ultrasonic 		: sonic

To use, say camera, write:
	import sensor
	cam = sensor.cam.Camera()
'''

# All files in this directory is now in the package sensor

from sensors.sensor import *
import sensors.camera as cam
import sensors.reflectance_sensors as ir
import sensors.ultrasonic as sonic