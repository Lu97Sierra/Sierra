class Usuario:
    def __init__(self, usuario, contrasena, rol, nombre, curp, ciudad):
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad

class Menu:
    def __init__(self):
        self.usuarios = []
        self.usuario_actual = None
        self.rol_administrador = "administrador"

    def registrar_usuario(self):
        print("Registro de nuevo usuario:")
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        nombre = input("Nombre: ")
        curp = input("CURP: ")
        ciudad = input("Ciudad: ")

        # Verificar que la CURP no se repita
        if any(usuario.curp == curp for usuario in self.usuarios):
            print("Error: La CURP ya está registrada")
        else:
            # Crear nuevo usuario y añadirlo a la lista
            nuevo_usuario = Usuario(usuario, contrasena, "usuario", nombre, curp, ciudad)
            self.usuarios.append(nuevo_usuario)
            print("Usuario registrado correctamente")

    def iniciar_sesion(self):
        print("Inicio de sesión:")
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        # Buscar usuario en la lista
        for usuario in self.usuarios:
            if usuario.usuario == usuario and usuario.contrasena == contrasena:
                self.usuario_actual = usuario
                print("Sesión iniciada correctamente")
                return

        print("Error: Usuario o contraseña incorrectos")

    def mostrar_usuarios(self):
        if self.usuario_actual and self.usuario_actual.rol == self.rol_administrador:
            print("Lista de usuarios registrados:")
            for usuario in self.usuarios:
                print(usuario.__dict__)
        else:
            print("Error: Acceso denegado")

    def ejecutar(self):
        while True:
            print("\nMenú:")
            print("1. Registro")
            print("2. Inicio de sesión")
            print("3. Salida")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                print("Hasta luego")
                break
            else:
                print("Opción no válida")

menu = Menu()
menu.ejecutar()
