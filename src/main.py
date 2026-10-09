from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.departamento import Departamento
from dominio.registroTiempo import RegistroTiempo
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.crear_bd import crear_tablas
from menus.menuEmpleado import *
from menus.menuPrincipal import menu

def main():
    menu()

    while True:
        seleccion = input("\n¿Qué quieres hacer?: ")

        if seleccion == "1":
            gestionar_empleados()

            while True:
                opcion = input("\nSeleccione una opción: ")

                if opcion == "1":
                    registrar_empleado()

                elif opcion == "2":
                    actualizar_empleado()

                elif opcion == "3":
                    eliminar_empleado()

                elif opcion == "6":
                    print("Hasta luego!")
                    break
            
                else:
                    print("\nSeleccione una opción válida")

        elif seleccion == "6":
            print("Hasta luego!")
            break
        
        else:
            print("\nSeleccione una opción válida")
            

if __name__ == "__main__":
    crear_tablas()
    print("Base de datos preparada correctamente.")
    main()