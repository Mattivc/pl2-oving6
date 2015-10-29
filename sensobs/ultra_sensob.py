__author__ = 'Marius'
import sensobs.sensob as sensob
from sensors.ultrasonic import Ultrasonic


class UltraSensob(sensob.Sensob):
    """Sensory object for Ultrasonic.
    Use get_value().
    Always call update() once before using get_*.
    """

    def __init__(self, ultrasonic_sensor):
        ''' trigger pin hardcoded to 26
        echo pin hardcoded to 11
        '''
        super().__init__()
        if not isinstance(ultrasonic_sensor, Ultrasonic):
            raise Exception("Invalid argument ultrasonic_sensor: wrong type "+type(ultrasonic_sensor))

        self.ultrasonic_sensor = ultrasonic_sensor
        self.distance = None

    def update(self):
        self.distance = self.ultrasonic_sensor.update()

    def get_value(self):
        if self.distance:
            return self.distance
        else:
            raise Exception("Distance is None")




