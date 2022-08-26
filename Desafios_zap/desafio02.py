#Sabendo que o Sky come duas vezes no dia 180 gramas de ração.
#Que o preço medio do saco de ração de 10kg é de 200 reais ( come melhor que eu esse jaguara)
#Faça um algoritmo que mostre quanto vou gastar de dinheiro em um ano.

porcao=float(input("Quantas gramas por dia?"))
racao_dia=porcao*2
saco_racao_kg=int(input("Quantos kg tem no saco"))
saco_racao_gramas=saco_racao_kg*1000
preco=int(input("Quanto custa o saco?"))
valor_gramas=preco/saco_racao_gramas
consumo_gramas=(racao_dia)*365
valor_ano=consumo_gramas*valor_gramas
print(f"Preco da grama de racao R${valor_gramas}")
print(f"Consumo no ano em gramas {consumo_gramas}")
print(f"Consumo no ano em Kg {consumo_gramas/1000}")
print(f"Valor do ano em racao R${valor_ano}")
sacos_ano=(consumo_gramas/1000)//saco_racao_kg
print(f"Quantos sacos preciso no ano {sacos_ano}")

