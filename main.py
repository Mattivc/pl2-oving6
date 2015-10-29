from bbcon import Bbcon
from behaviours.avoid_line_behaviour import AvoidLineBehaviour
from sensobs.line_sensob import LineSensob
from sensors import *

if __name__ == '__main__':
    bb = Bbcon()

    ir_sensor = ir.ReflectanceSensors(auto_calibrate=True)
    line_sensob = LineSensob(ir_sensor)
    avl = AvoidLineBehaviour(bb, line_sensob)

    bb.add_sensor(ir_sensor)
    bb.add_sensory_object(line_sensob)
    bb.add_behaviour(avl)

    while bb.run_one_timestep():
        print("Pi keeps on running.")

    print("Pi halted.")