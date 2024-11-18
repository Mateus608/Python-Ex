import numpy as np

# Criando uma matriz 2x3 (2 linhas e 3 colunas)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
matriz2 = np.array([[7,8,9],[10,11,12]])

# Exibindo a matriz
print("Matriz:")
print(matriz)

# Somando duas matrizes
print("\nSomando duas matrizes:")
soma = matriz + matriz2
print(soma)

# Acessando um elemento específico (linha 1, coluna 2)
print("\nElemento na linha 1, coluna 2:")
print(matriz[0, 1])  # Lembre-se que o índice começa de 0

# Transpondo a matriz
print("\nMatriz transposta:")
transposta = np.transpose(matriz)
print(transposta)

# Operações com a matriz
# Soma de todos os elementos
print("\nSoma de todos os elementos:")
print(np.sum(matriz))

print("\nMatriz inversa:")
matriz3 = np.array([[1,2],[4,5]])
#matriz inversa
inversa = np.linalg.inv(matriz3)
print(inversa)