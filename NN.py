import random
import math
def activ(x):
		return 1 / (1 + math.exp(-x))
def dactiv(x):
		return activ(x)*(1-activ(x))

	

class Jk:
	def __init__(self,ni,nh,no):    

		self.ni=ni+1
		self.nh=nh+1
		self.no=no
		self.winph=[[0]*self.nh]*self.ni
		for i in range(self.ni):
			for j in range(self.nh):
				self.winph[i][j]=random.uniform(-1,1)
		self.whout=[[0]*self.no]*self.nh
		for i in range(self.nh):    
			for j in range(self.no):
				self.whout[i][j]=random.uniform(-1,1)
		self.y=[0]*(self.nh)
		self.z=[0]*(self.no)
		#self.nethin[j]=[1.0]*self.nh
	def updat(self,x):
		x=map(lambda y:float(y),x)
		x.append(1.0)
		print len(x)
		for j in range(self.nh-1):
			nethin=0.0
			for i in range(self.ni):
				nethin+=x[i]*self.winph[i][j]
			self.y[j]=activ(nethin)
		self.y[self.nh-1]=random.uniform(-1,1)
		for k in range(self.no):
			nethout=0.0
			for j in range(self.nh):
				nethout+=self.y[j]*self.whout[j][k]
			self.z[k]=activ(nethout)
		return self.z    
	def backpro(self,eta,t,x):
		deltai=[0.0]*self.nh
		deltao=[0.0]*self.no
		x.append(1.0)
		for k in range(self.no):
			for j in range(self.nh):
				self.whout[j][k]+=(eta*(float(t[k])-self.z[k])*dactiv(self.z[k])*self.y[j])
				deltao[k]=(float(t[k])-self.z[k])*dactiv(self.z[k])
		for j in range(self.nh):
			for k in range(self.no):
				deltai[j]+=self.whout[j][k]*deltao[k]
			deltai[j]*=dactiv(self.y[j])
		for j in range(self.nh):
			for i in range(self.ni):
				self.winph[i][j]=self.winph[i][j]+eta*deltai[j]*float(x[i])
		return  
	def weights(self):
		"""
		t=[]
		for i in range(self.ni):
			for j in range(self.nh):
				t.append(self.winph[i][j])
		print "INput weights"
		print t
		t=[]
		for j in range(self.nh):
			for k in range(self.no):
				t.append(self.whout[j][k])
		print "outpu"
		print t
		"""
		print 'input weights'
		for i in range(self.ni):
			print self.winph[i]
		print '/n Outputweights'
		for j in range(self.nh):
			print self.whout[j] 	
	def training(self,itear,pattern):
		for i in range(itear):
			for tj in pattern:
				m=self.updat(tj[0])
				mer=self.backpro(0.5,tj[1],tj[0])
		self.weights()

if __name__=='__main__':
	txt=open('optdigits.tra','r')
	ape=[]
	for line in txt:
		if line!='\n' and line[-2] in {'2','5','7'}:
			ap=[]
			ap.append(line.split(',')[:-1])
			#ap.append(line.split(',')[-1][0])
			if line.split(',')[-1][0]=='2':
				ap.append(['1','0'])
			elif line.split(',')[-1][0]=='5':
				ap.append(['1','1'])
			elif line.split(',')[-1][0]=='7':
				ap.append(['0','1'])
			ape.append(ap)
	#print ape
	ghm=Jk(64,8,2)
	lm=[]
	for k in ape:
		lm.append(k[0])
	print lm
	ghm.training(10,ape)
	#print ghm.updat(lm)
