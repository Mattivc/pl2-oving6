from abc import abstractmethod

class Sensor(object):
    '''Base class for sensors.
    The main methods are update and get_value'''

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def reset(self):
        pass