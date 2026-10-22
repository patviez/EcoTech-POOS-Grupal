from persistencia.empleado_dao import EmpleadoDAO
from persistencia.usuario_dao import UsuarioDAO
from dominio.empleado import Empleado
from servicios.autenticacion import registrar_usuario

def sembrar_datos_iniciales():
    correo_admin = "admin@ecotech.cl"
    
    # 1. Buscar o crear Empleado Admin
    empleado = EmpleadoDAO.buscar_por_correo(correo_admin)
    if empleado is None:
        emp_id = EmpleadoDAO.insertar(Empleado(nombre="Admin General", correo=correo_admin))
    else:
        emp_id = empleado.id

    # 2. Buscar o crear Cuenta Admin
    usuario = UsuarioDAO.buscar_por_nombre("admin")
    if usuario is None:
        registrar_usuario(empleado_id=emp_id, nombre="admin", clave="Admin123!")
        print("Semilla ejecutada: Cuenta admin creada exitosamente.")
    else:
        print("Semilla verificada: La cuenta admin ya existe.")

if __name__ == "__main__":
    sembrar_datos_iniciales()