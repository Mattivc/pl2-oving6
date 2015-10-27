__author__ = 'kristian'
import behaviours.behaviour as behav

class AvoidLineBehaviour(behav.Behaviour):
    """Behaviour to avoid lines. Uses ir sensor."""

    def __init__(self, bbcon, ir_sensob):
        """
        :param bbcon: Bbcon
        :param ir_sensob:
        :return:
        """
        super().__init__(bbcon, list(ir_sensob))

