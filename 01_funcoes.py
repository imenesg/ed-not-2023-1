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
        
   valores = [2,3,5,7,9,11,"batata", "tomate", True]

for v in valores:
    print(v)

valores.append(29)
print("="*80)
valores.insert(4, "chuchu")
print(valores)

print("="*80)
valores.insert(0, "abobrinha")
print(valores)


#acessando posições especificas
print("="*80)
print("Elemento na setima posição", valores[6])
print("Elemento na terceira posição", valores[2])
print("Elemento na ultima posição", valores[-1])
print("Elemento na penultima posição", valores[-2])
print(valores)

#substituindo valores
print("antes:", valores)
valores[10] = "cenoura"

valores[0] = "beterraba"
valores[-1] = "alho"

print("depois:", valores)



