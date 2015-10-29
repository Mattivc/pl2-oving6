__author__ = 'kristian'
from behaviours.behaviour import Behaviour

class FollowRedBehaviour(Behaviour):
    def consider_activation(self):
        self.active_flag = True

    def consider_deactivation(self):
        self.active_flag = True

    def sense_and_act(self):
        pass