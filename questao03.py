#repetir a leitura de uma senha até que ela seja válida.

senha = int(input("Digite o número da senha:"))
while senha != 2002:
    print("Senha invalida!")
    senha = int(input("digite o número da senha:"))

print("Acesso permitido!")

