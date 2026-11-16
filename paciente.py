class Paciente:
    def __init__(self,codigo,nombre,edad):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = edad
        self._historial = []
    #Getters  @property es para no llamar los parentesis() en return
    @property
    def codigo(self):
        return self._codigo
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @property
    def historial(self):
        return list(self._historial)
    #Setters
    @codigo.setter
    def codigo(self,valor):
        self._codigo = valor
    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor
    @edad.setter
    def edad(self, valor):
        self._edad = valor

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._edad} años"
    def agregar_consulta(self, consulta):
        self._historial.append(consulta)

    def mostrar_historial(self):
        if not self._historial:
            return "Sin consultas registradas"
        return "\n".join(c.resumen() for c in self._historial)
    
        