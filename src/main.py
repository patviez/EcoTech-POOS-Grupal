from persistencia.crear_bd import crear_tablas
from menus.menuPrincipal import menu
from menus.menuEmpleado import (
    gestionar_empleados, registrar_empleado, actualizar_empleado, eliminar_empleado,
    listar_empleados, listar_empleados_por_departamento,
    buscar_empleado_por_id, buscar_empleado_por_nombre,
)
from menus.menuDepartamento import (
    gestionar_departamentos, crear_departamento, eliminar_departamento,
    agregar_empleado_departamento, quitar_empleado_departamento,
    listar_empleados_departamento, ver_cantidad_empleados, editar_departamento,
)

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

                elif opcion == "4":
                    listar_empleados()

                elif opcion == "5":
                    listar_empleados_por_departamento()

                elif opcion == "6":
                    buscar_empleado_por_id()

                elif opcion == "7":
                    buscar_empleado_por_nombre()

                elif opcion == "8":
                    print("Hasta luego!")
                    break

                else:
                    print("\nSeleccione una opción válida")

        elif seleccion == "2":
            gestionar_departamentos()

            while True:
                opcion = input("\nSeleccione una opción: ")

                if opcion == "1":
                    crear_departamento()

                elif opcion == "2":
                    eliminar_departamento()

                elif opcion == "3":
                    agregar_empleado_departamento()

                elif opcion == "4":
                    quitar_empleado_departamento()

                elif opcion == "5":
                    listar_empleados_departamento()

                elif opcion == "6":
                    ver_cantidad_empleados()

                elif opcion == "7":
                    editar_departamento()

                elif opcion == "8":
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
