# FILA: enqueue = inserir; dequeue = remover
# "método construtor", possui a responsabilidade de criar o objeto daquela classe.
class Pilha: 
    def __init__(self):
        self.lista = [] #atributos 

    def push(self, elemento):
        self.lista.append(elemento)
    
    def pop(self):
        self.lista.pop()
        
    def peek(self):
        return self.lista[-1]
    
    def isEmpty(self):
        if not self.lista:
            return True
        else: 
            return False
        
    def listar(self):
        for item in self.lista:
            print(item)
            
pilha_livros = Pilha()
pilha_comida = Pilha()

while (True):
    livros = input('Nome do livro: ')
    pilha_livros.push(livros)
    comidas = input('comida: ')
    pilha_comida.push(comidas)
    
    if pilha_livros.isEmpty():
        print('A lista está vazia. ')
    
    pilha_livros.listar()
    pilha_comida.listar()
    