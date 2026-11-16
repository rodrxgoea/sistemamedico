from consulta import Consulta
class Cita:
    def __init__(self,codigo,paciente,medico,fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._estado = "programada"
    @property
    def codigo(self):
        return self._codigo
    @property
    def paciente(self):
        return self._paciente
    @property
    def medico(self):
        return self._medico
    @property
    def fecha(self):
        return self._fecha
    @property
    def estado(self):
        return self._estado

    @codigo.setter
    def codigo(self,valor):
        self._codigo=valor
    @paciente.setter
    def paciente(self,valor):
        self._paciente=valor
    @medico.setter
    def medico(self,valor):
        self._medico=valor
    @fecha.setter
    def fecha(self,valor):
        self._fecha=valor

    def resumen(self):
        return f"{self._codigo}-{self._paciente.nombre} con el Dr. {self._medico.nombre} el {self._fecha}"
    def atender(self, motivo="Control", nota="Sin novedades"):
        if self._estado != "programada":
             raise ValueError(f"No se puede atender una cita {self._estado}")
        self._estado = "atendida"
        consulta = Consulta(self._fecha, self._medico, motivo, nota)
        self._paciente.agregar_consulta(consulta)
    def cancelar(self):
        if self._estado != "programada":
            raise ValueError(f"No se puede cancelar una cita {self._estado}")
        self._estado = "cancelada"