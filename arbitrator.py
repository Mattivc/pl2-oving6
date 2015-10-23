


class Arbitrator(object):
    '''Main method is choose_action().'''

    def __init__(self, bbcon):
        ''':param bbcon: Bbcon that uses this arbitrator
        '''
        self.bbcon = bbcon
        
    def choose_action(self):
        '''Returns a tuple where the first element is a list of
        motor reccomendations, where
            len(list) == len(bbcon.motobs)
        and the second element is a boolean indicating if the robot
        should halt.
        :return: tuple ([motor_reccomendations], halt)
        '''
        raise Exception("Not implemented")
    
