#6. Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.

#1 ler varias idade (while)
# finalizar com 0
#mostra a media

soma_idade=0
cont_idade=0
idade=99
while idade!=0:
    idade=int(input(f"digite a idade da pessoa {cont_idade+1}:\n"))
    if idade==0:
        break
    cont_idade+=1
    soma_idade+=idade

media=soma_idade/cont_idade
print(f"A media é {media}")
print(f"Foram lidas  {cont_idade}")