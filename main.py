from bbcon import Bbcon
from behaviours.avoid_line_behaviour import AvoidLineBehaviour
from sensobs.line_sensob import LineSensob
from sensors import *
from robot.motors import Motors
from motob import WheelMotob
from behaviours.avoid_collision_behaviour import AvoidCollisionBehaviour
from sensobs.ultra_sensob import UltraSensob
import sensors

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

    # Collision avoidance
    '''
    ultra_sensor = sensors.ultrasonic.Ultrasonic()
    ultra_sensob = UltraSensob(ultra_sensor)
    avc = AvoidCollisionBehaviour(bb, ultra_sensob)

    bb.add_sensor(ultra_sensor)
    bb.add_sensory_object(ultra_sensob)
    bb.add_behaviour(avc)
    bb.activate_behaviour(avc)
    '''
    # Motor

    motors = Motors()
    wheel_motob = WheelMotob(motors, bb.time_step)
    bb.motobs.append(wheel_motob)


    try:
        while bb.run_one_timestep():
            print("Pi keeps on running.")
    except Exception as e:
        # stop motor etc
        print("Stopping motor")
        motors.stop()
        if isinstance(e, KeyboardInterrupt):
            raise e
        # found no good way to print stacktrace, raising instead. -kriss
        raise e

    print("Pi halted.")