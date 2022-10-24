
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo    

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def catalogar(lista_vehiculos, ruedas = None):
    counter_vehiculos = 0
    for i, vehiculo in enumerate(lista_vehiculos):
        if ruedas != None:
            if vehiculo.ruedas == ruedas:
                counter_vehiculos += 1
                print('Vehiculo {} tipo: {}'.format(i+1, type(vehiculo).__name__))
                print('Atributos:')
                print(vehiculo.__dict__)
                print('Se ha(n) encontrado {} vehículo(s) con {} rueda(s)'.format(counter_vehiculos, ruedas))
        else:
            print('Vehiculo {} tipo: {}'.format(i+1, type(vehiculo).__name__))
            print('Atributos:')
            print(vehiculo.__dict__)   
 


vehiculos = []

vehiculo1 = Coche('Rojo', 4, 300, 100)
vehiculo2 = Camioneta('Verde', 6, 250, 150, 1000)
vehiculo3 = Bicicleta('Azul', 2, 'Deportiva')
vehiculo4 = Motocicleta('Negra', 2, 'Deportiva', 150, 120)

vehiculos.append(vehiculo1)
vehiculos.append(vehiculo2)
vehiculos.append(vehiculo3)
vehiculos.append(vehiculo4)

catalogar(vehiculos,6)

