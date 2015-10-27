
class Behaviour(object):
    """Base class for behaviours.
    Behaviours can never directly communicate with each other.
    Main methods are update(), consider_deactivation(), consider_activation(), sense_and_act().

    Subclassing:
    Remember to call constructor and override the static constant PRIORITY.
    self.match_degree should be altered on updates using set_match_degree(degree)

    Important state variables are self.active_flag, self.halt_request, self.match_degree.
    An update should alter self.motor_reccomendations.

    Override these methods:
        * sense_and_act
        * consider_deactivation
        * consider_activation
    """

    PRIORITY = 20

    def __init__(self, bbcon, sensobs):
        """:param bbcon: Bbcon that uses this behaviour
        :param sensobs: list sensor objects that this behaviour uses
        """
        self.bbcon = bbcon                  # Bbcon that uses this object
        self.sensobs = sensobs              # List of sensor objects
        self.motor_reccomendations = None   # List of motor reccomendations, one per motob
        self.active_flag = True             # Sets if this behaviour is active
        self.halt_request = False           # Tracks if this behaviour wants the robot to stop execution
        self.match_degree = 0.5             # How valid is the reccomendation, based on current conditions. Range [0,1]
        self.weight = 0                     # Used by the Arbitrator
        self.update_weight()

    def update_weight(self):
        self.weight = self.PRIORITY * self.match_degree

    def set_match_degree(self, degree):
        self.match_degree = degree
        self.update_weight()

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
            self.sense_and_act()  # FIXME: Should sense come before consider_deactivation?
            self.update_weight()
        else:
            self.consider_activation()

    def consider_deactivation(self):
        """Alters self.active_flag when it is True
        :return: None"""
        pass

    def consider_activation(self):
        """Alters self.active_flag when it is False
        :return: None"""
        pass

    def sense_and_act(self):
        """Main sensor method.
        Called when self.active_flag is true.
        Should update self.match_degree
        :return: None
        """
        pass