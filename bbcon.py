


class Bbcon(object):

    def __init__(self):
        self.behavs = []            # All behaviours
        self.active_behavs = []     # Active behaviours
        self.sensobs = []           # Sensory objects
        self.motobs = []            # Motor objects
        self.arbit = None           # Arbitrator

        def add_behaviour(self, behaviour):
            self.behavs.append(behaviour)

        def add_sensory_object(self, sensory_object):
            self.sensobs.append(sensory_object)

        def activate_behaviour(self, behaviour):
            self.active_behavs.append(behaviour)

        def deactivate_behaviour(self, behaviour):
            '''Remove behaviour.
            :return: True if removed, False otherwise
            '''
            try:
                self.active_behavs.remove(behaviour)
            except ValueError:
                return False
            else:
                return True
