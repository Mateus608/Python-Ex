# Inicializando a matriz 5x5
matriz = []

# Lendo os valores da matriz
print("Digite os elementos da matriz 5x5 (inteiros):")
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f"Elemento [{i+1},{j+1}]: ")))
    matriz.append(linha)

# Calculando a soma de todos os elementos
soma = 0
for i in range(5):
    for j in range(5):
        soma += matriz[i][j]

# Calculando a média aritmética
media = soma / 25

# Exibindo os resultados
print("\nSoma de todos os elementos:", soma)
print("Média aritmética:", media)
