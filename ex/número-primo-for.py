# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Assume que o número é primo até que se prove o contrário
eh_primo = True

# Um número menor ou igual a 1 não é primo
if numero <= 1:
    eh_primo = False
else:
    # Verifica se o número tem divisores entre 2 e a raiz quadrada de 'numero'
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break  # Sai do laço se encontrar um divisor

# Exibe o resultado
if eh_primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
