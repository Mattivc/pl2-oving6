import sensobs.sensob as sensob
from sensors.reflectance_sensors import ReflectanceSensors

class LineSensob(sensob.Sensob):
    """Sensory object for lines.
    Use get_line_position() and get_found_lines().
    Always call update() once before using get_*.
    """

    BLACK = 0.0
    WHITE = 1.0

    def __init__(self, ir_sensor, lines_are_black=True):
        """
        Takes in an ir-sensor from sensors package.
        Lines are assumed to be black tape on a white background.
            Set lines_are_black=False if the lines are not black tape.
        :param ir_sensor: sensors.ir.ReflectanceSensors
        :param lines_are_black: bool
        """
        super().__init__()
        if not isinstance(ir_sensor, ReflectanceSensors):
            raise Exception("Invalid argument ir_sensor: wrong type "+type(ir_sensor))

        self.ir_sensor = ir_sensor
        self.threshold = 0.35        # 35% of [min, max] is counted as a line. [0, 0.2] for black lines
        self.black_lines = lines_are_black
        self.line_position = 0
        self.found_lines = False


    def update(self):
        sensor_float_list = self.ir_sensor.get_value()                  # 6 floats
        line_positions = list(map(self._is_black, sensor_float_list))   # 6 bool
        print("LineSensob:"+str(sensor_float_list)+"\t"+str(line_positions))

        # Find longest subsequence of sensors that detected a line.
        position_str = "".join("1" if pos else "0" for pos in line_positions)
        print("LineSensob: "+position_str)
        try:
            biggest_subsequence = max(map(len, position_str.split("0")))    # throws if empty list
            self.found_lines = True
            pos = position_str.find("1"*biggest_subsequence)    # index from 0 to 5
            pos += biggest_subsequence//2                       # Middle of sensors
            self.line_position = pos / 6
            print("LineSensob: Line pos: "+str(self.line_position))
        except ValueError:
            # Empty list; no line detected
            self.found_lines = False

    def _is_black(self, value):
        """
        value is a float in range [0, 1]
        :param value: float
        :return: bool
        """
        # If BLACK and WHITE are not 0 and 1, threshold must also be multiplied
        # with (WHITE-BLACK).
        if self.black_lines:
            return value < self.threshold
        else:
            return value > 1 - self.threshold


    def get_line_position(self):
        """
        Returns a value in the range [0,1] where 0 is left, and 1 is right.
        If get_found_lines returns False, this data is invalid.
        :return: bool
        """
        return self.line_position

    def get_found_lines(self):
        """
        Returns true if any line was found. If false, get_line_position is contains invalid data.
        :return: bool
        """
        return self.found_lines