__author__ = 'kristian'
import behaviours.behaviour as behav
from sensobs.line_sensob import LineSensob

class AvoidLineBehaviour(behav.Behaviour):
    """Behaviour to avoid lines. Uses ir sensor."""

    def __init__(self, bbcon, line_sensob):
        """
        :param bbcon: Bbcon
        :param ir_sensob:
        :return:
        """
        if not isinstance(line_sensob, LineSensob):
            raise Exception("Invalid type for line_sensob: "+type(line_sensob))
        super().__init__(bbcon, [line_sensob])

        self.PRIORITY = 50

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        line_sensob = self.sensobs[0]
        if not isinstance(line_sensob, LineSensob):
            raise Exception("Invalid type for line_sensob: "+type(line_sensob))

        found_lines = line_sensob.get_found_lines()
        position = line_sensob.get_line_position()

        self.set_match_degree(1.0 if found_lines else 0.0)



