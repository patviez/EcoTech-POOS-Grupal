import re
from datetime import datetime
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO
from dominio.empleado import Empleado

# ===================== Validaciones de entrada =====================

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede quedar vacío, intente de nuevo.")

def pedir_entero(mensaje, minimo=1):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
        except ValueError:
            print("Debe ingresar un número entero, intente de nuevo.")
            continue
        if numero < minimo:
            print(f"El número debe ser mayor o igual a {minimo}, intente de nuevo.")
            continue
        return numero

def pedir_telefono(mensaje):
    while True:
        telefono = input(mensaje).strip()
        if telefono.isdigit() and 8 <= len(telefono) <= 12:
            return int(telefono)
        print("El teléfono debe tener solo números (entre 8 y 12 dígitos), intente de nuevo.")

def pedir_correo(mensaje):
    while True:
        correo = input(mensaje).strip()
        if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
            return correo
        print("El correo no es válido (ejemplo: nombre@dominio.cl), intente de nuevo.")

def pedir_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            return fecha
        except ValueError:
            print("La fecha debe tener el formato DD-MM-AAAA (ejemplo: 15-03-2024), intente de nuevo.")

def pedir_departamento(mensaje):
    """Devuelve el id de un departamento existente, o None si se deja vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            return None
        if not valor.isdigit() or int(valor) < 1:
            print("El id del departamento debe ser un número entero positivo, intente de nuevo.")
            continue
        if DepartamentoDAO.buscar_por_id(int(valor)) is None:
            print("No existe un departamento con ese id, intente de nuevo.")
            continue
        return int(valor)

# ===================== Menú =====================

def ingresar_datos():
    nombre = pedir_texto("\nNombre: ")
    direccion = pedir_texto("Dirección: ")
    numeracion = pedir_entero("Numeración: ")
    telefono = pedir_telefono("Teléfono: ")
    correo = pedir_correo("Correo: ")
    salario = pedir_entero("Salario: ")
    inicioContrato = pedir_fecha("Inicio contrato (DD-MM-AAAA): ")
    id_departamento = pedir_departamento("Id del departamento (Enter para dejarlo sin departamento): ")
    return nombre, direccion, numeracion, telefono, correo, salario, inicioContrato, id_departamento

def gestionar_empleados():
    print("1. Registrar empleado")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Listar empleados")
    print("5. Listar empleados por departamento")
    print("6. Buscar empleado por id")
    print("7. Buscar empleado por nombre")
    print("8. Salir")

def registrar_empleado():
    nombre, direccion, numeracion, telefono, correo, salario, inicioContrato, id_departamento = ingresar_datos()

    empleado = Empleado(nombre, direccion, numeracion, telefono, correo, salario, inicioContrato, id_departamento)
    if EmpleadoDAO.insertar(empleado) is not None:
        print(empleado.mostrar_datos())
        print("\nEmpleado registrado correctamente.")
    else:
        print("\nNo fue posible registrar el empleado.")

def actualizar_empleado():
    idEmpleado = pedir_entero("Ingrese el id del empleado que desea actualizar: ")
    actual = EmpleadoDAO.buscar_por_id(idEmpleado)
    if actual is None:
        print("\nNo existe un empleado con ese id")
        return

    print("\nDatos actuales:")
    print(actual.agregar_descripcion())
    nombre, direccion, numeracion, telefono, correo, salario, inicioContrato, id_departamento = ingresar_datos()

    empleado = Empleado(nombre, direccion, numeracion, telefono, correo, salario, inicioContrato, id_departamento, idEmpleado)

    if EmpleadoDAO.actualizar(empleado):
        print(empleado.mostrar_datos())
        print("\nEmpleado actualizado correctamente")
    else:
        print("\nNo fue posible actualizar al empleado")

def eliminar_empleado():
    idEmpleado = pedir_entero("Ingrese el id del empleado que desea eliminar: ")
    if EmpleadoDAO.buscar_por_id(idEmpleado) is None:
        print("\nNo existe un empleado con ese id")
        return

    if EmpleadoDAO.eliminar(idEmpleado):
        print("\nEmpleado eliminado correctamente")
    else:
        print("\nNo fue posible eliminar al empleado")

def mostrar_lista(empleados):
    if not empleados:
        print("\nNo se encontraron empleados.")
        return
    for empleado in empleados:
        print(empleado.mostrar_datos())

def listar_empleados():
    mostrar_lista(EmpleadoDAO.listar_todos())

def listar_empleados_por_departamento():
    idDepartamento = pedir_entero("Ingrese el id del departamento: ")
    mostrar_lista(EmpleadoDAO.listar_por_departamento(idDepartamento))

def buscar_empleado_por_id():
    idEmpleado = pedir_entero("Ingrese el id del empleado que desea buscar: ")

    empleado = EmpleadoDAO.buscar_por_id(idEmpleado)
    if empleado is not None:
        print("\n" + empleado.agregar_descripcion())
    else:
        print("\nNo se encontró un empleado con ese id")

def buscar_empleado_por_nombre():
    nombre = pedir_texto("Ingrese el nombre del empleado que desea buscar: ")
    mostrar_lista(EmpleadoDAO.buscar_por_nombre(nombre))
