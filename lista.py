# Lista vazia
minha_lista = []

# Lista com diferentes tipos de dados
minha_lista = [1, 2, "Python", True, 3.14]

minha_lista = [1, 2, 3]

#adiciona um item ao final da lista.
minha_lista.append(4)  # [1, 2, 3, 4]

#insere um item em uma posição específica.
minha_lista.insert(1, "novo")  # [1, "novo", 2, 3, 4]

# Primeiro elemento
print(minha_lista[0])
# Último elemento
print(minha_lista[-1])

# [1, "Python", 2, 3, 4]
minha_lista[1] = "Python"

#remove o primeiro elemento com o valor especificado.
minha_lista.remove("Python")  # [1, 2, 3, 4]

#remove e retorna um elemento por índice.
minha_lista.pop(2)  # Remove o elemento no índice 2 ([1, 2, 4])

#remove elementos ou fatias.
del minha_lista[0]  # [2, 4]

#tamanho da lista
print(len(minha_lista))  # Quantidade de elementos

#verificar a presença de elementos
if 2 in minha_lista:
    print("O número 2 está na lista!")

#ordenar e inverter
lista_numeros = [3, 1, 4, 1, 5]
lista_numeros.sort()  # [1, 1, 3, 4, 5]
lista_numeros.reverse()  # [5, 4, 3, 1, 1]

#combinar listas
lista1 = [1, 2]
lista2 = [3, 4]
lista_combinada = lista1 + lista2  # [1, 2, 3, 4]

#copiar lista
copia = minha_lista.copy()

#iterar
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)  # Exibe cada número da lista


#remover duplicatas
lista_com_dup = [1, 2, 3, 1, 4, 5, 3, 6]
lista_sem_dup = list(set(lista_com_dup))
print(lista_sem_dup)
