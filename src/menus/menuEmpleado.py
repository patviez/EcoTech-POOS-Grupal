from persistencia.empleado_dao import EmpleadoDAO
from dominio.empleado import Empleado

def ingresar_datos():
    nombre = input("\nNombre: ").strip()
    direccion = input("Dirección: ").strip()
    telefono = int(input("Teléfono: "))
    correo = input("Correo: ").strip()
    salario = float(input("Salario: "))
    inicioContrato = input("Inicio contrato: ").strip()
    return nombre, direccion, telefono, correo, salario, inicioContrato

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
    nombre, direccion, telefono, correo, salario, inicioContrato = ingresar_datos()

    empleado = Empleado(nombre, direccion, telefono, correo, salario, inicioContrato)
    print(empleado.mostrar_datos())
    try:
        EmpleadoDAO.insertar(empleado)
        print("\nEmpleado registrado correctamente.")

    except Exception:
        print("\nNo fue posible registrar el empleado.")

def actualizar_empleado():
    idEmpleado = input("Ingrese el id del empleado que desea actualizar: ")
    nombre, direccion, telefono, correo, salario, inicioContrato = ingresar_datos()

    empleado = Empleado(nombre, direccion, telefono, correo, salario, inicioContrato)
    empleado.id = idEmpleado
    print(empleado.mostrar_datos())

    try:
        EmpleadoDAO.actualizar(empleado)
        print("\nEmpleado actualizado correctamente")
    
    except Exception:
        print("\nNo fue posible eliminar al empleado")

def eliminar_empleado():
    idEmpleado = input("Ingrese el id del empleado que desea eliminar: ")

    try:
        EmpleadoDAO.eliminar(idEmpleado)
        print("Empleado eliminado correctamente")
    
    except Exception:
        print("\nNo fue posible eliminar al empleado")