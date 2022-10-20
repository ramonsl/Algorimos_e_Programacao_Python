#Efetue um programa que leia a nota de 10 alunos de uma turma. 
# Ao final, deve ser escrita a média geral da turma. Esse algoritmo deve ser feito duas vezes, uma usando o FOR, e WHILE


media=0
soma=0 #acumuladora
nota_aluno=0
quantidade_de_notas=0  #contadora
leituras_obrigatorias=10

for quantidade_de_notas in range(leituras_obrigatorias):
    nota_aluno=float(input("Digite a nota do aluno"))
    soma=soma+nota_aluno

media=soma/leituras_obrigatorias
print (f"A média é {media} ")