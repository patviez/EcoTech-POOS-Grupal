class Usuario:
    def __init__(self, nombre: str, contraseña: str, rol: str, correo: str = "", id: int = None):
        self._id = id
        self.nombre = nombre
        self._correo = correo
        self.contraseña = None
        self.rol = rol
        self._registrado = False
        self._establecer_contraseña(contraseña)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        self._correo = value

    def _establecer_contraseña(self, contraseña: str) -> None:
        from dominio.controlAcceso import ControlAcceso
        if not contraseña or len(contraseña) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        self.contraseña = ControlAcceso.cifrar_contraseña(contraseña)

    def registrar(self) -> bool:
        if not self.nombre or not self.contraseña or not self.rol:
            return False
        self._registrado = True
        return True

    def iniciar_sesion(self, contraseña_ingresada: str) -> bool:
        from dominio.controlAcceso import ControlAcceso
        if not self._registrado:
            return False
        return ControlAcceso.validar_credenciales(self, contraseña_ingresada)