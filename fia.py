class NO(object):
	valor,filho1,filho2,filho3,filho4=None,None,None,None,None
	def init(self,matriz):
		self.valor=matriz
	def gera_filhos(self):
		for x in range(0, 9):
			if self.valor[x]==0:
				pos=x
				if pos==0:
					matriz1=self.valor[:]
					matriz1[0],matriz1[1]=matriz1[1],matriz1[0]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[0],matriz1[3]=matriz1[3],matriz1[0]
					self.filho2=NO()
					self.filho2.init(matriz1)
				if pos==2:
					matriz1=self.valor[:]
					matriz1[2],matriz1[1]=matriz1[1],matriz1[2]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[2],matriz1[5]=matriz1[5],matriz1[2]
					self.filho2=NO()
					self.filho2.init(matriz1)
				if pos==6:
					matriz1=self.valor[:]
					matriz1[6],matriz1[3]=matriz1[3],matriz1[6]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[6],matriz1[7]=matriz1[7],matriz1[6]
					self.filho2=NO()
					self.filho2.init(matriz1)
				if pos==8:
					matriz1=self.valor[:]
					matriz1[8],matriz1[5]=matriz1[5],matriz1[8]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[8],matriz1[7]=matriz1[7],matriz1[8]
					self.filho2=NO()
					self.filho2.init(matriz1)
				if pos==1:
					matriz1=self.valor[:]
					matriz1[1],matriz1[0]=matriz1[0],matriz1[1]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[1],matriz1[4]=matriz1[4],matriz1[1]
					self.filho2=NO()
					self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[1],matriz1[2]=matriz1[2],matriz1[1]
					self.filho3=NO()
					self.filho3.init(matriz1)
				if pos==3:
					matriz1=self.valor[:]
					matriz1[3],matriz1[0]=matriz1[0],matriz1[3]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[3],matriz1[4]=matriz1[4],matriz1[3]
					self.filho2=NO()
					self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[3],matriz1[6]=matriz1[6],matriz1[3]
					self.filho3=NO()
					self.filho3.init(matriz1)
				if pos==5:
					matriz1=self.valor[:]
					matriz1[5],matriz1[2]=matriz1[2],matriz1[5]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[5],matriz1[4]=matriz1[4],matriz1[5]
					self.filho2=NO()
					self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[5],matriz1[8]=matriz1[8],matriz1[5]
					self.filho3=NO()
					self.filho3.init(matriz1)
				if pos==7:
					matriz1=self.valor[:]
					matriz1[7],matriz1[6]=matriz1[6],matriz1[7]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[7],matriz1[4]=matriz1[4],matriz1[7]
					self.filho2=NO()
					self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[7],matriz1[8]=matriz1[8],matriz1[7]
					self.filho3=NO()
					self.filho3.init(matriz1)
				if pos==4:
					matriz1=self.valor[:]
					matriz1[4],matriz1[1]=matriz1[1],matriz1[4]
					self.filho1=NO()
					self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[4],matriz1[3]=matriz1[3],matriz1[4]
					self.filho2=NO()
					self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[4],matriz1[5]=matriz1[5],matriz1[4]
					self.filho3=NO()
					self.filho3.init(matriz1)
					matriz1[4],matriz1[7]=matriz1[7],matriz1[4]
					self.filho4=NO()
					self.filho4.init(matriz1)
		
		
		
		
		
estadoinicial=[0,1,2,3,4,5,6,7,8]

root=NO()
root.init(estadoinicial)
atual=root
for i in range(0,5):
	atual.gera_filhos()
	print atual.valor
	atual=atual.filho1









		
		
		
		

