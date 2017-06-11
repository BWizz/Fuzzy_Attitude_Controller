from FUZZIFY_V2 import Fuzzify
from INFERENCE import Inference as inf
from DEFUZZIFY import Defuzzify
# import pylab as py
# import matplotlib.pyplot as plt
import time


# from DATA import Data
# from IMU import Imu


defuzz=Defuzzify()
fuzzy=Fuzzify()
inf=inf()

desiredAngle=10
desiredRoll=desiredAngle*.0055555556
desiredVelocity=0

# imu=Imu('/dev/ttyUSB1')
# data=Data()
STOP=100
OUTPUT=[0]*STOP
roll=[25]*STOP
roll_d=[3000]*STOP
t=[0]*STOP
ii=0
start=time.time()
while ii != STOP:
	t[ii]=time.time()-start
	# imu.stateUpdate(data)
	#Scaling Law
	roll=.0055555556*25
	rolld=.004166667*1000


	Position_Error=roll-desiredRoll
	Velocity_Error=rolld-desiredVelocity
	eFuzzy,edFuzzy=fuzzy.Fuzzy(Position_Error,Velocity_Error)
	OUTPUT[ii]=defuzz.Defuzz(inf.Mnd(eFuzzy,edFuzzy))
	dt=(time.time()-start)-t[ii]
	print dt
	ii=ii+1



# plt.plot(t,OUTPUT,label='Roll OUTPUT')
# plt.ylabel('IMU OUTPUT')
# plt.xlabel('Time (sec)')
# plt.title('IMU Data')
# plt.legend(loc='lower right')
# plt.ylim([-1,1])
# plt.show()