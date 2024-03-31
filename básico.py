#inicio do curso em Python
print ('hello world')
print ('8+5')
print ('8'+'5')
print (8+5)
print ('olá' , 5)
# , traz a mesma função de + porem com diferenças

nome = ('anna')
idade = 40
peso = 67.9
print (nome, idade, peso)

# input = leia
nom = input ('qual seu nome? ')
id = input ('qual sua idade? ')
pes = input ('qual seu peso? ')
print (nom, id, pes)

#desafio 
pessoa = input ('qual seu nome? ')
print ('Boas vindas,', pessoa)

dia = input ('dia:')
mes = input ('mês:')
ano = input ('ano:')
print ('você nasceu no dia', dia,'do', mes, 'de', ano, '. Correto?')

#format()
dia = input ('dia:')
mes = input ('mês:')
ano = input ('ano:')
print ('você nasceu no dia {} do {} de {}. Correto?' .format(dia, mes, ano))

#continuação do curso de python

n1 = int (input ('digite o primeiro numero:'))
n2 = int (input ('digite o segundo numero:'))
soma = n1 + n2 
print ('O resultado da soma é: {}' .format(soma))
print ('a soma vale: {}' .format(n1+n2))
#juntar a str na outra é concatenação
#int, float, bool, str

a = input ('digite algo: ')
print ('o tipo primitivo é: ', type(a))
print ('Só tem espaços? ', a.isspace())
print ('é numérico? ', a.isnumeric())

#há diversas funções de is"alguma coisa", basta testar usando mesma sintaxe
# + adição - subtração * multiplicação e / divisão ** potencia // divisão inteira % resto da divisão == igual
# ordem de precedência: - (); **; *,/,//,%; +,-
# pode usar por exemplo, {:.3f} dentro do .format pra aparecer so 3 casas decimais
# ,end=' ' pra não quebrar a linha entre prints e \n p quebrar

print ('=' * 20)
print (pow(4,3))
print ('oi' * 5)

nome = input ('Qual seu nome?')
print ('prazer em te conhecer, {:=^20}!'.format(nome))
#pode usar <,>,^

n = int (input ('Digite um número: '))
print ('O sucessor é {}' .format(n + 1))
print ('O antecessor é {}' .format(n - 1))
#quando se trata de operações sempre definir type

''' Dobro, Triplo, Raiz Quadrada'''

num = int(input('Digite um numero: '))
d = num * 2
t = num * 3
r = num ** (1/2) # pow(n(1/2))

print('O dobro é: {}\nO triplo é: {}\na raiz é: {:.2f}\n'.format(d, t, r))