import random

# Gera um número aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

# Laço para as tentativas do usuário
while True:
    try:
        tentativa = int(input("Digite sua tentativa: "))
        
        if tentativa < 1 or tentativa > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue
        
        if tentativa < numero_aleatorio:
            print("Muito baixo! Tente novamente.")
        elif tentativa > numero_aleatorio:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_aleatorio}!")
            break
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")


#While
senha = "123"
while True:
    passw = input("Digite a senha")
    if passw == senha:
        break
    else:
        print("Senha invalida")