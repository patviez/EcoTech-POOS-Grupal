from dominio.usuario import Usuario
from persistencia.conexion import abrir_conexion, marcador_sql

class UsuarioDAO:

    @staticmethod
    def _fila_a_usuario(fila):
        if fila is None:
            return None
        return Usuario(id=fila[0], username=fila[1], password=fila[2])

    @staticmethod
    def insertar(usuario: Usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"INSERT INTO usuario (username, password) VALUES ({marca}, {marca})"
            cursor.execute(sql, (usuario.username, usuario.password))
            usuario.id = cursor.lastrowid
            conexion.commit()
            return usuario
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            if conexion is not None:
                conexion.rollback()
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_username(username: str):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT id, username, password FROM usuario WHERE username = {marca}"
            cursor.execute(sql, (username,))
            fila = cursor.fetchone()
            return UsuarioDAO._fila_a_usuario(fila)
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_usuario: int) -> bool:
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM usuario WHERE id = {marca}"
            cursor.execute(sql, (id_usuario,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()