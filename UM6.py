# Yu Hin Hau
# 5/22/2014
# UM6 IMU Library
# https://www.chrobotics.com/docs/UM6_datasheet.pdf

import serial

class Imu:

    def __init__(self,port):
        self.imu = serial.Serial(port,115200)
        self.sendCommand('ac') # Zero Gyros
        self.sendCommand('ad') # Reset EKF


    def calibrate(self):
        self.sendCommand('ac') # Zero Gyros
        self.sendCommand('ad') # Reset EKF
        self.sendCommand('af') # Reset Accel Ref
        self.sendCommand('b0') # Reset Mag Reg


    def close(self):
        self.imu.close()


    def bitLen(self,int_type):
        length = 0
        while (int_type):
            int_type >>= 1
            length += 1
        return(length)


    def toggle(self,int_type):
        for i in xrange(self.bitLen(int_type)):
            mask = 1<<i
            int_type = int_type^mask
        return int_type


    def twoBytes2sComplement(self,b1,b2):
        d1 = ord(b1)
        d2 = ord(b2)
        val = (d1 << 8) + d2 # little endian

        if( val & (1<<15) != 0 ):
            val = val-1
            val = val-(1<<15)
            val = self.toggle(val)
            val = val *-1

        return val


    def checkSum(self,PT,ADD,d):

        # Received Checksum
        cs1 = self.imu.read()
        cs2 = self.imu.read()
        cs = self.twoBytes2sComplement(cs1,cs2)

        # Computed Checksum
        ccs = ord('s')+ord('n')+ord('p')+ord(PT)+ord(ADD)
        for i in xrange(8):
            ccs += ord(d[i])

        # Check if Received and Computed are Equal
        return cs == ccs



    def csum(self,buf):

        # Compute Checksum
        cs = 0
        for i in xrange(len(buf)):
            cs += ord(buf[i])

        cs1 = ((int('11111111',2) <<8) & cs) >>8
        cs2 = int('11111111',2) & cs

        # Attach Checksum to Buffer
        buf += chr(cs1)
        buf += chr(cs2)

        return buf


    def sendCommand(self,ADD):
        buf = 'snp'+chr(0)+chr(int(ADD,16))
        buf = self.csum(buf)
        self.imu.write(buf)

        while self.imu.read() != 's':
            pass
        if self.imu.read() == 'n':
            if self.imu.read() == 'p':
                PT = self.imu.read()
                ADD2 = self.imu.read()

                if ord(PT) == 0 and ADD2 == chr(int(ADD,16)):
                    print 'COMMAND SUCCESS @ ','{0:08x}'.format(ord(ADD2))
                else:
                    print 'COMMAND FAILED @ ','{0:08x}'.format(ord(ADD2))


    def readRegister(self,ADD):

        self.imu.flushInput()

        buf = 'snp'+chr(int('01001000',2))+chr(int(ADD,16))
        buf = self.csum(buf)
        self.imu.write(buf)


    def stateUpdate(self,data):

        #Read Euler Angles
        self.readRegister('00000062')
        self.parseData(data)

        # Read Gryo Data
        self.readRegister('0000005c')
        self.parseData(data)


    def parseData(self,data):

        while self.imu.read() != 's':
            pass
        if self.imu.read() == 'n':
            if self.imu.read() == 'p':

                # Package Type (7- Data? 6- Batch? 5,4,3,2- # Batch Address 1- Reserved 0- Command Error?)
                PT = self.imu.read()

                # Address
                ADD = self.imu.read()

                # Initialize Data
                d = []
                for i in xrange(8):
                    d.append(0)

                # Euler Phi Theta Psi
                if '{0:08x}'.format(ord(ADD)) == '00000062':
                    if '{0:08b}'.format(ord(PT)) == '11001000':

                        # Retrieve Data
                        for i in xrange(8):
                            d[i] = self.imu.read()

                        if self.checkSum(PT,ADD,d) == True:
                            phi = self.twoBytes2sComplement(d[0],d[1])*0.0109863
                            theta = self.twoBytes2sComplement(d[2],d[3])*0.0109863
                            psi = self.twoBytes2sComplement(d[4],d[5])*0.0109863
                            data.roll = phi
                            data.pitch = theta
                            data.yaw = psi
                        else:
                            print 'Checksum Failed @ Euler Angle'


                # Gryo X Y Z
                if '{0:08x}'.format(ord(ADD)) == '0000005c':
                    if '{0:08b}'.format(ord(PT)) == '11001000':

                        for i in xrange(8):
                            d[i] = self.imu.read()

                        if self.checkSum(PT,ADD,d) == True:
                            gx = self.twoBytes2sComplement(d[0],d[1])*0.0610352
                            gy = self.twoBytes2sComplement(d[2],d[3])*0.0610352
                            gz = self.twoBytes2sComplement(d[4],d[5])*0.0610352
                            data.roll_d = gx
                            data.pitch_d = gy
                            data.yaw_d = gz
                        else:
                            print 'Checksum Failed @ Gryo'









