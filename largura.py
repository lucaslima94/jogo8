def teste(vet, vet2):
        valor = 0
        for i in range(0,(len(vet))):
                if(vet[i] == vet2):
                        valor = valor + 1
        return valor

class NO(object):
	valor=None
	global listanodos
	def init(self,matriz):
		self.valor=matriz
	def gera_filhos(self,visitados):
		for x in range(0,9):
			if self.valor[x]==0:
				pos=x
		if pos==0:
			matriz1=self.valor[:]
			matriz1[0],matriz1[1]=matriz1[1],matriz1[0]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			matriz1=self.valor[:]
			matriz1[0],matriz1[3]=matriz1[3],matriz1[0]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			listanodos.append(None)
			listanodos.append(None)
		
		if pos==2:
			matriz1=self.valor[:]
			matriz1[2],matriz1[1]=matriz1[1],matriz1[2]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			matriz1=self.valor[:]
			matriz1[2],matriz1[5]=matriz1[5],matriz1[2]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			listanodos.append(None)
			listanodos.append(None)
			
		if pos==6:
			matriz1=self.valor[:]
			matriz1[6],matriz1[3]=matriz1[3],matriz1[6]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			matriz1=self.valor[:]
			matriz1[6],matriz1[7]=matriz1[7],matriz1[3]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			listanodos.append(None)
			listanodos.append(None)
			
		if pos==8:
			matriz1=self.valor[:]
			matriz1[8],matriz1[7]=matriz1[7],matriz1[8]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			matriz1=self.valor[:]
			matriz1[8],matriz1[5]=matriz1[5],matriz1[8]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			listanodos.append(None)
			listanodos.append(None)
			
		if pos==1:
			matriz1=self.valor[:]
			matriz1[1],matriz1[0]=matriz1[0],matriz1[1]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			matriz1=self.valor[:]
			matriz1[1],matriz1[4]=matriz1[4],matriz1[1]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			matriz1=self.valor[:]
			matriz1[1],matriz1[2]=matriz1[2],matriz1[1]
			if(teste(visitados, matriz1) == 0):
				temporario=NO()
				temporario.init(matriz1)
				listanodos.append(temporario)
			listanodos.append(None)
			
			if pos==3:
				matriz1=self.valor[:]
				matriz1[3],matriz1[0]=matriz1[0],matriz1[3]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[3],matriz1[4]=matriz1[4],matriz1[3]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[3],matriz1[6]=matriz1[6],matriz1[3]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				listanodos.append(None)
			
			if pos==5:
				matriz1=self.valor[:]
				matriz1[5],matriz1[2]=matriz1[2],matriz1[5]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[5],matriz1[4]=matriz1[4],matriz1[5]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[5],matriz1[8]=matriz1[8],matriz1[5]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				listanodos.append(None)
			
			if pos==7:
				matriz1=self.valor[:]
				matriz1[7],matriz1[6]=matriz1[6],matriz1[7]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[7],matriz1[4]=matriz1[4],matriz1[7]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[7],matriz1[8]=matriz1[8],matriz1[7]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				listanodos.append(None)
			
			if pos==4:
				matriz1=self.valor[:]
				matriz1[4],matriz1[1]=matriz1[1],matriz1[4]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[4],matriz1[3]=matriz1[3],matriz1[4]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[4],matriz1[5]=matriz1[5],matriz1[4]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
				matriz1=self.valor[:]
				matriz1[4],matriz1[7]=matriz1[7],matriz1[4]
				if(teste(visitados, matriz1) == 0):
					temporario=NO()
					temporario.init(matriz1)
					listanodos.append(temporario)
		
estadoinicial=[0,1,2,3,4,5,6,7,8]
raiz=NO()
raiz.init(estadoinicial)
atual=raiz
listanodos=[]
for j in range(0,10):
	listanodos.append(atual)
	atual.gera_filhos(listanodos)
for i in range(0,len(listanodos)):
	if (listanodos[i]!= None):
		print listanodos[i].valor
	else:
		print "Nulo"
print len(listanodos)
