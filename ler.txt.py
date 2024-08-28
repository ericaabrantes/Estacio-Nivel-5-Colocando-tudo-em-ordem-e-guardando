# Abrindo e lendo o conteúdo do arquivo txt
arquivo = open("loremipsum.txt", "r")

# Imprimindo todo o conteúdo do arquivo
conteudo_completo = arquivo.read()
print("Conteúdo completo do arquivo:\n", conteudo_completo)

# Retornando ao início do arquivo para ler a primeira linha
arquivo.seek(0)
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:\n", primeira_linha)

# Retornando ao início do arquivo para ler os 3 primeiros caracteres
arquivo.seek(0)
tres_primeiros_caracteres = arquivo.read(3)
print("\nOs 3 primeiros caracteres do arquivo:\n", tres_primeiros_caracteres)

# Fechando o arquivo
arquivo.close()

# Utilizando a instrução 'with' para abrir o arquivo e ler seu conteúdo
with open("loremipsum.txt", "r") as arquivo_com_with:
    conteudo_com_with = arquivo_com_with.read()
    print("\nConteúdo lido com 'with':\n", conteudo_com_with)