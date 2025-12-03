faturamento = input("Preencha com o faturamento (apenas números)")    
faturamento = faturamento.replace("R$,", "."). replace(",", ".")
faturamento = float(faturamento)
custo = 600
custo = input("Preencha com o custo (apenas números)")
custo = float(custo)

lucro = faturamento - custo
print(faturamento)

vendas_dia1 = float(input("Venda dia 1: "))
vendas_dia2 = float(input("Venda dia 2:")) 

print(vendas_dia1 + vendas_dia2)