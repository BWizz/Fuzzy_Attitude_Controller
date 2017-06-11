# Brian Wisniewski
# DATE
# Defuzzification Module V-1
class Defuzzify:
	def __init__(self):
		pass

	def Defuzz(self,out):
		N=out[0]
		Z=out[1]
		P=out[2]
		if N>0:
			a=-(-1-N*(-.85))
			b=1
			An=.5*N*(a+b)
			xn=-1+(a**2+b**2+a*b)/(3*(a+b))
		else:
			An=xn=0
		if Z>0:
			a=2*((Z-1)*-.1)
			b=.2
			Az=.5*Z*(a+b)
			xz=0
		else:
			xz=Az=0
		if P>0:
			a=(1-P*(.85))
			b=1
			Ap=.5*P*(a+b)
			xp=1-(a**2+b**2+a*b)/(3*(a+b))
		else:
			xp=Ap=0

		
		X=(xn*An+xp*Ap)/(An+Az+Ap)
		
		return X



			
			



