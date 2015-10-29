from bbcon import Bbcon
from behaviours.avoid_line_behaviour import AvoidLineBehaviour
from behaviours.follow_red_behaviour import FollowRedBehaviour
from sensobs.line_sensob import LineSensob
from sensobs.red_detector import RedDetector
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


    # Camera

    camera_sensor = cam.Camera(img_rot=180)
    follow_red_sensob = RedDetector(camera_sensor)
    follow_red_behaviour = FollowRedBehaviour(bb, follow_red_sensob)
    bb.add_sensor(camera_sensor)
    bb.add_sensory_object(follow_red_sensob)
    bb.add_behaviour(follow_red_behaviour)
    bb.activate_behaviour(follow_red_behaviour)

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