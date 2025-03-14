# composicion

"""una cordenada en dos dimenciones esta compuesta por dos valores, el valor del eje x y el valor de las y, esto podria ser una calase un cuadro esta compuesto por coordenadas que son los cuatro vertices, esto  podria ser que una clase esta compuesta por cuatro clases del objeto cordenada."""


# clase coordenada 
class Coordenada: 
    #metodo constructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y 

    # metodo par mostrar cordenada
    def mostrarCoordenada(self):
        print("(",self.X,",", self.Y, ")")

# clase cuadrado 

class cuadrado: 

    # metodo constructor 
    def __init__(self,v1,v2,v3,v4):
        self.V1 = v1 
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # metodo para mostrar los vertices
    def mostrarvertices(self):
        print("elcuadro esta compuesto por los siguientes vertices: ")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()

# Metodo principal 
def main():
    #input
    x1 = int(input("digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    #processing
    c1 = Coordenada(x1,x2)
    c1.mostrarCoordenada()
    
    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarvertices()
if __name__ == "__main__":
    main()





                         

