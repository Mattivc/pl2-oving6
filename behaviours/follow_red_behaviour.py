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
        self.active_flag = False

    def sense_and_act(self):
        red_detector = self.sensobs[0]

        if not isinstance(red_detector, RedDetector):
            raise Exception("Invalid type red_detector: " + str(type(red_detector)))

        red_position = red_detector.get_red_position()

        left = abs(1.0-red_position)/2.0
        right = abs(red_position)/2.0

        left = min(left, 1.0)
        right = min(right, 1.0)

        print("\033[91mRed position: "+str(red_position)+ ", left: %.3f\tright:%.3f"%(left, right) +"\033[0m")

        recommendation = [make_recommendation(left, right)]
        self.motor_recommendations = [recommendation]

        confidence = red_detector.get_confidence()
        print("RED confidence: {}".format(confidence))
        self.set_match_degree(confidence)