# Importa uma biblioteca Python2 que trabalha com equacoes matematicas
import numpy as np


# Sera tomado como exemplo o seguinte sistema linear: 
#  x -2y -2z = -1
#  x  -y  +z = -2
# 2x  +y +3z = 1

# Linha 1 =  x -2y -2z = -1
# Linha 2 =  x  -y  +z = -2
# Linha 3 = 2x  +y +3z =  1


# O programa recebe do usuario a quantida de equacoes que ele deseja inserir (Serao transformadas em uma matriz depois).
# Nesse caso, temos 3 linhas, entao qtd_linhas = 3
qtd_linhas    = int(input('Digite a quantidade de linhas do sistema linear desejado: '))

# Nesse caso, temos tambem 3 incognitas, entao qtd_variaveis = 3
# O programa recebe a quantidade de incognitas que existira em cada uma das linhas.
qtd_variaveis = int(input('Digite a quantidade de variaveis (incognitas): '))
print('\n')


# Agora o programa ira montar dinamicamente, com a ajuda do usuario.
# O objetivo e montar a seguinte matriz (baseado no sistema linear usado como exemplo)
# | 1 -2 -2 | -1 |
# | 1 -1  1 | -2 |
# | 2  1  3 |  1 |

matriz = []
respostas = []
for numero_linha, linha in enumerate(range(qtd_linhas)):
    # Para cada linha informada, sera criada uma lista [] que tera dentro dela armazenada cada uma das variaveis daquela linha.
    # Ou seja, linha_construida ao fim do range() de 3 (que e qtd_linhas), sera: linha_construida = [1, -2, -2]
    linha_construida = []
    for numero_variavel,variavel in enumerate(range(qtd_variaveis)):
        entrada = int(input('Digita a variavel '+str(numero_variavel+1)+' da linha: ' + str(numero_linha+1)+': '))
        linha_construida.append(entrada)
         # Recebemos o valor de x, y, z para uma determinada linha, e entao colocamos dentro de linha_construida
    resposta = int(input('Digita a resposta da linha: ' + str(numero_linha+1)+': '))
    # Aqui recebemos o valor para a coluna da direita. Por exemplo, para a primeira linha [1, -2, -2], reposta sera = -1
    print('\n')
    respostas.append(resposta)
    # Resposta se encontra como uma matriz vetor de um elemento [-1], porem assim que o 'for' continuar, ira receber -2 e por fim 1
    matriz.append(linha_construida)
    # Apos as 3 variaveis serem recebis pelo usuario, uma linha sera montada, como dito anteriormente. A primeira linha_construida sera:
    # [1, -2, -2]. Dentro de matriz, estamos colocando essa linha.
    # Matriz sera uma lista com varias listas dentro. Ou seja, no caso do exemplo, uma lista com 3 'listas/linhas dentro'.
    
    # Ao fim, 'matriz' possui a seguinte configuracao = [[1, -2, -2],[1, -1,  1],[2,  1,  3]]
    # E 'respostas' possui a seguinte configuracao = [-1, -2, 1]

# Apenas usamos as matrizes contruidas para informar ao numpy qual matriz e qual.
# A = matriz montada pelo usuario de incognitas -> [[1, -2, -2],[1, -1,  1],[2,  1,  3]]
# B = matriz montada pelo usuario de respostas  -> [-1, -2, 1]
A = np.array(matriz) 
B = np.array(respostas) 

# Resolucao usando a biblioteca
print('Resposta: ')
print(np.linalg.solve(A, B ))
