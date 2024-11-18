minha_tupla = (1, 2, 3, "Python", True)

tupla_vazia = ()

tupla_unica = (42,)  # Necessário usar a vírgula

#Acessar elementos: Use índices, como nas listas
minha_tupla = (10, 20, 30)
print(minha_tupla[0])  # 10
print(minha_tupla[-1])  # 30

#Fatiamento: Tuplas suportam fatiamento para acessar subconjuntos
print(minha_tupla[1:])  # (20, 30)
print(minha_tupla[:2])  # (10, 20)

#iterar
cores = ("vermelho", "verde", "azul")
for cor in cores:
    print(cor)

#unir e reptir tuplas
tupla1 = (1, 2)
tupla2 = (3, 4)
nova_tupla = tupla1 + tupla2  # (1, 2, 3, 4)
repetida = tupla1 * 3  # (1, 2, 1, 2, 1, 2)

#verificar a presença de elemento
if 20 in minha_tupla:
    print("Está na tupla!")

#tamanho da tupla
print(len(minha_tupla))  # 3

#count(): Retorna o número de vezes que um valor aparece
tupla = (1, 2, 2, 3)
print(tupla.count(2))  # 2

#index(): Retorna o índice da primeira ocorrência de um valor
print(tupla.index(2))  # 1

#Desempacotamento
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)  # 1 2 3