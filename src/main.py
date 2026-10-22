from menus.menuUsuario import solicitar_login, menu_privado
from persistencia.crear_bd import crear_tablas
from semilla_bd import sembrar_datos_iniciales

def main():    
    crear_tablas()
    sembrar_datos_iniciales()

    while True:
        print("\n=== INICIO DE SESIÓN ECOTECH ===")
        usuario_actual = solicitar_login()
        
        if usuario_actual is None:
            if input("Presione Enter para reintentar o '0' para salir: ").strip() == "0":
                return
            continue
            
        opcion = menu_privado(usuario_actual)
        usuario_actual = None
        
        if opcion == "0":
            print("Saliendo del programa...")
            return
            
        print("Sesión cerrada. Ingrese nuevamente.")

if __name__ == "__main__":
    main()
