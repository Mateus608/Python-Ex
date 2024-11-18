import numpy as np

#Soma de Linhas e Colunas
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
soma_linhas = np.sum(matriz, axis=1) # Somando as linhas
soma_colunas = np.sum(matriz, axis=0) # Somando as colunas

#Multiplicação de Matrizes
matriz1 = np.array([[1, 2],
                    [3, 4]])
matriz2 = np.array([[5, 6],
                    [7, 8]])
produto = np.dot(matriz1, matriz2) # Calculando o produto das matrizes

#Encontrar Elemento Máximo por Linha
matriz = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
maximos_linhas = np.max(matriz, axis=1) # Encontrando o elemento máximo de cada linha

#Encontrar Elemento Máximo por Coluna
matriz = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
maximos_colunas = np.max(matriz, axis=0) # Encontrando o elemento máximo de cada coluna

#Transposição de Matriz
matriz = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
matriz_transposta = np.transpose(matriz)

#Rotacionar a matriz em 90 Graus
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matriz_rotacionada = np.rot90(matriz, k=-1)  # k=-1 indica rotação no sentido horário


'''
Construa um algoritmo que gere a seguinte matriz: 
111111
122221
123321
123321
122221
111111
'''
# Inicializando a matriz 6x6
matriz = []

# Construindo a matriz conforme o padrão solicitado
for i in range(6):
    linha = []
    for j in range(6):
        if i == 0 or i == 5:  # Primeira e última linha
            linha.append(1)
        elif i == 1 or i == 4:  # Segunda e penúltima linha
            linha.append(min(j+1, 6-j))
        else:  # Terceira e quarta linha
            linha.append(min(j+1, 7-j))
    matriz.append(linha)

# Exibindo a matriz
for linha in matriz:
    print("".join(map(str, linha)))
