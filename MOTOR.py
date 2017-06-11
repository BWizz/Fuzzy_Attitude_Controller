# Yu Hin Hau
# 4/15/2014
# PWM OUTPUT Module
# Pololu Micro Maestro

import serial
import time

class Motor():
    
    # Initialize Motor
    def __init__(self,port):
        self.motor = serial.Serial(port,9600)
        self.safety = True
                
    # Convert PWM to Binary Data for Pololu
    def timeToBinary(self,pwm):
        pwm *= 4
        mask = 0b1111111
        high = pwm >> 7
        low = pwm & mask
        return [low,high]
	
    # Write PWM to Individual Channel
    def writeChannel(self,channel,pwm):
        if self.safety == False:
            data = self.timeToBinary(pwm);
            self.motor.write(chr(132))
            self.motor.write(chr(channel))
            self.motor.write(chr(data[0]))
            self.motor.write(chr(data[1]))
        else:
            print 'Safety On! Arm motor before use!'
    
    # Write PWM to All Channels
    def writeAll(self,pwm):
        for i in range(0,6):
            self.writeChannel(i,pwm)    
    
    # Write PWM State to All Channels
    def writePWM(self,data):
        for i in range(0,len(data)):
            self.writeChannel(i,data[i])
    
    # Arm Device
    def arm(self):
        self.safety = False
        self.writeAll(1000)
        time.sleep(1)
        print 'Motor Armed!'
    
    # Disarm Device
    def disarm(self):
        self.writeAll(1000)
        self.safety = True        
        print 'Motor Disarmed!'
    
    # Close COM Port
    def close(self):
        if self.safety == False:
            self.disarm()
        self.motor.close()