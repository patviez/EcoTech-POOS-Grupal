from persistencia.conexion import (abrir_conexion,obtener_motor )

def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    if obtener_motor() == "sqlite":
        sentencias = [
            """CREATE TABLE IF NOT EXISTS departamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                id_gerente INTEGER,
                FOREIGN KEY (id_gerente) REFERENCES empleado(id)
            )""",
            """CREATE TABLE IF NOT EXISTS empleado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_departamento INTEGER,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                numeracion INTEGER NOT NULL,
                telefono TEXT NOT NULL,
                correo TEXT NOT NULL,
                salario INTEGER NOT NULL,
                inicioContrato TEXT NOT NULL,
                FOREIGN KEY (id_departamento) REFERENCES departamento(id)
            )""",
        ]
    else:
        sentencias = [
            """CREATE TABLE IF NOT EXISTS departamento (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                id_gerente INT
            )""",
            """CREATE TABLE IF NOT EXISTS empleado (
                id INT PRIMARY KEY AUTO_INCREMENT,
                id_departamento INT,
                nombre VARCHAR(100) NOT NULL,
                direccion VARCHAR(100) NOT NULL,
                numeracion INT NOT NULL,
                telefono VARCHAR(20) NOT NULL,
                correo VARCHAR(150) NOT NULL,
                salario INT NOT NULL,
                inicioContrato VARCHAR(150) NOT NULL,
                FOREIGN KEY (id_departamento) REFERENCES departamento(id)
            )""",
            """ALTER TABLE departamento
            ADD CONSTRAINT fk_gerente
            FOREIGN KEY (id_gerente) REFERENCES empleado(id)""",
            """CREATE TABLE IF NOT EXISTS registroTiempo (
                id INT PRIMARY KEY AUTO_INCREMENT,
                id_empleado INT,
                fecha VARCHAR(150) NOT NULL,
                horasTrabajadas INT NOT NULL,
                FOREIGN KEY (id_empleado) REFERENCES empleado(id)
            )""",
            """CREATE TABLE IF NOT EXISTS proyecto (
                id INT PRIMARY KEY AUTO_INCREMENT,
                id_registroTiempo INT,
                nombre VARCHAR(100) NOT NULL,
                descripcion VARCHAR(300) NOT NULL,
                fechaInicio VARCHAR(150) NOT NULL,
                FOREIGN KEY (id_registroTiempo) REFERENCES registroTiempo(id)
            )""",
            """CREATE TABLE IF NOT EXISTS usuario (
                id INT PRIMARY KEY AUTO_INCREMENT,
                id_empleado INT,
                nombre VARCHAR(100) NOT NULL,
                contraseña VARCHAR(100) NOT NULL,
                rol VARCHAR (100) NOT NULL,
                FOREIGN KEY (id_empleado) REFERENCES empleado(id)
            )""",
        ]

    for sql in sentencias:
        cursor.execute(sql)
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()