'''
    programa: main.py
    data: 16/09/2024
    autor: prof. Marcelo Almeida
    breve descrição: uso da estrutura de
        repetição WHILE com uso de ELSE
        uso da estrutura de repetição FOR

#numero maximo de tentativas
max_attemps = 3

#senha correta a ser atingida
correct_password = "123senha"

#contador de tentativas
attemp = 0

while attemp < max_attemps:
    #entrada do usuario
    password = input("Entre com a senha: ")

    #verificar se a senha está correta
    if password == correct_password:
        print("Login efetuado com sucesso")
        #quebrar o laço
        break
    else:
        #aumenta o contador de tentativa
        attemp += 1
        #informa usuario que senha é inválida
        print(f"Senha inválida! Tentativa {attemp} de {max_attemps}")
else:
    #este bloco será executado se o laço 
    # terminar sem sucesso
    print("Número máximo de tentativas atingido. Acesso bloqueado")

'''

#estrutura basica for
# for variavel in sequencia:

#for i in range(5):
 #   print(i)

#outra linguagens
# for(variavel; condicao parada; incremento/decremeto)
# for(i = 0; i<5; i++)

#for i in range(2,6):
 #   print(i)

#for i in range(0,10,2):
#    print(i)

#programa que gera senha de 8 digitos aleatoria
'''
import random
import string

tamanho_senha = 8
caracteres = string.ascii_letters + string.digits

senha = ''
for i in range(tamanho_senha):
    senha += random.choice(caracteres)

print(f"senha gerada: {senha}")
'''
'''
import random

for i in range(1,6):
    dado = random.randint(1,20)
    if dado == 1:
        print("falha crítica") 
    else:   
        print(f"Lançamento {i}: {dado}")
'''

for i in range(10):
    for j in range(10):
        print(f"{i},{j}")
