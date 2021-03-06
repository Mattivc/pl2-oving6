

import time
from arbitrator import Arbitrator
from sensors.camera import Camera
from motob import WheelMotob
from motob import Motob
import threading


class Bbcon(object):
    def __init__(self, time_step=0.2):
        """:param time_step: float time in seconds between to wait after each time step
        """
        self.sensors = []               # All sensors
        self.behavs = []                # All behaviours
        self.active_behavs = []         # Active behaviours
        self.sensobs = []               # Sensory objects
        self.motobs = []                # Motor objects
        self.arbit = Arbitrator(self)   # Arbitrator
        self.time_step = time_step

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def remove_sensor(self, sensor):
        try:
            self.sensors.remove(sensor)
        except ValueError:
            pass

    def add_behaviour(self, behaviour):
        self.behavs.append(behaviour)

    def add_sensory_object(self, sensory_object):
        self.sensobs.append(sensory_object)

    def activate_behaviour(self, behaviour):
        self.active_behavs.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        """Remove behaviour.
        :return: boolean True if removed, False otherwise
        """
        try:
            self.active_behavs.remove(behaviour)
        except ValueError:
            return False
        else:
            return True


    def set_arbit(self, arbitrator):
        self.arbit = arbitrator

    def run_one_timestep(self):
        """
        Returns if execution should continue.
            False => Halt, stop program
            True  => Keep running
        :return: bool
        """

        print("="*50)
        print()

        forks = []

        # Update sensors
        for sensor in self.sensors:
            if isinstance(sensor, Camera):
                thread = threading.Thread(target=sensor.update)
                forks.append(thread)
                thread.start()
            else:
                sensor.update()

        for fork in forks:
            fork.join()

        forks = []
        # Update sensobs
        for sensob in self.sensobs:
            thread = threading.Thread(target=sensob.update)
            forks.append(thread)
            thread.start()

        for fork in forks:
            fork.join()

        # Update behaviours
        for behav in self.active_behavs:
            behav.update()

        # Invoke arbitrator
        motor_rec = self.arbit.choose_action()     # Returns a tuple(list(motor_recommendations), halt)
        print("Arbitrator chose: "+str(motor_rec))

        if motor_rec[1]:  # Check halt recommendation
            return False  # Halt and exit program


        # Update motobs
        print(self.motobs)
        i = 0
        for motob in self.motobs:     # Updates each motob with it's respective motor recommendation
            print("Bbcon: Updating motob " + str(i))

            motob.update(motor_rec[0][i])
            i += 1

        # Wait
        time.sleep(0.5)    #waits half a second

        # Reset sensors
        for sensor in self.sensors:
            sensor.reset()

        return True