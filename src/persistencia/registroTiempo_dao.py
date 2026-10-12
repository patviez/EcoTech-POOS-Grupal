from dominio.registroTiempo import RegistroTiempo
from persistencia.conexion import abrir_conexion, marcador_sql

class RegistroTiempoDAO:

    @staticmethod
    def _fila_a_registro(fila):
        if fila is None:
            return None
        # Estructura: id, fecha, horas (y opcionalmente id_empleado / id_proyecto según tu BD)
        reg = RegistroTiempo(fecha=fila[1], horas=fila[2])
        reg.id = fila[0]
        return reg

    @staticmethod
    def insertar(registro: RegistroTiempo):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"INSERT INTO registro_tiempo (fecha, horas) VALUES ({marca}, {marca})"
            cursor.execute(sql, (registro.fecha, registro.horas))
            registro.id = cursor.lastrowid
            conexion.commit()
            return registro
        except Exception as e:
            print(f"Error al insertar registro de tiempo: {e}")
            if conexion is not None:
                conexion.rollback()
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
            sql = "SELECT id, fecha, horas FROM registro_tiempo"
            cursor.execute(sql)
            filas = cursor.fetchall()
            return [RegistroTiempoDAO._fila_a_registro(f) for f in filas]
        except Exception as e:
            print(f"Error al listar registros de tiempo: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_registro: int) -> bool:
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM registro_tiempo WHERE id = {marca}"
            cursor.execute(sql, (id_registro,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar registro de tiempo: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()