
parcelas=6
debito=250
for parcelas in range(18) :
    print(f"Valor devido na parcela {parcelas}:{debito}")
    if debito>500:
        break
    debito=debito*1.1
