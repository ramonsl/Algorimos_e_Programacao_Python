#digita ida
# 
# 
# 
# for
#for 
#for i in range(10):

#for i  in range(5):
i=0
while i < 5 :
    idade=int(input("Digite a sua idade"))
    if i==0:
        menor_idade_sistema=idade
        maior_idade_sistema=idade
    if menor_idade_sistema  > idade :
            menor_idade_sistema=idade
    if maior_idade_sistema< idade:
            maior_idade_sistema=idade
    i=i+1

print(f"A menor idade é {menor_idade_sistema} ")
print(f"A maior idade é {maior_idade_sistema} ")