__author__ = 'kristian'
import behaviours.behaviour as behav
from sensobs.line_sensob import LineSensob
from motob import make_recommendation

class AvoidLineBehaviour(behav.Behaviour):
    """Behaviour to avoid lines. Uses ir sensor."""

    def __init__(self, bbcon, line_sensob):
        """
        :param bbcon: Bbcon
        :param ir_sensob:
        :return:
        """
        if not isinstance(line_sensob, LineSensob):
            raise Exception("Invalid type for line_sensob: "+str(type(line_sensob)))
        super().__init__(bbcon, [line_sensob])

        self.PRIORITY = 50

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        line_sensob = self.sensobs[0]
        if not isinstance(line_sensob, LineSensob):
            raise Exception("Invalid type for line_sensob: "+str(type(line_sensob)))

        found_lines = line_sensob.get_found_lines()
        position = line_sensob.get_line_position()

        self.set_match_degree(1.0 if found_lines else 0.0)

        left_sign, right_sign = 1.0, 1.0        # Negate in if-test to reverse motor

        if position < 0.5:  # Line is left, drive right
            strength = position/0.5             # Map to [0, 1]
            right_sign = -1.0
        else:               # Line is right, drive left
            strength = (position-0.5)/0.5       # Map to [0, 1]
            left_sign = -1.0

        amount = max(0.05, 0.7*strength)    # Motor power capped to range [0.05, 0.7]
        recommendation = make_recommendation(amount*left_sign, amount*right_sign)
        self.motor_recommendations = [recommendation]
        print(self)

    def __str__(self):
        return "AvoidLineBehaviour "+str(self.motor_recommendations) + ", " +str(self.active_flag)