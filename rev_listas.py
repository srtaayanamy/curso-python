#listas

listas = []

listas.append(1) #adiciona sempre ao final da lista
listas.append('anna')
listas.append(True)
print(listas)

copia = listas.copy()
print(listas.count('anna'))

listas.pop() #remove o ultimo da lista
listas.remove('anna') #remove algo específico, somente o primeiro
listas.insert(2, 5) #insere um elemento em um indice especifico insere na terceira posição o nmr 5
listas.sort()
listas2= ['ama', 'ver']
listas.extend(listas2) #junta listas
