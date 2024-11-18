''' ambiente = input("Ambiente a ser rodado: ")

#outras linguagens
#switch-case => escolha-caso

#PYTHON match-case
match ambiente:
    case "desenvolvimento":
        apiUrl = "http://localhost:3000/api"
#         outras linguagens
#         break
    case "teste":
        apiUrl = "http://ns.server.com/api"
    case "producao":
        apiUrl = "http://np.server.com/api"
#   outras linguagens
#   case default:
    case _:
        apiUrl = "http://localhost:3000/api"

print(apiUrl)

restful = input("Verbo de request: ")

match restful:
    case "get":
        print("Buscando dados...")
    case "post":
        print("Inserir novo registro")
    case "put":
        print("Atualizar um registro")
    case "delete":
        print("Remover um registro")
    case _:
        print("verbo de request invalido")

#Estrutura de repetição
#loop

#WHILE
#Repete bloco de código enquanto a condição for
#verdadeira
'''
import time 
import random

#numero de tentativas
max_attemps = 5

#contador de tentativas
attemp = 0

#flag para verficar sucesso
success = False

while attemp < max_attemps and not success:
    #attemp++ => incremento
    attemp += 1
    print(f"Tentativa {attemp} de {max_attemps}")

    #simulação da requisição
    response_status = random.choice([200,500])

    if(response_status == 200):
        print("Conexão efetuada com sucesso")
        success = True
    else :
        print("Erro de conexão, tentando novamente...")
        time.sleep(2) #pausa de 2 segundos no programa

if not success:
    print("Falha após várias tentativas. Tente novamente mais tarde.")





