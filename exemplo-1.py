# Programação Estruturada

nome = "Camiseta"
preco = 50.0

def aplicar_desconto(preco, desconto):
    return preco - (preco * desconto)

aplicar_desconto(preco, 0.1)

print(nome, preco)

nome = "Calça Jeans"
preco = 90.0

aplicar_desconto(preco, 0.1)

print(nome, preco)
