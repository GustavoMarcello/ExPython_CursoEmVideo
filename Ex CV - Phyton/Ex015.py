km = float(input('Digite a qtde de Km percorridos: '))
dias = int(input('Digite a quantidade de dias alugados: '))
total = ((dias * 60) + (km * 0.15))
print(f'Total a pagar pelo carro: {total} reais')