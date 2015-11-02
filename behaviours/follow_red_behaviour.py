__author__ = 'kristian'
from behaviours.behaviour import Behaviour
from sensobs.red_detector import RedDetector
from motob import make_recommendation

class FollowRedBehaviour(Behaviour):

    def __init__(self, bbcon, red_detector):
        if not isinstance(red_detector, RedDetector):
            raise Exception("Invalid type red_detector: " + str(type(red_detector)))
        super().__init__(bbcon, [red_detector])

        self.PRIORITY = 20


    def consider_activation(self):
        self.active_flag = True

    def consider_deactivation(self):
        self.active_flag = True

    def sense_and_act(self):
        red_detector = self.sensobs[0]

        if not isinstance(red_detector, RedDetector):
            raise Exception("Invalid type red_detector: " + str(type(red_detector)))

        red_position = red_detector.get_red_position()

        recommendation = [make_recommendation(red_position, -red_position)]
        self.motor_recommendations = [recommendation]

        confidence = red_detector.get_confidence()
        print("RED confidence: {}".format(confidence))
        self.set_match_degree(confidence)