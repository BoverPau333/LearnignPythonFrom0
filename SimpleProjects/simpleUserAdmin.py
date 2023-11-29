import random

lower = "abcdefghijqlmnopqrstuwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
numbers = "1234567890"
simbols = "@#$€+-&[]{}()./;"

all = lower + upper + numbers + simbols
lenght = random.randint(16,20)

def generateRandomPassword():
    password = "".join(random.sample(all, lenght))
    print(password)
    return password

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def show(self):
        print("User: %s  Password: %s" % (self.name, self.password))


#Clase Contenerdora de Users 
class Usuarios:
    def __init__(self):
        # Inicializar parametros
        self.contador = 0  
        self.map = { self.contador:User("root","x")}

    def adduser(self,valor):
        # Agregar un elemento al map
        self.contador += 1
        self.map[self.contador] = valor

    def rmuser(self, clave):
        if clave == 0:
            print(f"No se pude eliminar el usuario {clave} o root")
        else:
            if clave in self.map:
                del self.map[clave]
                print(f"Elemento con clave {clave} eliminado.")
            else:
                print(f"No se encontró un elemento con clave {clave}.")

    def show(self):
        for user_id, user in self.map.items():
            print(f"ID: {user_id}", end= "  ")
            user.show()


def agregar_usuario(mapa):
    nombre = input("Introduce el nombre del usuario: ")
    entrada = input("Introduce 'True' o 'False', si quieres añdir tu propia contraseña o que el sistema elija una: ").strip().lower()
    if entrada == 'true':
        password = input("Introduce la contraseña del usuario: ")    
    elif entrada == 'false':
        password = generateRandomPassword()    
    else:
        raise ValueError("Entrada no válida. Introduce 'True' o 'False'.")
    usuario = User(nombre, password)
    mapa.adduser(usuario)

def quitar_usuario(mapa):
    mapa.show()
    num = input("Introduce el numero del usuario a eliminar: ")
    try:
        num = int(num)
    except ValueError:
        print("Por favor, introduce un número válido.")
        return
    mapa.rmuser(num)

def mostrar_mapa(mapa):
    mapa.show()

def mostrar_ayuda(mapa):
    print("Opciones:")
    print("a: Añadir usuario")
    print("r: Mostrar el mapa y quitar usuario")
    print("m: Mostrar solo el mapa")
    print("h: Mostrar ayuda")
    print("q: Salir")

if __name__ == "__main__":
    mi_mapa = Usuarios()

    opciones = {
        'a': agregar_usuario,
        'r': quitar_usuario,
        'm': mostrar_mapa,
        'h': mostrar_ayuda,
        'q': exit
    }

    mostrar_ayuda(mi_mapa)
    while True:
        opcion = input("Introduce la opción: ")

        if opcion in opciones:
            opciones[opcion](mi_mapa)
        else:
            print("Opción no válida. Inténtalo de nuevo.")