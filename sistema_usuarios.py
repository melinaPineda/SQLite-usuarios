import sqlite3

def crear_tabla():
    #se conecta a la base (y si no existe, se crearía sola)
    conexion = sqlite3.connect("colectivo.db")
    cursor = conexion.cursor()

    # acá se crea la tabla donde se van a guardar los usuarios
    # y cada campo tiene su tipo (por si se ingresa valor de texto o d num)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            dni TEXT UNIQUE NOT NULL,
            edad INTEGER NOT NULL
        )
    """)

    conexion.commit()  # guardalos cambios
    conexion.close()   # cierra la conexión


# crear un usuario nuevo
def crear_usuario(nombre, apellido, dni, edad):
    conexion = sqlite3.connect("colectivo.db")
    cursor = conexion.cursor()

    # se meten datos que pasan por los parámetros (son segun cda atributo)
    cursor.execute(
        "INSERT INTO usuarios (nombre, apellido, dni, edad) VALUES (?, ?, ?, ?)",
        (nombre, apellido, dni, edad)
    )

    conexion.commit()
    conexion.close()


# muestra todos los usuarios
def leer_usuarios():
    conexion = sqlite3.connect("colectivo.db")
    cursor = conexion.cursor()

    #acá pide todos los registros de la tabla para dps mostrarlos
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()  #devuelve una lista con todos

    conexion.close()
    return usuarios


#actualizar datos de un usuario
def actualizar_usuario(id_usuario, nuevo_nombre, nuevo_apellido, nuevo_dni, nueva_edad):
    conexion = sqlite3.connect("colectivo.db")
    cursor = conexion.cursor()

    #aca c cambian los datos del usuario que tenga ese ID
    cursor.execute("""
        UPDATE usuarios
        SET nombre=?, apellido=?, dni=?, edad=?
        WHERE id=?
    """, (nuevo_nombre, nuevo_apellido, nuevo_dni, nueva_edad, id_usuario))

    conexion.commit()
    conexion.close()


# borrar un usuario según su ID
def eliminar_usuario(id_usuario):
    conexion = sqlite3.connect("colectivo.db")
    cursor = conexion.cursor()

    #elimina el registro que coincida con ese ID
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))

    conexion.commit()
    conexion.close()


def menu():
    crear_tabla()  #por si la tabla no existe todavía

    while True:
        print("\n--- SISTEMA DE USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Ver usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            # pido los datos y los guardo
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            edad = int(input("Edad: "))
            crear_usuario(nombre, apellido, dni, edad)

        elif opcion == "2":
            # muestro todos los usuarios
            usuarios = leer_usuarios()
            for u in usuarios:
                print(u)

        elif opcion == "3":
            # actualizo según ID
            id_u = int(input("ID del usuario a actualizar: "))
            n = input("Nuevo nombre: ")
            a = input("Nuevo apellido: ")
            d = input("Nuevo DNI: ")
            e = int(input("Nueva edad: "))
            actualizar_usuario(id_u, n, a, d, e)

        elif opcion == "4":
            # borro por ID
            borrar = int(input("ID del usuario a eliminar: "))
            eliminar_usuario(borrar)

        elif opcion == "5":
            break #bai
        else:
            print("Ese no ta")


menu()
