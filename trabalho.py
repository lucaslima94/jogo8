import copy

def soluvel(vetor): #vetor de entrada
    saida = 0
    for x in range(9):
        if(vetor[x] != 0):
            for y in range((x+1), 9):
                if(vetor[y] != 0):
                    if(vetor[x] > vetor[y]):
                        saida = saida + 1
    return saida #retorna numero de inversoes, fazer saida%2 == 0 pra saber se eh soluvel


def teste(vet, vet2):
        valor = 0
        for i in range(0,(len(vet))):
                if(vet[i] == vet2):
                        valor = valor + 1
        return valor
        
def buscameta(inicial,meta):
	valor=0
	if (inicial==meta):
		valor=1
	return valor


class NO(object):
	valor,filho1,filho2,filho3,filho4=None,None,None,None,None
	flag1,flag2,flag3,flag4=0,0,0,0
	pai=None
	statusfilhos=0
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
			matriz1=self.valor[:]
			matriz1[4],matriz1[7]=matriz1[7],matriz1[4]
			if(teste(visita, matriz1) == 0):
				self.filho4=NO()
				self.filho4.pai=self
				self.filho4.init(matriz1)
		
		
		
		
		
estadometa=[0,1,2,3,4,5,6,7,8]
estadoinicial=[2,0,7,8,5,4,3,6,1]
visitados=[]
i=0
root=NO()
root.pai=None
root.init(estadoinicial)	
atual=root
contador=0
folhas =[]
#print atual.pai
vava=soluvel(estadoinicial)
if(vava%2==0): #Se for soluvel
	while(buscameta(atual.valor,estadometa)!=1): #Enquanto nao encontra, continua
		if (contador<5): #Verifica profundidade
			if(contador == 2):
				print "PROFUNDIDADE"
			if((atual.flag1==1 or atual.filho1==None)and(atual.flag2==1 or atual.filho2==None)and (atual.flag3==1 or atual.filho3==None)and(atual.flag4==1 or atual.filho4==None)):
				visitados.append(atual.valor) #Adiciona no a lista de visitados
			if (atual.statusfilhos==0): #Verifica se foi gerados os filhos desse no
					atual.gera_filhos(visitados) #Gera os filhos caso nao foi gerado
					print atual.valor
					if atual.filho1 !=None:
						print "filho1:",atual.filho1.valor
					if atual.filho2 !=None:
						print "filho2:",atual.filho2.valor
					if atual.filho3 !=None:
						print "filho3:",atual.filho3.valor
					if atual.filho4 !=None:
						print "filho4:",atual.filho4.valor
					print "\n\n\n"
					atual.statusfilhos=1 #Recebe 1 pra nao gerar novamente os filhos desse no
			if(atual.filho1 != None and atual.flag1==0):
						atual.flag1=1
						atual=atual.filho1
						contador = contador+1
						print "entrou1"
						if(buscameta(atual.valor,estadometa)==1):
							break
					
			else:
					if(atual.filho2 != None and atual.flag2==0):
								atual.flag2=1
								atual=atual.filho2
								contador = contador+1
								print "entrou2"
								if(buscameta(atual.valor,estadometa)==1):
									break
					else:
							if(atual.filho3 != None and atual.flag3==0):
										atual.flag3=1
										atual=atual.filho3
										contador = contador+1
										print "entrou3"
										if(buscameta(atual.valor,estadometa)==1):
											break
							else:
									if(atual.filho4 != None and atual.flag4==0):
												atual.flag4=1
												atual=atual.filho4
												contador = contador+1
												print "entrou4"
												if(buscameta(atual.valor,estadometa)==1):
													break
									else:	
											if(buscameta(atual.valor,estadometa)==1): #Estado final, breaka
													break 
											if(atual.pai==None): #No raiz, breaka
												print "Raiz"
												atual = copy.copy(folhas[0])
												
												
												folhas.remove(folhas[0])
											
											elif((atual.flag1==1 or atual.filho1==None)and(atual.flag2==1 or atual.filho2==None)and (atual.flag3==1 or atual.filho3==None)and(atual.flag4==1 or atual.filho4==None)):
												atual=atual.pai
												contador=contador-1
												print "Voltou pro pai"
											else:
												print " entrou onde nao devia"
												break
			
		else: #Entra aqui caso profundidade chegue no maximo
			print "Prof maxima, volta pro pai"
			nodotemp=NO()
			nodotemp=copy.copy(atual)
			folhas.append(nodotemp)
			contador=contador-1 #Volta 1 posicao na arvore
			atual=atual.pai #Volta pro pai
		print atual.valor[0]," ",atual.valor[1]," ",atual.valor[2]
		print atual.valor[3]," ",atual.valor[4]," ",atual.valor[5]
		print atual.valor[6]," ",atual.valor[7]," ",atual.valor[8],"\n"
		i=i+1
else: #Caso nao seja soluvel
	print "vavacilao"		
print i
print "teste:", contador
print vava
caminhoarvore=[]
while (atual.pai!=None):
	caminhoarvore.append(atual.valor)
	atual=atual.pai
caminhoarvore.append(atual.valor)
print caminhoarvore [::-1]
print len(caminhoarvore)

        
        
