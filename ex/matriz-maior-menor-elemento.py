# Inicializando a matriz 6x3
matriz = []

# Lendo os valores da matriz
print("Digite os elementos da matriz 6x3 (inteiros):")
for i in range(6):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Elemento [{i+1},{j+1}]: ")))
    matriz.append(linha)

# Encontrando o maior e o menor elemento
maior_elemento = max(max(linha) for linha in matriz)
menor_elemento = min(min(linha) for linha in matriz)

# Exibindo os resultados
print("\nMaior elemento:", maior_elemento)
print("Menor elemento:", menor_elemento)
