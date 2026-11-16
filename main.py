from paciente import Paciente
from medico import Medico
from cita import Cita
from clinica import Clinica

MOTIVOS = ["Control", "Chequeo general", "Consulta de rutina", "Seguimiento"]

def pedir_numero(texto):
    try:
        return int(input(texto))
    except ValueError:
        raise ValueError("Debes escribir un número")

def mostrar_menu():
    print("\n===== VENTANILLA =====")
    print("1. Registrar paciente")
    print("2. Generar cita (asignar doctor)")
    print("3. Atender cita (genera consulta)")
    print("4. Cancelar cita")
    print("5. Ver historial de un paciente")
    print("6. Ver doctores")
    print("7. Ver citas")
    print("0. Salir")

def mostrar_doctores(clinica):
    print("\n--- Especialidades disponibles ---")
    for i, m in enumerate(clinica.medicos, start=1):
        print(f"{i}. {m.especialidad} - Dr. {m.nombre}")

def main():
    clinica = Clinica("AGUIRRE")
    print(f"\n=====Bienvenido a {clinica.nombre}====1=")
    print(f"Trabajando por tu Salud")
   
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del paciente: ")
                edad = pedir_numero("Edad: ")
                p = clinica.registrar_paciente(nombre, edad)
                print("Paciente registrado:", p.resumen())

            elif opcion == "2":
                codigo = input("Código del paciente (ej. P001): ")
                if clinica.buscar_paciente(codigo) is None:
                    raise ValueError("Paciente no encontrado")
                mostrar_doctores(clinica)
                numero = pedir_numero("Elige la especialidad (1-5): ")
                fecha = input("Fecha de la cita (dd/mm/aaaa): ")
                cita = clinica.agendar_cita(codigo, numero, fecha)
                print("Cita generada:", cita.resumen())

            elif opcion == "3":
                codigo = input("Código de la cita (ej. C001): ")
                cita = clinica.buscar_cita(codigo)
                if cita is None:
                    raise ValueError("Cita no encontrada")
                print("\nMotivos:")
                for i, m in enumerate(MOTIVOS, start=1):
                    print(f"{i}. {m}")
                n = pedir_numero("Elige el motivo: ")
                if n < 1 or n > len(MOTIVOS):
                    raise ValueError("Motivo inválido")
                cita.atender(MOTIVOS[n - 1], "Sin novedades")
                print("Cita atendida y consulta guardada en el historial")

            elif opcion == "4":
                codigo = input("Código de la cita: ")
                cita = clinica.buscar_cita(codigo)
                if cita is None:
                    raise ValueError("Cita no encontrada")
                cita.cancelar()
                print("Cita cancelada")

            elif opcion == "5":
                codigo = input("Código del paciente: ")
                p = clinica.buscar_paciente(codigo)
                if p is None:
                    raise ValueError("Paciente no encontrado")
                print(f"\nHistorial de {p.nombre}:")
                print(p.mostrar_historial())

            elif opcion == "6":
                mostrar_doctores(clinica)

            elif opcion == "7":
                if not clinica.citas:
                    print("No hay citas registradas")
                for c in clinica.citas:
                    print(f"{c.resumen()} [{c.estado}]")

            elif opcion == "0":
                print("Hasta luego")
                break

            else:
                print("Opción no válida")

        except ValueError as e:
            print("Error:", e)

main()
