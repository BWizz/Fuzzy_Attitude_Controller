# Brian Wisniewski
# 5/14/2014
# Fuzzification Module V-2
class Fuzzify:
	def __init__(self):
		pass
	def Fuzzy(self,e,ed,end_e,end_ed):
		def eTrapN(self,x):
			if x <= -.15:
				return 1
			elif x > -.15 and x < 0:
				return x/float(-.15)
			else: 
				return 0

		def eTrapP(self,x):
			if x >= .15:
				return 1
			elif x > 0 and x < .15:
				return x/float(.15)
			else:
				return 0

		def eTri(self,x,end_e):
			#Assumes a symetric Trianguler memebership function
			end_e=.15/1
			if x >= -end_e and x < 0:
				return 1+x/float(end_e)
			elif x >= 0 and x <= end_e:
				return 1-x/float(end_e)
			else:
				return 0
		eFuzzy=[eTrapN(self,e),eTri(self,e,end_e),eTrapP(self,e)]
		

		def edTrapN(self,x):
			if x <= -1.5:
				return 1
			elif x > -1.5 and x < 0:
				return x/float(-1.5)
			else: 
				return 0

		def edTrapP(self,x):
			if x >= 1.5:
				return 1
			elif x > 0 and x < 1.5:
				return x/float(1.5)
			else:
				return 0

		def edTri(self,x,end_ed):
			#Assumes a symetric Trianguler memebership function
			end_ed=1.5/1
			if x >= -end_ed and x < 0:
				return 1+x/float(end_ed)
			elif x >= 0 and x <= end_ed:
				return 1-x/float(end_ed)
			else:
				return 0
		edFuzzy=[edTrapN(self,ed),edTri(self,ed,end_ed),edTrapP(self,ed)]

		return eFuzzy, edFuzzy





