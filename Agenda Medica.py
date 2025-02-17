


from myFun1 import hospitales, medicos

def capturar_datos_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    telefono = input("Ingrese el teléfono del paciente: ")
    identificacion = input("Ingrese la identificación del paciente: ")
    return {"nombre": nombre, "telefono": telefono, "identificacion": identificacion}

def agendar_cita(hospital, medico, paciente, horario_disponible):
    print("\nLa información de la cita es la siguiente:")
    print("Hospital:", end=" ")
    hospitales(hospital)
    print("Médico asignado:", end=" ")
    medicos(hospital, medico)
    print("Horario de la cita:", horario_disponible)
    print("Nombre del paciente:", paciente['nombre'])
    print("Teléfono del paciente:", paciente['telefono'])
    print("Identificación del paciente:", paciente['identificacion'])

def generar_horarios(hospital):
    # Establecemos un turno de 12 horas, de 8:00 a 20:00
    inicio_turno = 8
    fin_turno = 20
    horas_por_turno = fin_turno - inicio_turno
    if hospital == '1':
        medicos_hospital = 2
    elif hospital == '2':
        medicos_hospital = 3
    elif hospital == '3':
        medicos_hospital = 1
    else:
        print("Hospital no válido.")
        return []

    citas_por_medico = horas_por_turno // medicos_hospital
    horarios = []
    for medico_num in range(medicos_hospital):
        for cita in range(citas_por_medico):
            hora_cita = inicio_turno + cita + (citas_por_medico * medico_num)
            horario = f"{hora_cita}:00 - {hora_cita + 1}:00"
            horarios.append(horario)
    return horarios

# Programa principal
pacientes = []
horarios_disponibles = []

for i in range(5):  # Para agendar cinco citas de pacientes
    print(f"\nAgendando cita para el paciente {i + 1}")
    paciente = capturar_datos_paciente()
    mi_hospital = hospitales()
    mi_medico = medicos(mi_hospital)

    if not horarios_disponibles:  # Generar horarios si no están disponibles
        horarios_disponibles = generar_horarios(mi_hospital)

    if horarios_disponibles:
        horario_cita = horarios_disponibles.pop(0)  # Asigna el siguiente horario disponible
        agendar_cita(mi_hospital, mi_medico, paciente, horario_cita)
    else:
        print("No hay horarios disponibles para este hospital.")