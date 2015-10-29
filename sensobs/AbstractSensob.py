from abc import abstractmethod

class AbstractSensob(object):
    '''Base class for all sensory objects.
    The main methods are update and __init__(Sensor...)
    '''

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass


