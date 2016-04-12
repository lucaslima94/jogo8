class NO(object):
	valor,filho1,filho2,filho3,filho4=None,None,None,None,None	
	def init(self,matriz):
		self.valor=matriz
	def gera_filhos(self):
		self.filho1=NO()
		for x in range(0, 9):
			if self.valor[x]==0:
				pos=x
				matriz=self.valor[:]
				aux=matriz[pos]
				matriz[pos]=matriz[pos-2]
				matriz[pos-2]=aux
				self.filho1.init(matriz)
				
		
		
		
		
		
estadoinicial=[1,2,3,4,5,6,7,8,0]

root=NO()
root.init(estadoinicial)
root.gera_filhos()
print root.valor
print root.filho1.valor









		
		
		
		

