from dominio.registroTiempo import RegistroTiempo
from dominio.proyecto import Proyecto
 
class Empleado:
    def __init__(self, nombre: str, direccion: str, telefono: int, correo: str, salario: int, inicioContrato: str,  id = None):
        self.id = id,
        self.nombre = nombre,
        self.direccion = direccion,
        self.telefono = telefono,
        self.correo = correo,
        self.salario = salario,
        self.inicioContrato = inicioContrato
        self._registro_tiempo:list[RegistroTiempo] = []
        self._proyectos: list[Proyecto] = []
        self._departamentos: list = []

    def mostrar_datos(self) -> str:
        print(f"\nId {self.id}, Nombre {self.nombre}, Correo {self.correo}")

    def actualizar_nombre(self, nombre):
         self.nombre = nombre

    def registrar_tiempo(self, rg:RegistroTiempo) -> bool:
        if rg in self._registro_tiempo:
            return False
        self._registro_tiempo.append(rg)
        return True

    def agregar_descripcion(self) -> str:
        return (f"Empleado {self.nombre} (ID {self.id}) - {self.correo}\n"
                f"Dirección: {self.direccion} | Salario: {self.salario}")

    def crear_proyecto(self, nombre: str, descripcion: str, fecha_inicio: str) -> Proyecto:
        proyecto = Proyecto(nombre, descripcion, fecha_inicio)
        proyecto.asignar_empleado(self)
        self._proyectos.append(proyecto)
        return proyecto

    def editar_proyecto(self, proyecto: Proyecto, **cambios) -> bool:
        if proyecto not in self._proyectos:
            return False
        for atributo, valor in cambios.items():
            if hasattr(proyecto, atributo):
                setattr(proyecto, atributo, valor)
        return True

    def eliminar_proyecto(self, proyecto: Proyecto) -> bool:
        if proyecto not in self._proyectos:

            return False
        proyecto.eliminar_empleado(self)
        self._proyectos.remove(proyecto)
        return True

    def crear_departamento(self, nombre: str, gerente_asociado: str):
        from dominio.departamento import Departamento  
        departamento = Departamento(nombre, gerente_asociado)
        departamento.agregar_empleado(self)
        self._departamentos.append(departamento)
        return departamento

    def eliminar_departamento(self, departamento) -> bool:
        if departamento not in self._departamentos:
            return False
        self._departamentos.remove(departamento)
        return True



        