class Usuario:
    def __init__(self, usuario, contraseña, nombre, curp, ciudad, rol='cliente'):
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad
        
    def __str__(self):
        return f'Usuario: {self.usuario}\nRol: {self.rol}\nNombre: {self.nombre}\nCURP: {self.curp}\nCiudad: {self.ciudad}'
        
    @staticmethod
    def registrar():
        usuario = input('Ingrese el usuario: ')
        contraseña = input('Ingrese la contraseña: ')
        nombre = input('Ingrese el nombre: ')
        curp = input('Ingrese el CURP: ')
        ciudad = input('Ingrese la ciudad: ')
        nuevo_usuario = Usuario(usuario, contraseña, nombre, curp, ciudad)
        if nuevo_usuario in usuarios_registrados:
            print('El usuario ya existe')
        else:
            usuarios_registrados.append(nuevo_usuario)
            print('Usuario registrado correctamente')
    
    @staticmethod
    def iniciar_sesion():
        usuario = input('Ingrese el usuario: ')
        contraseña = input('Ingrese la contraseña: ')
        for u in usuarios_registrados:
            if u.usuario == usuario and u.contraseña == contraseña:
                print(u)
                return
        print('Datos incorrectos')
        
usuarios_registrados = []
admin = Usuario('admin', 'admin123', 'Administrador', '0000000000000', 'Ciudad de México', 'administrador')

while True:
    print('MENU\n1.- Registro\n2.- Inicio de sesión\n3.- Salida')
    opcion = input('Seleccione una opción: ')
    if opcion == '1':
        Usuario.registrar()
    elif opcion == '2':
        Usuario.iniciar_sesion()
    elif opcion == '3':
        break
    elif admin.usuario == opcion and admin.contraseña == input('Ingrese la contraseña del administrador: '):
        for u in usuarios_registrados:
            print(u)
