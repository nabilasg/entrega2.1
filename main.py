# noinspection PyArgumentList
class Forma:
    pass

    def __init__(self, nombre, color, coordenadas):
        self.nombre = nombre
        self.color = color
        self.coordenadas = Forma(coordenadas)
        self.coordenadas.x = coordenadas.x
        self.coordenadas.y = coordenadas.y

    def imprimir(self):
        """Imprime el nombre y el color de la figura por pantalla."""

        print(f"el nombre de la figura es str{self.nombre} y es de color str{self.color} con las cordenadas {Forma}")

    def cambiar(self, nuevoColor):
        """obtiene el color y lo modifica """
        color = nuevoColor
        nuevoColor = str(input("introduzca un color: "))
        print(f"el nuevo color es str{self.color}")

    def mover(self, coordenadas):
        int = coordenadas.x == 0
        int = coordenadas.y == 0
        print(f"las nuevas coordenadas son {coordenadas.x} y {coordenadas.y}")

        self.imprimir()
        self.cambiar()
        self.mover()

    class Rectangulo(Forma):
        pass

        def __init__(self, ladoMayor, ladoMenor):
            self.ladoMayor = ladoMayor
            self.ladoMenor = ladoMenor

        def imprimirRectangulo(self):
            nombre = self.nombre
            color = self.color
            centro = self.centro
            lado = self.lado
            print(
                f"el nombre de la figura es str{self.nombre} y es de color str{self.color},el centro {self.centro} y el lado {self.lado}")

        @staticmethod
        def multiplicacion(ladoMayor, ladoMenor):
            print(f"la multiplicacion de los dos lados es {ladoMenor * ladoMayor}")

        def calcularPerimetro(self, ladoMenor, ladoMayor):
            print(f"la multiplicacion de los dos lados es {(2 * ladoMenor) + (2 * ladoMayor)}")

            self.imprimirRectangulo()
            self.multiplicacion(ladoMayor, ladoMenor)
            self.calcularPerimetro(ladoMenor, ladoMayor)


# definimos la clase Eclipe

class Elipse(Forma):
    pass

    def __init__(self, radioMayor, radioMenor, nombre, color, coordenadas):
        super().__init__(nombre, color, coordenadas)

        self.radioMayor = radioMayor
        self.radioMenor = radioMenor

        def area():
            print(f"el area del elipse es igual a {3.14 * (radioMayor * radioMenor)}")

        self.area()


# definimos la clase Circulo
class Circulo(Elipse):
    pass

    def __init__(self , radio, radioMayor, radioMenor):
        super().__init__(self , radioMayor, radioMenor)
        self.radio=radio
        #no sé porqué me da error aquí

    def areaCirculo(self):
        print(f"el area del elipse es igual a {3.14 * (self.radio * self.radio)}")


    def imprimirCirculo(self):
        print(f"el radio es {self.radio}")

    areaCirculo()
    imprimirCirculo()

#definimos la clase cuadrado

class Cuadrado(Forma):    #acá cuando pongo que la clase Cuadrado es derivada de Rectangulo me da error y cuando pongo otro me dice que está bien asi que lo que hice es poner los atributos que necesitamos de rectangulo en la de Cuadrado
    pass
    def __init__(self, ladoMenor,ladoMayor=int):
        super().__init__(self, ladoMayor,ladoMenor)

    def area(self):
        print(f"el area del cuadrado igual a {self.ladoMenor * self.ladoMayor}")


    def imprimirCuadrado(self):
        print(f"el area del cuadrado igual a {self.ladoMenor * self.ladoMayor}")











