import numpy as np

GRAU_DESEJADO = 2
Vum = [-2, -1,  0,  1,   2]
W = [-7,  7,  15, 17, 13]

vetores = []
grau = GRAU_DESEJADO
while grau > 1:
    vetores.append([numero ** grau for numero in Vum])
    grau -= 1

vetores.append(Vum)
vetor_de_ums = list(np.ones(len(Vum)))
vetores.append(vetor_de_ums)

tamanho_da_matriz = GRAU_DESEJADO + 1
matriz_esquerda = np.zeros((tamanho_da_matriz, tamanho_da_matriz))
for i_matriz, matriz in enumerate(matriz_esquerda):
    for i_elemento, elemento in enumerate(matriz):
        matriz_esquerda[i_matriz][i_elemento] = np.inner(vetores[i_matriz], vetores[i_elemento])

matriz_direita = [np.inner(W, vetor) for vetor in vetores]

resposta = np.linalg.solve(matriz_esquerda, matriz_direita)
print(resposta)
