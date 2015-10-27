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

        super().__init__(bbcon, list(line_sensob))
