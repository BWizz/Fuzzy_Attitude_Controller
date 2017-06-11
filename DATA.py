# Yu Hin Hau
# 4/19/2014
# Data Class

class Data():

    def __init__(self):

        # Throttle Data
        self.throttle = 0

        # Attitude Data from IMU
        self.roll = 0
        self.pitch = 0
        self.yaw = 0

        self.roll_d = 0
        self.pitch_d = 0
        self.yaw_d = 0

        self.accel_x = 0	# front
        self.accel_y = 0	# right
        self.accel_z = 0	# down

        self.roll_t = 0
        self.pitch_t = 0
        self.yaw_t = 0

        # Altitude Data from Ultrasonic Sensor and Altimeter
        self.u_range = 0
        self.altitude = 0

        self.height = 0
        self.height_t = 0

        # Voltage Divider to Detect Battery Status
        self.v_motor = 0
        self.v_comp = 0

        # GPS Positioning Data
        self.gps_fixed = 'f'	 # t - true / f - false
        self.longitude = 35.2568 # might need *100000 and send as long to reduce error
        self.latitude = -75.3254

        self.longitude_t = 35.2561
        self.latitude_t = -75.3220

        self.heading = 0
        self.velocity = 0

        # Control Mode
        self.control_mode = 'm' # a - auto / m - radio manual
        self.flight_mode = 'd' # t - take_off / c - cruise / k - landing / m - gui manual

        # Radio PWM Command
        self.pwm_roll = 0
        self.pwm_pitch = 0
        self.pwm_yaw = 0
        self.pwm_throttle = 0
        self.pwm_aux = 0

        # PID Controller Gains
        self.K_Pr = 60
        self.K_Ir = 20
        self.K_Dr = 3

        self.K_Pp = 50
        self.K_Ip = 10
        self.K_Dp = 2

        self.K_Py = 40
        self.K_Iy = 30
        self.K_Dy = 10

        self.K_D = 2

        # PID Controller Integral Values
        self.rI = 0
        self.pI = 0
        self.yI = 0


