__author__ = 'Marius'
import behaviours.behaviour as behav
from sensobs.ultra_sensob import UltraSensob

class AvoidCollisionBehaviour(behav.Behaviour):
    '''Behaviour to stop the robot to avoid collisions'''

    def __init__(self, bbcon, ultra_sensob):

        if not isinstance(ultra_sensob, UltraSensob):
            raise Exception("Invalid type for line_sensob: "+type(ultra_sensob))

        super().__init__(bbcon, list(ultra_sensob))




    def sense_and_act(self):
        self.distance = UltraSensob.update()
        if self.distance <= 1:
            self.motor_reccomendations.append(('L', 0))     #reccomends the motors to stop (what to put in the first index of the tuple?)
            self.set_match_degree(0.9)                      #sets a high match degree
        else:
            self.set_match_degree(0.5)

    def consider_deactivation(self):      #ultrasonic sensor should always be active?
        pass

    def consider_activation(self):     #activates the sensor if it is not active
        if not self.active_flag:
            self.active_flag = True
