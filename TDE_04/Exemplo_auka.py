



from cmath import sqrt


nome="ramon"
nome2="ramon"
if nome != nome2:
    print("nomes diferente")
else:
    print("nomes iguais")
is_umidade=False
umidade=60

#is_umidade=True if umidade >= 50 else is_umidade=False
if umidade>=50:
    is_umidade=True
else:
    is_umidade=False

nota_ps=float(input("Digite a nota"))
if nota_ps >=6:
    print("Você foi aprovado\n")
    print("Parabéns\n")
    if nota_ps>9:
        print("você é d+")
elif nota_ps<6 and nota_ps>4:
    print("Você pegou exame")
    print("Sem pizza galera")
else:
    print("você não foi aprovado")

print(f"sua nota é{nota_ps}")

