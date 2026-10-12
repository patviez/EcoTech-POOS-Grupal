from dominio.departamento import Departamento
from persistencia.conexion import abrir_conexion, marcador_sql

# Orden de columnas usado en todos los SELECT
COLUMNAS = "id, nombre, id_gerente"


def _fila_a_departamento(fila):
    """Convierte una fila de la BD en un objeto Departamento."""
    return Departamento(
        id=fila[0],
        nombre=fila[1],
        id_gerente=fila[2],
    )


class DepartamentoDAO:
    """Acceso a datos de Departamento.
    Si ocurre un error, el método lo informa por pantalla y devuelve un valor
    seguro (None, False o []) en vez de dejar caer el programa."""

    @staticmethod
    def insertar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"INSERT INTO departamento (nombre, id_gerente) VALUES ({marca}, {marca})"
            cursor.execute(sql, (departamento.nombre, departamento.id_gerente))
            departamento.id = cursor.lastrowid
            conexion.commit()
            return departamento
        except Exception as e:
            print(f"Error al insertar el departamento: {e}")
            if conexion is not None:
                conexion.rollback()
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM departamento WHERE id = {marca}"
            cursor.execute(sql, (id_departamento,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar el departamento: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM departamento WHERE id = {marca}"
            cursor.execute(sql, (id_departamento,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return _fila_a_departamento(fila)
        except Exception as e:
            print(f"Error al buscar el departamento por id: {e}")
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"UPDATE departamento SET nombre = {marca}, id_gerente = {marca} WHERE id = {marca}"
            cursor.execute(sql, (departamento.nombre, departamento.id_gerente, departamento.id))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar el departamento: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()