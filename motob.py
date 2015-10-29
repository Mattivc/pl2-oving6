from abc import abstractmethod
from robot.motors import Motors

class Motob(object):
    """Motor object. Main method is update(reccomendation)."""
    
    def __init__(self):
        self.motors = []    # List of motors
        self.value = []     # Most recent motor reccomendation received

    def update(self, recommendation):
        """Sets the recommendation, and calls operationalize to activate motors
        :param recommendation: list
        """
        self.value = recommendation
        self.operationalize()

    @abstractmethod
    def operationalize(self):
        """Converts the motor reccomendation into a set of
         motor settings, which are then sent to the motors. This requires experimentation, since motor_rec is high level ex: (L, 30)
         and the motor class requires a vector on the form [-1, 1]
         """
        pass

def make_recommendation(left_wheel, right_wheel):
    """ Make a reccomendation for the motor motob.
    Arguments are in range [-1, 1] where negative means backwards
    :param left_wheel: float
    :param right_wheel: float
    :return: tuple[float, float]
    """
    return left_wheel, right_wheel

class WheelMotob(Motob):

    def __init__(self, motors, duration):
        """
        motors is the robot.Motors object to use.
        duration is a float indicating the time to run. Usually bbcon.time_step
        :param motors: Motors
        :param duration: float
        """
        super().__init__()
        if not isinstance(motors, Motors):
            raise Exception("Invalid type motors: "+type(motors))
        self.motors = [motors]
        self.duration = duration

    def operationalize(self):
        recommendation = self.value[0]
        motors = self.motors[0]

        if not isinstance(recommendation, tuple):
            print("Recommendation is not a tuple: "+str(recommendation) + type(recommendation))
            raise Exception("Recommendation is not tuple")

        motors.set_value(recommendation, self.duration)