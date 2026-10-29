from dominio.empleado import Empleado
from persistencia.base_dao import BaseDAO
from persistencia.conexion import abrir_conexion

class EmpleadoDAO(BaseDAO):
    TABLA = "empleado"
    COLUMNAS = "id, nombre, direccion, telefono, correo, salario, inicioContrato, id_departamento"
    NOMBRE = "el empleado"

    @staticmethod
    def _convertir(fila):
        return Empleado(
            id=fila[0],
            nombre=fila[1],
            direccion=fila[2],
            telefono=fila[3],
            correo=fila[4],
            salario=fila[5],
            inicioContrato=fila[6],
            id_departamento=fila[7],
        )

    @classmethod
    def insertar(cls, empleado):
        conexion = abrir_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO empleado (nombre, correo, direccion, telefono, salario, inicioContrato)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
            empleado.nombre,
            empleado.direccion,
            empleado.telefono,
            empleado.correo,
            empleado.salario,
            empleado.inicioContrato,
            empleado.id_departamento,
        ))
        conexion.commit()            
            return cursor.lastrowid
    except Exception as e:
        print(f"Error al insertar el empleado: {e}")
        return None
    finally:
        conexion.close()

    @classmethod
    def actualizar(cls, empleado):
        sql = (
            "UPDATE empleado "
            "SET nombre = ?, direccion = ?, telefono = ?, correo = ?, salario = ?, "
            "inicioContrato = ?, id_departamento = ? "
            "WHERE id = ?"
        )
        parametros = (
            empleado.nombre,
            empleado.direccion,
            empleado.telefono,
            empleado.correo,
            empleado.salario,
            empleado.inicioContrato,
            empleado.id_departamento,
            empleado.id,
        )
        return cls._ejecutar(sql, parametros, "actualizar el empleado") > 0

    @classmethod
    def buscar_por_nombre(cls, nombre):
        buscadas = nombre.casefold().split()
        return [
            empleado for empleado in cls.listar_todos()
            if all(palabra in empleado.nombre.casefold().split() for palabra in buscadas)
        ]

    @classmethod
    def buscar_por_correo(cls, correo):
        conexion = abrir_conexion()
        with conexion.cursor() as cursor:
             sql = "SELECT * FROM empleados WHERE correo = %s"
             cursor.execute(sql, (correo,))
             return cursor.fetchone()

    @classmethod
    def listar_por_departamento(cls, id_departamento):
        return cls._listar_donde("id_departamento = ?", (id_departamento,),
                                 "listar los empleados del departamento", orden="nombre")

    @classmethod
    def asignar_departamento(cls, id_empleado, id_departamento):
        sql = "UPDATE empleado SET id_departamento = ? WHERE id = ?"
        return cls._ejecutar(sql, (id_departamento, id_empleado),
                             "asignar el departamento al empleado") > 0

    @classmethod
    def listar_por_proyecto(cls, id_proyecto):
        columnas = ", ".join(f"e.{c.strip()}" for c in cls.COLUMNAS.split(","))
        sql = (
            f"SELECT {columnas} FROM empleado e "
            "JOIN empleado_proyecto ep ON ep.id_empleado = e.id "
            "WHERE ep.id_proyecto = ? ORDER BY e.nombre"
        )
        filas = cls._consultar(sql, (id_proyecto,), "listar los empleados del proyecto")
        return [cls._convertir(fila) for fila in filas]
