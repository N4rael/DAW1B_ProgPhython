monto_depositado = float(input("Introduce la cantidad de dinero depositada: "))

interes_anual = 0.04
saldo_despues_de_1_ano = monto_depositado * (1 + interes_anual)

saldo_despues_de_2_anos = saldo_despues_de_1_ano * (1 + interes_anual)


saldo_despues_de_3_anos = saldo_despues_de_2_anos * (1 + interes_anual)

print("Saldo después de 1 año: {:.2f}".format(saldo_despues_de_1_ano))
print("Saldo después de 2 años: {:.2f}".format(saldo_despues_de_2_anos))
print("Saldo después de 3 años: {:.2f}".format(saldo_despues_de_3_anos))
