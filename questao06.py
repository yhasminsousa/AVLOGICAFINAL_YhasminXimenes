# ler 6 valores
# indicar quantos são positivos.

positivos = [float(input("digite os valores:")) for _6
    in range (6)] #colocar em for in range para a contagem.
totalpositivos = 0
somadosposit = 0

for j in positivos:
    if j > 0:
        totalpositivos += 1 #contagem de positivos
        somadosposit += j # soma deles

print('{} valores positivos' .format(totalpositivos))
print('{:.1f}'.format(somadosposit/totalpositivos))

