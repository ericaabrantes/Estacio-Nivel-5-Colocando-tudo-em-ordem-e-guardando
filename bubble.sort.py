def bubbleSort(array):
    # Loop para percorrer todos os elementos do array
    for i in range(len(array)):
        # Loop para percorrer o array de dois em dois elementos
        for j in range(0, len(array) - i - 1):
            # Comparar e trocar os elementos adjacentes, se necessário
            if array[j] > array[j + 1]:
                # Troca de elementos
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Array de números com 15 posições
array_numeros = [64, 34, 25, 12, 22, 11, 90, 88, 1, 55, 29, 78, 45, 67, 3]

# Aplicação do método bubbleSort
bubbleSort(array_numeros)

# Imprimindo o array ordenado
print("Array ordenado de forma crescente:", array_numeros)