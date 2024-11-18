import numpy as np

palavras = {
    "maça" : "3",
    "banana" : "2",
    "laranja" : "1"
}

#remover duplicatas
lista_com_dup = [1, 2, 3, 1, 4, 5, 3, 6]
lista_sem_dup = list(set(lista_com_dup))
print(lista_sem_dup)

#soma de valores pares
lista = np.array([1, 2, 3, 1, 4, 5, 3, 6])
print(np.sum(lista[lista % 2 == 0]))

#contar numeros positivos e negativos
postivoNegativo = np.array([2,4,-8,-5,10,-9,6])
print(np.count_nonzero(postivoNegativo[postivoNegativo > 0]))
print(np.count_nonzero(postivoNegativo[postivoNegativo < 0]))

#Diferença entre Máximo e Mínimo
arr = np.array([2,6,4,10])
maior = np.max(arr)
menor = np.min(arr)
print(maior-menor)

#Inverter Ordem dos Elementos
inverter = np.array([1,2,3,4,5,6,7,8,9])
print(inverter[::-1])

#Substituir Valores Negativos por Zero
postivoNegativo[postivoNegativo < 0] = 0
print(postivoNegativo)

# Verificar número
arrN10 = np.array([2,10,4,13,7,8,15,16,19,3])
numero = int(input("Digite um número: "))
if numero in arrN10:
    print("Número encontrado")
else:
    print("Número não encontrado")


#Rotação à direita
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# Número de rotações à direita
n = 1
# Garantindo que n não exceda o tamanho do array
n = n % len(array)
# Rotação direta
array_rotacionado = np.concatenate((array[-n:], array[:-n]))


#Rotação à esquerda
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# Número de rotações à direita
n = 1
# Garantindo que n não exceda o tamanho do array
n = n % len(array)
# Rotação direta
array_rotacionado = np.concatenate((array[n:], array[:n]))


#União e Interseção
# Gerar os arrays A e B com números aleatórios de 1 a 50
A = np.random.randint(1, 51, 8)
B = np.random.randint(1, 51, 8)
# Declarar os arrays C e D
# C = União de A e B
C = np.union1d(A, B)
# D = Interseção de A e B
D = np.intersect1d(A, B)
# Completar D com zeros até 8 posições (se necessário)
D = np.pad(D, (0, 8 - len(D)), 'constant')

#Números maiores que a média do array
# Calcular a média dos elementos
media = sum(array) / len(array)
# Encontrar os valores maiores que a média
maiores_que_media = [num for num in array if num > media]