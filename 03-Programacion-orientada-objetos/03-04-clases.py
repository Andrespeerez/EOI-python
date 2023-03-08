from datetime import datetime

#############################
# clases

class Alumno:
    """"Comentario de uso de la clase"""
    # variables o propiedades de la clase
    nombre = None
    apellido1 = None
    apellido2 = None
    fechaDeNacimiento = None

    # Funcion constructora : se usa cuando se instancia el objeto
    def __init__(self, nombre, apellido1, apellido2 = None) -> None:
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
    
    # Otras funciones del objeto
    def getNombreCompleto(self) -> str:
        return f"{self.nombre} {self.apellido1} {self.apellido2}"

    def setFechaDeNacimiento(self, fecha) -> bool:
        try:
            if(len(fecha) == 10):
                self.fechaDeNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            else:
                self.fechaDeNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()

            return True
        except:
            return False

    def getEdad(self) -> int:
        if(self.fechaDeNacimiento == None):
            return -1
        else:
            return datetime.now().year - self.fechaDeNacimiento.year

# creamos un objeto y llamamos a su constructor:
Alu1 = Alumno("Andres", "Perez", "Guardiola")
print(Alu1.setFechaDeNacimiento("03-09-93"))
print(Alu1.fechaDeNacimiento)

print(f"Me llamo {Alu1.getNombreCompleto()}")
