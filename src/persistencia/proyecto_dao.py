from dominio.proyecto import Proyecto
from persistencia.conexion import abrir_conexion, marcador_sql, obtener_motor

class ProyectoDAO:

    @staticmethod
    def _fila_a_proyecto(fila):
        if fila is None:
            return None
        # Asumiendo estructura de tabla: id, nombre, descripcion, fechaInicio
        return Proyecto(id=fila[0], nombre=fila[1], descripcion=fila[2], fechaInicio=fila[3])

    @staticmethod
    def insertar(proyecto: Proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"INSERT INTO proyecto (nombre, descripcion, fechaInicio) VALUES ({marca}, {marca}, {marca})"
            cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fechaInicio))
            
            proyecto.id = cursor.lastrowid
            conexion.commit()
            return proyecto
        except Exception as e:
            print(f"Error al insertar proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_proyecto: int):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT id, nombre, descripcion, fechaInicio FROM proyecto WHERE id = {marca}"
            cursor.execute(sql, (id_proyecto,))
            fila = cursor.fetchone()
            return ProyectoDAO._fila_a_proyecto(fila)
        except Exception as e:
            print(f"Error al buscar proyecto: {e}")
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            sql = "SELECT id, nombre, descripcion, fechaInicio FROM proyecto"
            cursor.execute(sql)
            filas = cursor.fetchall()
            return [ProyectoDAO._fila_a_proyecto(f) for f in filas]
        except Exception as e:
            print(f"Error al listar proyectos: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(proyecto: Proyecto) -> bool:
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"UPDATE proyecto SET nombre = {marca}, descripcion = {marca}, fechaInicio = {marca} WHERE id = {marca}"
            cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fechaInicio, proyecto.id))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_proyecto: int) -> bool:
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM proyecto WHERE id = {marca}"
            cursor.execute(sql, (id_proyecto,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()