
import time

class Bbcon(object):

    def __init__(self, time_step=0.2):
        ''':param time_step: float time in seconds between to wait after each time step
        '''
        self.sensors = []           # All sensors
        self.behavs = []            # All behaviours
        self.active_behavs = []     # Active behaviours
        self.sensobs = []           # Sensory objects
        self.motobs = []            # Motor objects
        self.arbit = None          # Arbitrator
        self.time_step = time_step

        def add_behaviour(self, behaviour):
            self.behavs.append(behaviour)

        def add_sensory_object(self, sensory_object):
            self.sensobs.append(sensory_object)

        def activate_behaviour(self, behaviour):
            self.active_behavs.append(behaviour)

        def deactivate_behaviour(self, behaviour):
            '''Remove behaviour.
            :return: boolean True if removed, False otherwise
            '''
            try:
                self.active_behavs.remove(behaviour)
            except ValueError:
                return False
            else:
                return True

        def set_arbit(self, arbitrator):
            self.arbit = arbitrator

        def run_one_timestep(self):
            # Update sensors
            for sensob in self.sensobs:
                sensob.update()
            # Update behaviours

            # Invoke arbitrator
            motor_rec = self.arbit.choose_action()     #returns a tuple of (motor_recommendation, halt)


            # Update motobs
            i = 0
            for motob in self.motobs:     #updates each motob with it's respective motor recommendation
                motob.update(motor_rec(0)[i])
                i = i +1

            # Wait
            time.sleep(0.5)    #waits half a second

            # Reset sensobs
            for sensob in self.sensobs:     #resets each sensob in the list of sensobs
                sensob.reset()

        
