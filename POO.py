'''9.5 CARRERA
Desarrolle un programa que simule una carrera de 6 automóviles y el respectivo lugar de
llegada de cada auto se verá dado aleatoriamente. Cada automóvil posee por lo menos
dos características(atributos) que le permiten ser diferenciado con otros:
Marca del automóvil.
Conductor.
Al final el programa deberá ser capaz de imprimir en pantalla la lista de llegada de los
automóviles de forma ordenada.
'''

from Carro import *
from Car_Functions import *

lista_carros = []

while len(lista_carros) < 6:

    nombre = input(
        f'introduce el nombre del conductor del auto num:{len(lista_carros)+1} ==> ')

    marca = input(
        f'introduce la marca del auto num:{len(lista_carros)+1} ==> ')

    carro = Car(marca, nombre)
    random_position(lista_carros, carro)

    lista_carros.append(carro)

positions_in_order(lista_carros)

print_car_list(lista_carros)
