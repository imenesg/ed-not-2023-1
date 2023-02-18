"""
função para calcular o IMC, levando em conta o peso e a altura
"""
def imc(peso, altura):
    # Peso dividido pela altura elevada ao quadrado
    return peso / altura ** 2
resultado = imc(81, 1.75)
print(f"Seu Imc é de {resultado}")
#####################################
from math import pi
def calcula_area(base, altura, tipo):
    if tipo == "R": #retangulo
         return base * altura
    elif tipo == "T": #triangulo
        return base * altura / 2
    elif tipo == "E": #elipse
        return (base/2) * (altura/2) * pi
    else:
        return 




