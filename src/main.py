import sys
import os

directorio_src = os.path.dirname(os.path.abspath(__file__))
if directorio_src not in sys.path:
    sys.path.insert(0, directorio_src)

from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.departamento import Departamento
from dominio.registroTiempo import RegistroTiempo
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO

def probar_demostrasion():
    
    crear_tablas()
    
    empleado = Empleado(
        nombre="Ana Pérez",
        correo="ana@ecotech.cl",
        direccion="Av. Providencia",
        numeracion=1234,
        numero=5678,
        salario=1200000.0,
        inicioContrato="2024-01-15",
        cargo="Analista QA"
    )

    # Mostrar ID antes de guardar (debe ser None)
    print("Antes:", empleado.id)

    # Guardar en la base de datos a través del DAO
    EmpleadoDAO.insertar(empleado)

    # Mostrar ID asignado por la BD
    print("Después:", empleado.id)

if __name__ == "__main__":
    probar_demostrasion()