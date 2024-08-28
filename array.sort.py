import random

# Criação de um array de 15 posições com números inteiros aleatórios
array_numeros = [random.randint(1, 100) for _ in range(15)]

# Imprimindo o array original
print("Array original:", array_numeros)

# Ordenando o array de forma crescente
array_numeros.sort()
print("Array ordenado de forma crescente:", array_numeros)

# Ordenando o array de forma decrescente
array_numeros.sort(reverse=True)
print("Array ordenado de forma decrescente:", array_numeros)

# Criação de um array de strings
array_strings = ["banana", "laranja", "uva", "maçã", "abacaxi", "manga", "pêssego", "morango", "cereja", "pera"]

# Imprimindo o array de strings original
print("\nArray de strings original:", array_strings)

# Ordenando o array de strings de forma crescente
array_strings.sort()
print("Array de strings ordenado de forma crescente:", array_strings)

# Ordenando o array de strings de forma decrescente
array_strings.sort(reverse=True)
print("Array de strings ordenado de forma decrescente:", array_strings)