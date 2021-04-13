largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
#cada L de tinta pinta uma área de 2m2
print(f'Área da parede = {area}')
print(f'Serão nescessários ao menos {area/2:.4f} litros de tinta para pintar a parede completa.')