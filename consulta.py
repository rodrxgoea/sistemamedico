class Consulta:
    def __init__(self, fecha, medico, motivo, nota):
        self._fecha = fecha
        self._medico = medico
        self._motivo = motivo
        self._nota = nota
    @property
    def fecha(self):
        return self._fecha
    @property
    def medico(self):
        return self._medico
    @property
    def motivo(self):
        return self._motivo
    @property
    def nota(self):
        return self._nota

    def resumen(self):
        return f"{self._fecha} | Dr. {self._medico.nombre} ({self._medico.especialidad}) | {self._motivo}: {self._nota}"