
class persona:
    # metodo constructor
    def __init__ (self, nombre , apellidos , edad):
        self.nombre = nombre 
        self.apellidos = apellidos
        self.edad = edad 

    # metodo para mostrar los datos de una persona     
    def mostrarpersona(self):
        print("nombre: " + self.nombre)
        print("apellidos:" + self.apellidos)
        print("edad:" + str(self.edad))

# metodo principal
def main():
    p1 = persona("daniel", " diaz", 17)
    p1.mostrarpersona()
    p2 = persona("maias", "ortiz", 14 )
    p2.mostrarpersona()
    p1.edad = 20
    p1.mostrarpersona()
    p1 = p2
    p2.mostrarpersona()

if __name__ == "__main__":
    main()    



