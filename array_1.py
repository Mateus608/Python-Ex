import numpy as np

#criando array com numpy, todos valores esmo tipo
array = np.array([1,2,3,4,5])

#mostrar o array
print("Array:",array)

#mostrar array indice 2
print(array[2])

#alterar array indice 4
array[4] = 10
print("Array:",array)

#operações matemáticas
array2 = np.array([1,2,3,4,5])

soma = array + array2
print("Soma: ",soma)

#multiplicação escalar
mult = array2 * 2
print("Multiplicação por escalar: ",mult)

#fatiamento
array3 = np.array([0,10,20,30,40,50])
sub_array = array3[1:4]
print(sub_array)

#calcular media
media = np.mean(array3)
print(media)