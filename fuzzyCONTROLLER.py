from FUZZIFY_V2 import Fuzzify
from INFERENCE import Inference as inf
from DEFUZZIFY import Defuzzify
from math import exp

class Fuzzycontroller():
	def __init__(self,desired):
		self.desiredRoll   = .016*desired[0][0]
		self.desiredPitch  = .016*desired[0][1]
		self.desiredYaw    = .00555*desired[0][2]
		self.desiredRolld  = .005*desired[1][0]
		self.desiredPitchd = .005*desired[1][1]
		self.desiredYawd   = .005*desired[1][2]
		self.defuzz=Defuzzify()
		self.fuzzy=Fuzzify()
		self.inf=inf()



	def control(self,data,throttle):	
		per_control_pitch=.01
		per_control_roll=.01
		per_control_yaw=0
		offback=8
		offleft=8
		Blimit=1100



		roll  =.016*data.roll
		pitch =.016*data.pitch
		yaw   =.0055555556*data.yaw

		rolld  =.005*data.roll_d
		pitchd =.005*data.pitch_d
		yawd   =.005*data.yaw_d
		if data.roll_d > 600 or data.roll_d < -600:
			if data.roll_d > 600:
				rolld=3
			else:
				rolld=-3
		if data.pitch_d > 600 or data.pitch_d < -600:
			if data.pitch_d > 600:
				pitchd=3
			else:
				pitchd=-3
		if data.yaw_d > 600 or data.yaw_d < -600:
			if data.yaw_d > 600:
				yawd=3
			else:
				yawd=-3



		roll_e  = self.desiredRoll-roll
		pitch_e = self.desiredPitch-pitch
		yaw_e   = self.desiredYaw-yaw

		roll_ed  = self.desiredRolld-rolld
		pitch_ed = self.desiredPitchd-pitchd
		yaw_ed   = self.desiredYawd-yawd


		eFuzzyRoll ,edFuzzyRoll  =self.fuzzy.Fuzzy(roll_e,roll_ed,.15,1.5)
		eFuzzyPitch,edFuzzyPitch =self.fuzzy.Fuzzy(pitch_e,pitch_ed,.15,1.5)
		eFuzzyYaw  ,edFuzzyYaw   =self.fuzzy.Fuzzy(yaw_e,yaw_ed,.15,1.5)
		OUT=[0]*3
		OUT[0]=self.defuzz.Defuzz(self.inf.Mnd(eFuzzyRoll,edFuzzyRoll))
		OUT[1]=self.defuzz.Defuzz(self.inf.Mnd(eFuzzyPitch,edFuzzyPitch))
		OUT[2]=self.defuzz.Defuzz(self.inf.Mnd(eFuzzyYaw,edFuzzyYaw))
	
		error=[roll_e,pitch_e,yaw_e]
		errorRate=[roll_ed,pitch_ed,yaw_ed]
		# This Defines the PWM OUTPUT that will be sent to the motors
		a=3235/128
		b=-7/64
		c=1
		amp=(a*pitch_e**2+b*pitch_e+c)/2
		yaw=0 #int(round(600*OUT[2]*per_control_yaw))

		front=+int(amp*(round(per_control_pitch*600*OUT[1])))+yaw+throttle+Blimit-offback
		back=-int(amp*(round(per_control_pitch*600*OUT[1])))-yaw+throttle+Blimit+offback
		left=+int(amp*(round(per_control_roll*600*OUT[0])))-yaw+throttle+Blimit+offleft
		right=-int(amp*(round(per_control_roll*600*OUT[0])))+yaw+throttle+Blimit-offleft

		PWMmot=[left,right,front,back]

		return error, errorRate, OUT,PWMmot





		


