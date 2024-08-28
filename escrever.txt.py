# Abrindo (ou criando) o arquivo texto.txt em modo de escrita
arquivo = open("texto.txt", "w")

# Criando uma lista para armazenar frases
texto = list()

# Adicionando frases à lista usando o método append
texto.append("Esta é a primeira frase.\n")
texto.append("Aqui está a segunda frase.\n")
texto.append("E finalmente, a terceira frase.\n")

# Escrevendo o conteúdo da lista no arquivo
arquivo.writelines(texto)

# Fechando o arquivo
arquivo.close()

print("O arquivo 'texto.txt' foi criado e as frases foram gravadas com sucesso.")