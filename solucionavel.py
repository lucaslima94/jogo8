def soluvel(vetor): #vetor de entrada
    saida = 0
    for x in range(9):
        if(vetor[x] != 0):
            for y in range((x+1), 9):
                if(vetor[y] != 0):
                    if(vetor[x] > vetor[y]):
                        saida = saida + 1
    print ("Numero total de inversoes: ", saida)
    return saida #retorna numero de inversoes, fazer saida%2 == 0 pra saber se eh solucionavel (impar = insoluconavel, par = solucionavel)

estadoinicial = [1,5,8,0,2,3,4,6,7]
teste2 = [5,1,8,0,2,3,4,6,7]
teste3 = [2,0,7,8,5,4,3,6,1]
teste4 = [8,7,6,5,4,3,2,1,0]
teste = 0
teste = soluvel(estadoinicial)
print(teste)
teste = soluvel(teste2)
print(teste)
teste = soluvel(teste3)
print(teste)
teste = soluvel(teste4)
print(teste)
