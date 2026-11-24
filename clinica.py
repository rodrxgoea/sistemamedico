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
        self._medicos = [
            Medico("M001", "Oscar", "Cardiologia"),
            Medico("M002", "Ricardo", "Cardiologia"),
            Medico("M003", "Elena", "Cardiologia"),
            Medico("M004", "Lucia", "Pediatria"),
            Medico("M005", "Andrea", "Pediatria"),
            Medico("M006", "Javier", "Pediatria"),
            Medico("M007", "Carlos", "Dermatologia"),
            Medico("M008", "Sofia", "Dermatologia"),
            Medico("M009", "Raul", "Dermatologia"),
            Medico("M010", "Marta", "Traumatologia"),
            Medico("M011", "Pedro", "Traumatologia"),
            Medico("M012", "Valeria", "Traumatologia"),
            Medico("M013", "Diego", "Medicina General"),
            Medico("M014", "Camila", "Medicina General"),
            Medico("M015", "Hugo", "Medicina General"),
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
        ocupadas = list(filter(
            lambda c: c.medico == medico and c.fecha == fecha and c.estado == "programada",
            self._citas
    ))
        if ocupadas:
            raise ValueError("Ese doctor ya tiene una cita en esa fecha")

        medico = self._medicos[numero_medico - 1]
        for c in self._citas:
            if c.medico == medico and c.fecha == fecha and c.estado == "programada":
                raise ValueError("Ese doctor ya tiene una cita en esa fecha")

        self._contador_citas += 1
        codigo = f"C{self._contador_citas:03d}"
        cita = Cita(codigo, paciente, medico, fecha)
        self._citas.append(cita)
        return cita
    def especialidades(self):
        return list(dict.fromkeys(m.especialidad for m in self._medicos))

    def medicos_por_especialidad(self, especialidad):
        return list(filter(lambda m: m.especialidad == especialidad, self._medicos))

    def buscar_medico(self, codigo):
        resultado = list(filter(lambda m: m.codigo == codigo.upper(), self._medicos))
        return resultado[0] if resultado else None