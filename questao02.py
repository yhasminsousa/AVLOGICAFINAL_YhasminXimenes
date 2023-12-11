#reajuste dos salários.

# 0 - 400.00          -    15%
# 400.01 - 800.00     -    12%
# 800.01 - 1200.00    -    10%
# 1200.01 - 2000.00   -    7%
# acima de 2000.00    -    4%
# valor do salário, valor do reajuste e percentual de ajuste ganho

salarioatual = float(input("digite seu salário atual:"))
if salarioatual > 0 and salarioatual < 400.00:
    newsalario = (salarioatual*15)/100
    nuevosalario = (newsalario+salarioatual)                                                                                                                                                                                                                                                                                                                                                 
    print (f"seu salário atual é de:{nuevosalario}")
    print (f"o valor do reajuste é de>:{newsalario}")
    print (f"o percentual de ajuste é de 15%")

if salarioatual > 400.01 and salarioatual <= 800.00: 
    salario20 = (salarioatual*12)/100
    salario21 = (salarioatual+salario20)
    print (f"seu salário atual é de:{salario21}")
    print (f"o valor do reajuste é de>:{salario20}")
    print (f"o percentual de ajuste é de 12%") 

if salarioatual > 800.01 and salarioatual <= 1200.00:
    salario23 = (salarioatual*10)/100
    salario24 = (salarioatual+salario23)
    print (f"seu salário atual é de:{salario24}")
    print (f"o valor do reajuste é de>:{salario23}")
    print (f"o percentual de ajuste é de 10%") 

if salarioatual > 1200.01 and salarioatual <= 2000.00:
    salario25 = (salarioatual*7)/100
    salario26= (salarioatual+salario25)
    print (f"seu salário atual é de:{salario26}")
    print (f"o valor do reajuste é de>:{salario25}")
    print (f"o percentual de ajuste é de 7%") 

else:
    ajuste05 = (salarioatual*4)/100
    ajuste04 = (salarioatual+ajuste05)
    print (f"seu salário atual é de:{ajuste04}")
    print (f"o valor do reajuste é de>:{ajuste05}")
    print (f"o percentual de ajuste é de 4%")
    


