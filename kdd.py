import time

# Função Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Função Selection Sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

# Lendo o conteúdo do arquivo e armazenando em uma lista
with open("texto.txt", "r") as file:
    words = list()
    for line in file:
        words.extend(line.split())  # Separando cada linha em palavras e adicionando à lista

# Ordenação usando Bubble Sort
words_bubble = words.copy()
start_time = time.time()
bubble_sort(words_bubble)
bubble_time = time.time() - start_time
print("\nOrdenação Bubble Sort:")
print(words_bubble)
print(f"Tempo de execução (Bubble Sort): {bubble_time:.6f} segundos")

# Ordenação usando Selection Sort
words_selection = words.copy()
start_time = time.time()
selection_sort(words_selection)
selection_time = time.time() - start_time
print("\nOrdenação Selection Sort:")
print(words_selection)
print(f"Tempo de execução (Selection Sort): {selection_time:.6f} segundos")

# Ordenação usando o método nativo sort()
words_native = words.copy()
start_time = time.time()
words_native.sort()
native_time = time.time() - start_time
print("\nOrdenação Método Nativo (sort):")
print(words_native)
print(f"Tempo de execução (Método Nativo): {native_time:.6f} segundos")

# Escolhendo o método mais rápido e criando um novo arquivo txt com as palavras ordenadas
best_method = min((bubble_time, 'Bubble Sort'), (selection_time, 'Selection Sort'), (native_time, 'Método Nativo'), key=lambda x: x[0])
print(f"\nO método mais eficiente foi: {best_method[1]} com tempo de {best_method[0]:.6f} segundos")

# Salvando as palavras ordenadas usando o método mais eficiente em um novo arquivo
with open("palavras_ordenadas.txt", "w") as output_file:
    if best_method[1] == 'Bubble Sort':
        output_file.write("\n".join(words_bubble))
    elif best_method[1] == 'Selection Sort':
        output_file.write("\n".join(words_selection))
    else:
        output_file.write("\n".join(words_native))