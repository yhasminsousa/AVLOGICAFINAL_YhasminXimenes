# programa que leia 5 números inteiros.
# diga quantos são pares.

#contador
posit = [int(input("digite um inteiro:")) for _ in range (5)] #receber valores
totals = [par for par in posit if par % 2 == 0] #mostrar os pares
print("{} valores são pares".format(len(totals)))

