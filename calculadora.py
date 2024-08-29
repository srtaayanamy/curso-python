class Calculadora:
    def __init__(self):
        pass
    
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        return a / b

    def calcular(self, operacao, a, b):
        if operacao == "soma":
            return self.somar(a, b)
        elif operacao == "subtracao":
            return self.subtrair(a, b)
        elif operacao == "multiplicacao":
            return self.multiplicar(a, b)
        elif operacao == "divisao":
            return self.dividir(a, b)
        else:
            return "Operação inválida!"

def main():
    calc = Calculadora()

    print("Operações disponíveis: soma, subtracao, multiplicacao, divisao")
    operacao = input("Digite a operação desejada: ").lower()
    
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        
        resultado = calc.calcular(operacao, a, b)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: Por favor, insira números válidos.")

if __name__ == "__main__":
    main()