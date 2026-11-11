from paciente import Paciente
from medico import Medico
from cita import Cita

paciente_01 = Paciente("P001","Juan",22)
medico_01 = Medico("M001","Oscar","Cardiologia")
cita_01 = Cita("C001",paciente_01,medico_01,"04/11/2026")

print(paciente_01.resumen())
print(medico_01.resumen())
print(cita_01.resumen())
