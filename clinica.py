from datetime import datetime
from paciente import Paciente
from medico import Medico
from cita import Cita

class Clinica:
    def __init__(self, nombre):
        self._nombre = nombre
        self._pacientes = []
        self._citas = []
        self._contador_pacientes = 0
        self._contador_citas = 0
        # Los 5 doctores fijos, uno por especialidad
        self._medicos = [
            Medico("M001", "Oscar", "Cardiologia"),
            Medico("M002", "Lucia", "Pediatria"),
            Medico("M003", "Carlos", "Dermatologia"),
            Medico("M004", "Marta", "Traumatologia"),
            Medico("M005", "Diego", "Medicina General"),
        ]

    @property
    def nombre(self):
        return self._nombre
    @property
    def medicos(self):
        return list(self._medicos)
    @property
    def pacientes(self):
        return list(self._pacientes)
    @property
    def citas(self):
        return list(self._citas)

    def registrar_paciente(self, nombre, edad):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        self._contador_pacientes += 1
        codigo = f"P{self._contador_pacientes:03d}"
        paciente = Paciente(codigo, nombre.strip(), edad)
        self._pacientes.append(paciente)
        return paciente

    def buscar_paciente(self, codigo):
        for p in self._pacientes:
            if p.codigo == codigo.upper():
                return p
        return None

    def buscar_cita(self, codigo):
        for c in self._citas:
            if c.codigo == codigo.upper():
                return c
        return None

    def agendar_cita(self, codigo_paciente, numero_medico, fecha):
        paciente = self.buscar_paciente(codigo_paciente)
        if paciente is None:
            raise ValueError("Paciente no encontrado")
        if numero_medico < 1 or numero_medico > len(self._medicos):
            raise ValueError("Opción de especialidad inválida")
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Fecha inválida, usa el formato dd/mm/aaaa")

        medico = self._medicos[numero_medico - 1]
        for c in self._citas:
            if c.medico == medico and c.fecha == fecha and c.estado == "programada":
                raise ValueError("Ese doctor ya tiene una cita en esa fecha")

        self._contador_citas += 1
        codigo = f"C{self._contador_citas:03d}"
        cita = Cita(codigo, paciente, medico, fecha)
        self._citas.append(cita)
        return cita