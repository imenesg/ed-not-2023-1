# LISTAS EM PYTHON
# Listas são uma forma de armazenar mais de um valor


# Uma lista de números
valores = [2, 3, 5, 7, 9, 11, "batata", "tomate", True]

# OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO: significa percorrer a lista do primeiro
#    até o último elemento, fazendo algo com cada um
#    deles. No caso a seguir, vamos exibir cada um dos
#    elementos separadamente usando print().
for val in valores:
    print(val)

print("*" * 80)     # Imprime * 80 vezes

# 2) INSERÇÃO DE UM NOVO ELEMENTO NO *FIM* DA LISTA: append()
valores.append("cebola")
print(valores)

valores.append(29)
print(valores)

print("*" * 80)

# 3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1º: posição para inserir (contagem inicia em 0)
#    2º: valor a ser inserido
valores.insert(4, "chuchu")     # Insere "chuchu" na 5ª posição
print(valores)

valores.insert(0, "abobrinha")  # Insere "abobrinha" na 1ª posição
print(valores)

print("-" * 80)

# 4) ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECÍFICA
print('Elemento na SÉTIMA posição:', valores[6])
print('Elemento na TERCEIRA posição:', valores[2])
print('Elemento na PRIMEIRA posição:', valores[0])
print('Elemento na ÚLTIMA posição:', valores[-1])
print('Elemento na PENÚLTIMA posição:', valores[-2])
print(valores)

print('-' * 80)

# 5) SUBSTITUINDO VALORES EXISTENTES
print("ANTES:", valores)

# Substituindo o valor da posição 10
valores[10] = "cenoura"
# Substituindo o valor da posição 0
valores[0] = "beterraba"
# Substituindo o valor da última posição
valores[-1] = "alho"

print("DEPOIS:", valores)

