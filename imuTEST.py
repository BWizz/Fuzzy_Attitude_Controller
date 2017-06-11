from UM6 import Imu
from DATA import Data
data=Data()
imu=Imu('COM5')
imu.stateUpdate(data)

print data.roll
