import numpy as np


# |V2V2   V2V1   V2V0
# |V1V2   V1V1   V1V0
# |V0V2   V0V1   V0V0

GRAU_DESEJADO = 2
Vum = [-2, -1,  0,  1,   2]
W   = [-7,  7,  15, 17, 13]


# Cria todos os V's que sersão utilizados, além de adicionar
# os pontos dados 'Vum' e também o conjunto de um's ao fim.
grau = GRAU_DESEJADO
vetores = []
while grau > 1:
    vetores.append([numero ** grau for numero in Vum])
    grau -= 1
vetores.append(Vum)
vetores.append(list(np.ones(len(Vum))))
print(vetores)
print('\n')


# Determina os valores das diagonais principais
# baseados nos pontos calculados anteriormente.
tamanho_da_matriz = GRAU_DESEJADO + 1
matriz_esquerda = np.zeros((tamanho_da_matriz, tamanho_da_matriz))
for i_matriz, matriz in enumerate(matriz_esquerda):
    for i_elemento, elemento in enumerate(matriz):
        if i_matriz == i_elemento:
            matriz_esquerda[i_matriz][i_elemento] = np.inner(vetores[i_matriz], vetores[i_elemento])
        else:
            matriz_esquerda[i_matriz][i_elemento] = np.inner(vetores[i_matriz], vetores[i_elemento])
print(matriz_esquerda)


matriz_direita = [np.inner(W, vetor) for vetor in vetores]
print(matriz_direita)


print(np.linalg.solve(matriz_esquerda, matriz_direita))
