#3. Faça um programa que receba a idade, a altura e o peso de 25 pessoas, calcule e mostre:
#a) quantidade de pessoas com idade superior a 50 anos;\
#b) ‘media’ das alturas das pessoas com idade entre 10 e 20 anos;
#c) percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.


#usar um laco (for) 25
tamanho=25 #mudar para 25 depois
contar_maior_50=0
contar_entre_10_e_20=0
soma_das_alturas=0
contar_peso_menor_40=0
for i in range (tamanho):
#ler idade , altura e peso
    idade=int(input(f" Digite a idade da pessoa {i+1} "))
    altura=int(input(f" Digite a altura em cm da pessoa {i+1} "))
    peso=float(input(f"Digite o peso em kg da pessoa {i+1} "))
    #quantidade idade maior que cinquenta
    if idade>=50:
        contar_maior_50+=1 #conta_maior= conta_maior_50+1
     #media alturas entre 10 e 20 anos / somar alturas, contar pessoas e depois dividir pela quantidas
    if idade>=10 and idade <=20:
        contar_entre_10_e_20+=1
        soma_das_alturas+=altura
    #porcentagem peso inferior a 40 / contar pessoas
    if peso<40:
        contar_peso_menor_40+=1

print(f"A- Maiores de 50={contar_maior_50}") 
media_altura=soma_das_alturas/contar_entre_10_e_20
print(f"B- Média das alturas é{media_altura}")
percetangem=(contar_peso_menor_40/tamanho)*100
print(f"c- Percentagem éé{percetangem}%")



