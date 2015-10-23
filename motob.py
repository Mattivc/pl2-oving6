

class Motob(object):
    '''Motor object. Main method is update(reccomendation).'''
    
    def __init__(self):
        self.motors = []    # List of motors
        self.value = None   # Most recent motor reccomendation received

    def update(self, reccomendation):
        '''Sets the reccomendation, and calls operationalize to activate motors
        '''
        self.value = reccomendation
        self.operationalize()

    def operationalize(self):
        '''Converts the motor reccomendation into a set of
         motor settings, which are then sent to the motors.
         '''
        pass
