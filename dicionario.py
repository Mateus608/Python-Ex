#criando um dicionario
dados_pessoais = {
    "nome" : "Marcelo",
    "idade" : "40",
    "cidade" : "SJBV"
}

#acessar valor
#usando colchetes
print(dados_pessoais["nome"])
#usando metodo get
print(dados_pessoais.get("nome"))

#adicionar uma nova chave
dados_pessoais["profissao"] = "professor"

#atualizar item
dados_pessoais["nome"] = "Marcelo Ciacco"

#remover item
#remover pelo indice, com DEL
del dados_pessoais["cidade"]
#remover com metodo pop()
profissao = dados_pessoais.pop("profissao")

#verificar a existencia de uma chave
if "nome" in dados_pessoais:
    print("Chave nome está presente no dicionario")

#keys() - retorna todas as chaves
print(dados_pessoais.keys())

#values() - retorna valores
print(dados_pessoais.values())