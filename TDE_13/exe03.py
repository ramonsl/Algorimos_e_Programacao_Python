
#3. Faça um programa que receba a idade, a altura e o peso de 25 pessoas, calcule e mostre:
#a) quantidade de pessoas com idade superior a 50 anos;\
#b) ‘media’ das alturas das pessoas com idade entre 10 (inluindo) e 20 incluido anos;
#c) percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.


from statistics import median


quantidade_pessoas_50=0
quantidade_pessoas_10_20=0
soma_altura_pessoas_10_20=0
pessoas_peso_40=0
quantidade=25

for i in range(quantidade):
    altura=int(input("Digite sua altura em cm\n"))
    peso=float(input("Digite o seu peso\n"))
    idade=int(input("Digite o seu idade\n"))
    if idade>50:
        quantidade_pessoas_50+=1
    if idade>=10 and idade <=20:
        quantidade_pessoas_10_20+=1
        soma_altura_pessoas_10_20+=altura
    if peso<40:
        pessoas_peso_40+=1

print(f"Quantidade de pessoas com mais de 50:{ quantidade_pessoas_50}")
if quantidade_pessoas_10_20!=0:
    media_altura=soma_altura_pessoas_10_20/quantidade_pessoas_10_20
    print(f"Media de altura:{ media_altura}")
else:
    print("Não há pessoas entre 10 e 20")

porcentaem=(pessoas_peso_40/quantidade)*100
print(f"A porcentagem é {porcentaem}")