# Brian Wisniewski
# 5/16/2014
# Inference Engine Module V-1
from numpy import zeros as ze
from math import ceil
class Inference:
	def __init__(self):
		pass
	
	def Mnd(self,error,error_d): #Manmadi Inference engine
		RULES = [[0,0,1],[0,1,2],[1,2,2]]
		out=ze((4,2))
		ind=0
		Zer=[0]*4
		Pos=[0]*4
		Neg=[0]*4


		for ii in range(0,len(error_d)):
			if error_d[ii] > 0:
				for jj in range(0,len(error)):
					if error[jj] > 0:
 						out[ind,0] = min(error_d[ii],error[jj])
						out[ind,1] = RULES[ii][jj]
						ind=ind+1
					
		

		for ii in range(0,4):
			if out[ii,1]==0:
				Neg[ii]=out[ii,0]
			if out[ii,1]==1:
				Zer[ii]=out[ii,0]
			if out[ii,1]==2:
				Pos[ii]=out[ii,0]
		OUT=[ceil(max(Neg)*10000)/10000,ceil(max(Zer)*10000)/10000,ceil(max(Pos)*10000)/10000]
		return OUT
	


			



