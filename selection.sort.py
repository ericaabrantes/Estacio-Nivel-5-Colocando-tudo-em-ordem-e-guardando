# Array de números com 15 posições, sem ordenação
array = [29, 10, 14, 37, 13, 2, 25, 17, 7, 21, 5, 45, 32, 18, 1]

# Loop para percorrer todos os elementos do array
for i in range(len(array)):
    # Variável para armazenar o índice do menor elemento
    min_idx = i
    
    # Loop para encontrar o menor elemento na sublista restante
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j  # Atualiza o índice do menor elemento
    
    # Troca de elementos
    array[i], array[min_idx] = array[min_idx], array[i]

# Imprimir o array ordenado
print("Array ordenado de forma crescente:", array)