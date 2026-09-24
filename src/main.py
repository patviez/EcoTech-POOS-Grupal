import sys
import os

# Configurar rutas para que Python reconozca 'dominio' y 'persistencia'
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
    # 1. Crear las tablas en MySQL si no existen
    crear_tablas()

    # 2. Instanciar empleado (usa los atributos que definió tu compañero)
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

    # 3. Paso 5 de la clase: Mostrar ID antes de guardar (debe ser None)
    print("Antes:", empleado.id)

    # 4. Guardar en la base de datos a través del DAO
    EmpleadoDAO.insertar(empleado)

    # 5. Paso 5 de la clase: Mostrar ID asignado por la BD
    print("Después:", empleado.id)

if __name__ == "__main__":
    probar_demostrasion()