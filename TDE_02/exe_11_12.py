#11.F.U.A que leia dois números e calcule qual é o resto da divisão do 1o pelo 2o número. Exiba na tela este valor final.
#12. F.U.A que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o número. Exiba na tela este valor final.

num01 = int(input("Digite numero 1\n"))
num02 = int(input("Digite numero 2\n"))

resto=num01%num02
quoeficiente = num01//num02


print(f"O resto é:{resto}")
print(f"o quoeficiente é: {quoeficiente}")