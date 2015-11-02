__author__ = 'Marius'
import behaviours.behaviour as behav
from sensobs.ultra_sensob import UltraSensob
from motob import make_recommendation

class AvoidCollisionBehaviour(behav.Behaviour):
    '''Behaviour to stop the robot to avoid collisions'''

    def __init__(self, bbcon, ultra_sensob):

        if not isinstance(ultra_sensob, UltraSensob):
            raise Exception("Invalid type for line_sensob: "+str(type(ultra_sensob)))

        super().__init__(bbcon, [ultra_sensob])
        self.PRIORITY = 100

    def sense_and_act(self):
        ultra_sensob = self.sensobs[0]
        if not isinstance(ultra_sensob, UltraSensob):
            raise Exception("Invalid type for line_sensob: "+str(type(ultra_sensob)))

        distance = ultra_sensob.get_value()

        if distance <= 1:
            recommendation = [make_recommendation(0, 0)]
            self.motor_recommendations = [recommendation]     #recommends the motors to stop
            self.set_match_degree(1.0)                      #sets a high match degree
        print(self)

    def consider_deactivation(self):
        # should ultrasonic sensor always be active?
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True


    def __str__(self):
        return "AvoidCollisionBehaviour "+str(self.motor_recommendations) + ", active: " +str(self.active_flag) + ", weight: " + str(self.weight)