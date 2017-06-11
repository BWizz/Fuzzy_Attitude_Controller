from fuzzyCONTROLLER import Fuzzycontroller 
from DATA import Data
import time
from UM6 import Imu
from MOTOR import Motor
import Adafruit_BBIO.UART as UART
desired=[[0,0,0],[0,0,0]]
throttlemin=320 # MAX throttle PWM signal 420
throttlemax=370
data=Data()
controller=Fuzzycontroller(desired)

UART.setup("UART1")
imu=Imu('/dev/ttyO1')
imu.calibrate()	
UART.setup("UART2")
motor = Motor('/dev/ttyO2')
motor.arm()

start=time.time()
flight=1
mode='B'
throttle=throttlemin
start=time.time()
Left  =1
Right =5
Front =3
Back =2
while flight ==1:
	throttle = throttle + 1
	if throttle>= throttlemax:
		throttle=throttlemax
	ti=time.time()
	imu.stateUpdate(data)
	tf=time.time()
	dt=tf-ti
	error,errorRate,OUT,PWMmot=controller.control(data,throttle)
	# Write PWM signal to proper channel
	motor.writeChannel(Left, PWMmot[0])
	motor.writeChannel(Right,PWMmot[1])
	motor.writeChannel(Front,PWMmot[2])
	motor.writeChannel(Back, PWMmot[3])
	# print data.roll
	
	# print 'roll Rate',data.roll_d,'Pitch Rate',data.pitch_d
	#print PWMmot
	if time.time()-start>30:
		flight=0
	
	# if mode=='H': #Hove Mode
	# 	imu.stateUpdate(data)
	# 	error,errorRate,OUT,PWMmot=controller.control(data,throttle)
	# 	# Write PWM signal to proper channel
	# 	Left  =0
	# 	Right =1
	# 	Front =2
	# 	Back =3
	# 	motor.writeChannel(Left, PWMmot[0])
	# 	motor.writeChannel(Right,PWMmot[1])
	# 	motor.writeChannel(Front,PWMmot[2])
	# 	motor.writeChannel(Back, PWMmot[3])
	# 	#need an IF stament to terminate flight
	# if mode=='L': #Landing Mode
	# 	throttle=throttle-10
	# 	imu.stateUpdate(data)
	# 	error,errorRate,OUT,PWMmot=controller.control(data,throttle)
	# 	# Write PWM signal to proper channel
	# 	Left  =1
	# 	Right =5
	# 	Front =3
	# 	Back =2
	# 	motor.writeChannel(Left, PWMmot[0])
	# 	motor.writeChannel(Right,PWMmot[1])
	# 	motor.writeChannel(Front,PWMmot[2])
	# 	motor.writeChannel(Back, PWMmot[3])
	# 	if throttle<100:
	# 		flight=0
		
motor.disarm()

# Close Device
motor.close()


