def teste(vet, vet2):
        valor = 0
        for i in range(0,(len(vet))):
                if(vet[i] == vet2):
                        valor = valor + 1
        return valor


class NO(object):
	valor,filho1,filho2,filho3,filho4=None,None,None,None,None
	flag1,flag2,flag3,flag4=0,0,0,0
	pai=None
	def init(self,matriz):
		self.valor=matriz
	def gera_filhos(self, visita):
		for x in range(0, 9):
			if self.valor[x]==0:
				pos=x
				if pos==0:
					matriz1=self.valor[:]
					matriz1[0],matriz1[1]=matriz1[1],matriz1[0]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
                                                
                                        matriz1=self.valor[:]
                                        matriz1[0],matriz1[3]=matriz1[3],matriz1[0]
                                        if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
				if pos==2:
					matriz1=self.valor[:]
					matriz1[2],matriz1[1]=matriz1[1],matriz1[2]
                                        if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[2],matriz1[5]=matriz1[5],matriz1[2]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
				if pos==6:
					matriz1=self.valor[:]
					matriz1[6],matriz1[3]=matriz1[3],matriz1[6]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[6],matriz1[7]=matriz1[7],matriz1[6]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
				if pos==8:
					matriz1=self.valor[:]
					matriz1[8],matriz1[5]=matriz1[5],matriz1[8]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[8],matriz1[7]=matriz1[7],matriz1[8]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
				if pos==1:
					matriz1=self.valor[:]
					matriz1[1],matriz1[0]=matriz1[0],matriz1[1]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[1],matriz1[4]=matriz1[4],matriz1[1]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[1],matriz1[2]=matriz1[2],matriz1[1]
					if(teste(visita, matriz1) == 0):
                                                self.filho3=NO()
                                                self.filho3.pai=self
                                                self.filho3.init(matriz1)
				if pos==3:
					matriz1=self.valor[:]
					matriz1[3],matriz1[0]=matriz1[0],matriz1[3]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[3],matriz1[4]=matriz1[4],matriz1[3]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[3],matriz1[6]=matriz1[6],matriz1[3]
                                        if(teste(visita, matriz1) == 0):
                                                self.filho3=NO()
                                                self.filho3.pai=self
                                                self.filho3.init(matriz1)
				if pos==5:
					matriz1=self.valor[:]
					matriz1[5],matriz1[2]=matriz1[2],matriz1[5]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[5],matriz1[4]=matriz1[4],matriz1[5]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[5],matriz1[8]=matriz1[8],matriz1[5]
					if(teste(visita, matriz1) == 0):
                                                self.filho3=NO()
                                                self.filho3.pai=self
                                                self.filho3.init(matriz1)
				if pos==7:
					matriz1=self.valor[:]
					matriz1[7],matriz1[6]=matriz1[6],matriz1[7]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[7],matriz1[4]=matriz1[4],matriz1[7]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[7],matriz1[8]=matriz1[8],matriz1[7]
					if(teste(visita, matriz1) == 0):
                                                self.filho3=NO()
                                                self.filho3.pai=self
                                                self.filho3.init(matriz1)
				if pos==4:
					matriz1=self.valor[:]
					matriz1[4],matriz1[1]=matriz1[1],matriz1[4]
					if(teste(visita, matriz1) == 0):
                                                self.filho1=NO()
                                                self.filho1.pai=self
                                                self.filho1.init(matriz1)
					matriz1=self.valor[:]
					matriz1[4],matriz1[3]=matriz1[3],matriz1[4]
					if(teste(visita, matriz1) == 0):
                                                self.filho2=NO()
                                                self.filho2.pai=self
                                                self.filho2.init(matriz1)
					matriz1=self.valor[:]
					matriz1[4],matriz1[5]=matriz1[5],matriz1[4]
					if(teste(visita, matriz1) == 0):
                                                self.filho3=NO()
                                                self.filho3.pai=self
                                                self.filho3.init(matriz1)
					matriz1[4],matriz1[7]=matriz1[7],matriz1[4]
					if(teste(visita, matriz1) == 0):
                                                self.filho4=NO()
                                                self.filho4.pai=self
                                                self.filho4.init(matriz1)
		
		
		
		
		
estadoinicial=[0,2,3,6,5,8,4,7,1]
visitados=[]
root=NO()
root.pai=None
root.init(estadoinicial)
atual=root
#print atual.pai
for i in range(0,10):
        visitados.append(atual.valor)
        atual.gera_filhos(visitados)
        print (atual.valor)
        if (atual.pai!=None):
			print atual.pai.valor
	print "\n \n"
        if(atual.filho1 != None and atual.flag1==0):
				atual.flag1=1
				atual=atual.filho1
                
        else:
                if(atual.filho2 != None and atual.flag2==0):
						atual.flag2=1
						atual=atual.filho2
                else:
                        if(atual.filho3 != None and atual.flag3==0):
								atual.flag3=1
								atual=atual.filho3
                        else:
                                if(atual.filho4 != None and atual.flag4==0):
										atual.flag4=1
										atual=atual.filho4
                                else:
									atual=atual.pai

print i										

        
        
