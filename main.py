from bbcon import Bbcon
from behaviours.avoid_line_behaviour import AvoidLineBehaviour
from sensobs.line_sensob import LineSensob
from sensors import *
from robot.motors import Motors
from motob import WheelMotob

if __name__ == '__main__':
    bb = Bbcon()

    # Line detection
    ir_sensor = ir.ReflectanceSensors(auto_calibrate=True)
    line_sensob = LineSensob(ir_sensor)
    avl = AvoidLineBehaviour(bb, line_sensob)

    bb.add_sensor(ir_sensor)
    bb.add_sensory_object(line_sensob)
    bb.add_behaviour(avl)
    bb.activate_behaviour(avl)

    # Motor

    motors = Motors()
    wheel_motob = WheelMotob(motors, bb.time_step)
    bb.motobs.append(wheel_motob)


    try:
        while bb.run_one_timestep():
            print("Pi keeps on running.")
    except Exception as e:
        print("Exception occurred! "+str(e))
        # stop motor etc
        motors.stop()
        if isinstance(e, KeyboardInterrupt):
            raise e

    print("Pi halted.")