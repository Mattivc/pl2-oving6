
import random

class Arbitrator(object):
    '''Main method is choose_action().'''

    def __init__(self, bbcon):
        ''':param bbcon: Bbcon that uses this arbitrator
        '''
        self.bbcon = bbcon
        
    def choose_action(self):
        '''Returns a tuple where the first element is a list of
        motor recommendations, where
            len(list) == len(bbcon.motobs)
        and the second element is a boolean indicating if the robot
        should halt.
        :return: ([motor_recommendations], halt)
        '''
        ranges = []   #list of tuples with ranges for stochastic choosing
        i = 0
        prev = 0
        sum = 0
        winner = None
        for behav in self.bbcon.active_behavs:         #creates ranges of weights for stochastic choosing
            print("Arbitrator: examining behaviour: "+str(behav))
            ranges.append((prev, behav.weight))
            i = i + 1
            prev = behav.weight
            sum = sum + behav.weight
        random_number = random.uniform(0, sum)     #generates a random number between 0 and the sum of the weights
        for entry in ranges:                       #checks which range the random number is in
            r = (entry[0], entry[1])
            print("Arbitrator: looking at range "+str(r))
            if r[0] < random_number < r[1]:
                print("\033[94mArbitrator: found winner: "+str(ranges.index(entry)) + "\033[0m")
                winner = ranges.index(entry)       #sets winner to the index of the winning range
                break
        if winner is not None:
            return (self.bbcon.active_behavs[winner].motor_recommendations, self.bbcon.active_behavs[winner].halt_request)    #returns a tuple containing motor recommendations and halt_request
        else:
            return [[(0.0, 0.0)]], False  # This just helps IntelliJ understant the return type.
