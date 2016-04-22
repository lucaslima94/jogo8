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

def gerafilhos(vetor,listanodos):
	vetorfilhos = []
	temp = vetor[:]
	temp1 = vetor[:]
	temp2 = vetor[:]
	temp3 = vetor[:]
	for x in range(0,9):
		if vetor[x]==0:
			pos=x
	if pos == 0:
		temp[0],temp[1]=temp[1],temp[0]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[0],temp1[3]=temp1[3],temp1[0]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 2:
		temp[2],temp[1]=temp[1],temp[2]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[2],temp1[5]=temp1[5],temp1[2]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 6:
		temp[6],temp[3]=temp[3],temp[6]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[6],temp1[7]=temp1[7],temp1[6]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 8:
		temp[8],temp[7]=temp[7],temp[8]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[8],temp1[5]=temp1[5],temp1[8]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 1:
		temp[1],temp[0]=temp[0],temp[1]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[1],temp1[4]=temp1[4],temp1[1]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		temp2[1],temp2[2]=temp2[2],temp2[1]
		if(teste(listanodos,temp2)==0):
			vetorfilhos.append(temp2)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 3:
		temp[3],temp[0]=temp[0],temp[3]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[3],temp1[4]=temp1[4],temp1[3]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		temp2[3],temp2[6]=temp2[6],temp2[3]
		if(teste(listanodos,temp2)==0):
			vetorfilhos.append(temp2)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 5:
		temp[5],temp[2]=temp[2],temp[5]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[5],temp1[4]=temp1[4],temp1[5]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		temp2[5],temp2[8]=temp2[8],temp2[5]
		if(teste(listanodos,temp2)==0):
			vetorfilhos.append(temp2)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 7:
		temp[7],temp[6]=temp[6],temp[7]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[7],temp1[4]=temp1[4],temp1[7]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		temp2[7],temp2[8]=temp2[8],temp2[7]
		if(teste(listanodos,temp2)==0):
			vetorfilhos.append(temp2)
		else:
			vetorfilhos.append(None)
		vetorfilhos.append(None)
	if pos == 4:
		temp[4],temp[1]=temp[1],temp[4]
		if(teste(listanodos,temp)==0):
			vetorfilhos.append(temp)
		else:
			vetorfilhos.append(None)
		temp1[4],temp1[3]=temp1[3],temp1[4]
		if(teste(listanodos,temp1)==0):
			vetorfilhos.append(temp1)
		else:
			vetorfilhos.append(None)
		temp2[4],temp2[5]=temp2[5],temp2[4]
		if(teste(listanodos,temp2)==0):
			vetorfilhos.append(temp2)
		else:
			vetorfilhos.append(None)
		temp3[4],temp3[7]=temp3[7],temp3[4]
		if(teste(listanodos,temp3)==0):
			vetorfilhos.append(temp3)
		else:
			vetorfilhos.append(None)
	return vetorfilhos
			
		
		
estadofinal=[0,1,2,3,4,5,6,7,8]
estadoinicial=[3,1,2,6,4,5,0,7,8]
estadoinicial2=[1,5,8,0,2,3,4,6,7]
estadoinicial3=[1,4,2,3,7,5,6,0,8]

listanodos=[]
listatemp = []
contador=0
listanodos.append(estadoinicial3)
while(listanodos[contador] != estadofinal):
	print listanodos[contador]
	atual = listanodos[contador]
	if(listanodos[contador] == None):
		listanodos.append(None)
		listanodos.append(None)
		listanodos.append(None)
		listanodos.append(None)
	else:
		listatemp = gerafilhos(atual,listanodos)
		listanodos.append(listatemp[0])
		listanodos.append(listatemp[1])
		listanodos.append(listatemp[2])
		listanodos.append(listatemp[3])
	contador = contador + 1
print listanodos[contador]
	
