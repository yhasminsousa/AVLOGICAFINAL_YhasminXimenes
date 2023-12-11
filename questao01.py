#calcular o valor do imposto que uma pessoa de Lisarb 
#deve pagar de acordo com seu salário.

#0.00 - 2.000 -> não paga
#2.001 - 3.000 -> 8%
#3.001 - 4.500 -> 18%
#acima de 4.501 -> 28% 

salario = float(input("digite o valor de seu salário:"))
if salario > 0 and salario <= 2000.00:
    notimposto = (salario) 
    print("não paga imposto")

elif salario > 2000.00 and salario < 3000.00:
    impost01 = (salario*8) / 100 
    print(f"você pagará um imposto de: {impost01}")
    
elif salario > 3000.00 and salario <= 4500.00:
    impost02 = (salario*18)/100
    print(f"seu imposto é de: {impost02}")

else:
    impost03 = (salario*28)/100
    print(f"seu imposto é de: {impost03}")

