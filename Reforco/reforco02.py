#4.Faca um programa que receba a idade,o peso,a altura,a cor dos olhos(A-azul,P-preto,V-verde e C-castanho)e a cor dos cabelos(P-preto,C-castanho,L-louro e R-ruivo)de vinte pessoas,e que calcule e mostre:
#a)a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos;
#b)a média das idades das pessoas com altura inferior a 1,50 metro;
#c)a percentagem de pessoas com olhos azuis entre todas as pessoas analisadas;
#d)a quantidade de pessoas ruivas e que não possuem olhos azuis.

#fazer um laco de 20


tamanho=5
pessoa_50a_menos60=0
somar_idades=0
cont_alturas=0
cont_olhos=0
cont_ruivos=0
for i in range (tamanho):
#ler idade, peso,altura olhos e cabelos
    idade=int(input(f" Digite a idade da pessoa {i+1} "))
    altura=int(input(f" Digite a altura em cm da pessoa {i+1} "))
    peso=float(input(f"Digite o peso em kg da pessoa {i+1} "))
    olhos=input("Digite a cor dos seus olhos (A-azul,P-preto,V-verde e C-castanho)")
    cabelos=input("Digite a  cor dos cabelos(P-preto,C-castanho,L-louro e R-ruivo)")
#quantdiade pessoas >50 AND peso <60
    if idade>50 and peso <60:
        pessoa_50a_menos60+=1
#0 AND 0 = 0
#0 AND 1 = 0
#1 AND 0 = 0
#1 AND 1 = 1
#media das idade dos baixicnho 150
    if altura<150:
        somar_idades+=idade
        cont_alturas+=1
#percentagem olhos azuis entre todos
    if olhos=="a":
        cont_olhos+=1
#quantidade ruivas e nao possui olhos azuis
    if cabelos=="r" and olhos!="a":
        cont_ruivos+=1

#mostrar os dados
print(f"a)a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos:{pessoa_50a_menos60}")

media_idades=somar_idades/cont_alturas
print(f"b)a média das idades das pessoas com altura inferior a 1,50 metros: {media_idades}")
percertagem=(cont_olhos/tamanho)*100
print(f"c)a percentagem de pessoas com olhos azuis entre todas as pessoas analisadas {percertagem}")
print(f"d)a quantidade de pessoas ruivas e que não possuem olhos azuis: {cont_ruivos}")