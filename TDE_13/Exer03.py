#3. Faça um programa que receba a idade, a altura e o peso de 25 pessoas, calcule e mostre:
#a) quantidade de pessoas com idade superior a 50 anos;\
#b) ‘media’ das alturas das pessoas com idade entre 10 e 20 anos;
#c) percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.

soma_pessoas = 0
idade_superior_50_anos = 0 
total_altura_10_20 = 0

pessoas_idade_10_20=0
soma_pessoas_peso_40 = 0
pessoas_peso_40=0

for i in range (3):
    idade  = int(input( "Digite a sua idade:"))
    altura = float(input("Digite a sua altura :"))
    peso = float(input("Digite o seu peso:"))

    soma_pessoas +=1

    if idade>50:
        idade_superior_50_anos+=1
    

    if idade >=10 and idade<=20:
        pessoas_idade_10_20+=1
        total_altura_10_20+=altura
        

    if peso < 40:
        soma_pessoas_peso_40+=1

print(f'O numero de pessoas com idade maior que 50 anos é {idade_superior_50_anos}')

if pessoas_idade_10_20!=0:
    print(f'A média de alturas das pessoas entre 10 e 20 anos é {total_altura_10_20/pessoas_idade_10_20}')
porcentagem= (soma_pessoas_peso_40/soma_pessoas)*100 
print(f'A porcentagem é {porcentagem}')
