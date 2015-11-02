from bbcon import Bbcon
from behaviours.avoid_line_behaviour import AvoidLineBehaviour
from behaviours.follow_red_behaviour import FollowRedBehaviour
from sensobs.line_sensob import LineSensob
from sensobs.red_detector import RedDetector
from sensors import *
from robot.motors import Motors
from motob import WheelMotob
from behaviours.avoid_collision_behaviour import AvoidCollisionBehaviour
from sensobs.ultra_sensob import UltraSensob
from sensors.ultrasonic import Ultrasonic

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


    # Camera

    camera_sensor = cam.Camera(img_rot=180)
    follow_red_sensob = RedDetector(camera_sensor)
    follow_red_behaviour = FollowRedBehaviour(bb, follow_red_sensob)
    bb.add_sensor(camera_sensor)
    bb.add_sensory_object(follow_red_sensob)
    bb.add_behaviour(follow_red_behaviour)
    bb.activate_behaviour(follow_red_behaviour)


    # Ultrasonic

    ultra_sonic_sensor = Ultrasonic()
    collision_sensob = UltraSensob(ultra_sonic_sensor)
    collision_behaviour = AvoidCollisionBehaviour(bb, collision_sensob)
    bb.add_sensor(ultra_sonic_sensor)
    bb.add_sensory_object(collision_sensob)
    bb.add_behaviour(collision_behaviour)
    bb.activate_behaviour(collision_behaviour)


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