import serial
import time

class Imu():
        
    def __init__(self,port):
        self.imu = serial.Serial(port,57600,timeout = 1)
        print self.imu
        time.sleep(2)
        
    def stateUpdate(self,data):

        imuData = [0,0,0]
        imuData2 = [0,0,0]
        
        # IMU Angle Data
        self.imu.flushInput()
        self.imu.write('#ot')
        self.imu.write('#f')
        
        while self.imu.inWaiting() <= 0:
            pass

        rawData=self.imu.readline()
        imuData=rawData.split('=')[1].split(',')
        
        for i in range(3):
            imuData[i]=float(imuData[i])
            
        data.yaw = imuData[0]
        data.pitch = imuData[1]
        data.roll = imuData[2]
        
        # IMU Gryo Data
        self.imu.flushInput()
        self.imu.write('#osct')
        self.imu.write('#f')
        
        while self.imu.inWaiting() <= 0:
            pass

        rawData=self.imu.readline()
        imuData=rawData.split('=')[1].split(',')
        
        for i in range(3):
            imuData2[i]=float(imuData[i])
             
        data.yaw_d = (imuData2[2]+3)
        data.pitch_d = (imuData2[1]-4)
        data.roll_d = (imuData2[0]+5)
        
        return data
        
    def close(self):
        self.imu.close()