from dominio.empleado import Empleado
from persistencia.conexion import abrir_conexion, marcador_sql
 
# Orden de columnas usado en todos los SELECT
COLUMNAS = "id, nombre, direccion, numeracion, telefono, correo, salario, inicioContrato"
 
 
def _fila_a_empleado(fila):
    """Convierte una fila de la BD en un objeto Empleado."""
    return Empleado(
        id=fila[0],
        nombre=fila[1],
        direccion=fila[2],
        numeracion=fila[3],
        telefono=fila[4],
        correo=fila[5],
        salario=fila[6],
        inicioContrato=fila[7],
    )
 
 
class EmpleadoDAO:
    """Acceso a datos de Empleado.
    Si ocurre un error, el método lo informa por pantalla y devuelve un valor
    seguro (None, False, [] o 0) en vez de dejar caer el programa."""
 
    # ===================== CRUD (los del profe) =====================
 
    @staticmethod
    def insertar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                INSERT INTO empleado
                    (nombre, direccion, telefono, correo, salario, inicioContrato)
                VALUES ({marca}, {marca}, {marca}, {marca}, {marca}, {marca})
            """
            cursor.execute(sql, (
                empleado.nombre,
                empleado.direccion,
                empleado.telefono,
                empleado.correo,
                empleado.salario,
                empleado.inicioContrato,
            ))
            empleado.id = cursor.lastrowid
            conexion.commit()
            return empleado
        except Exception as e:
            print(f"Error al insertar el empleado: {e}")
            if conexion is not None:
                conexion.rollback()
            return None
        finally:
            if conexion is not None:
                conexion.close()
 
    @staticmethod
    def actualizar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE empleado "
                f"SET nombre = {marca}, direccion = {marca}, "
                f"telefono = {marca}, correo = {marca}, salario = {marca}, "
                f"inicioContrato = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (
                empleado.nombre,
                empleado.direccion,
                empleado.telefono,
                empleado.correo,
                empleado.salario,
                empleado.inicioContrato,
                empleado.id,
            ))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar el empleado: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()
 
    @staticmethod
    def eliminar(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM empleado WHERE id = {marca}"
            cursor.execute(sql, (id_empleado,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar el empleado: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()
 
    # ===================== Métodos adicionales =====================
 
    @staticmethod
    def listar_todos():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute(f"SELECT {COLUMNAS} FROM empleado ORDER BY id")
            filas = cursor.fetchall()
            return [_fila_a_empleado(f) for f in filas]
        except Exception as e:
            print(f"Error al listar los empleados: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM empleado WHERE id = {marca}"
            cursor.execute(sql, (id_empleado,))
            fila = cursor.fetchone()
 
            if fila is None:
                return None
            return _fila_a_empleado(fila)
        except Exception as e:
            print(f"Error al buscar el empleado por id: {e}")
            return None
        finally:
            if conexion is not None:
                conexion.close()
 
    @staticmethod
    def buscar_por_nombre(nombre):
        """Búsqueda parcial: 'ana' encuentra 'Ana', 'Mariana', etc."""
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM empleado WHERE nombre LIKE {marca} ORDER BY nombre"
            # El comodín va en el parámetro, nunca concatenado en el SQL
            cursor.execute(sql, (f"%{nombre}%",))
            filas = cursor.fetchall()
            return [_fila_a_empleado(f) for f in filas]
        except Exception as e:
            print(f"Error al buscar empleados por nombre: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()
 
    @staticmethod
    def existe_correo(correo):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT 1 FROM empleado WHERE correo = {marca}"
            cursor.execute(sql, (correo,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al verificar el correo: {e}")
            return False
        finally:
            if conexion is not None:
                conexion.close()
 
    @staticmethod
    def listar_por_departamento(id_departamento):
        """Requiere la columna id_departamento en la tabla empleado (FK)."""
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM empleado WHERE id_departamento = {marca} ORDER BY nombre"
            cursor.execute(sql, (id_departamento,))
            filas = cursor.fetchall()
            return [_fila_a_empleado(f) for f in filas]
        except Exception as e:
            print(f"Error al listar empleados por departamento: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()
 
    @staticmethod
    def contar():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM empleado")
            return cursor.fetchone()[0]
        except Exception as e:
            print(f"Error al contar los empleados: {e}")
            return 0
        finally:
            if conexion is not None:
                conexion.close()