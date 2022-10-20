
#Faça um programa que leia a matrícula, o nome e às três notas de 10 alunos, e indique para cada aluno, se ele foi aprovado ou não, considere a média 7.

for i in range(10):
    nota_01=float(input("Digite a nota 1"))
    nota_02=float(input("Digite a nota 2"))
    nota_03=float(input("Digite a nota 3"))
    media= (nota_01+nota_02+nota_03)/3
    if media>=7:
        print(f"Aprovado {media}")
    else:
        print(f"Reprovado {media}")