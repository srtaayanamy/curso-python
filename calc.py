class Calculadora:
    def __init__(self):
        pass
    
    def somar(self, a, b, resul):
        resul == a + b
        return resul
    
    def subtrair(self, a, b, resul):
        resul == a - b
        return resul
    
    def multiplicar(self, a, b, resul):
        resul == a * b
        return resul
    
    def dividir(self, a, b, resul):
        if b == 0:
            print('\nDIVISÃO INVÁLIDA\n')
        resul == a / b
        return resul

def main():
    while True:
        calculadora = Calculadora()
        print('\nCALCULADORA\n[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAÇÃO\n[4]DIVIDIR\n[5]SAIR\n')
        operacao = int(input('DIGITE O QUE DESEJA FAZER: '))
        a = float(input('N1: '))
        b = float(input('N2: '))

        if operacao == 1:
            return calculadora.somar(a, b)
        elif operacao == 2:
            return calculadora.subtrair(a, b)
        elif operacao == 3:
            return calculadora.multiplicar(a, b)
        elif operacao == 4:
            return calculadora.dividir(a, b)
        elif operacao == 5:
            print('\nENCERRANDO SISTEMA\n')
            break
        else:
            print('\nOPÇÃO INVÁLIDA\n')
            
        resultado = calculadora.calcular(operacao, a, b)
        print('O RESULTADO É: ', resultado, '\n')

if __name__ == "__main__":
    main()
