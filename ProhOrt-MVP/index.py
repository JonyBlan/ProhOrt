from asyncio.windows_events import NULL
import pyodbc
import math

# from services.db import DB

#sql = DB('Driver={SQL Server};'
#        'Server=A-PHZ2-AMI-011;'
#        'Database=ProhOrt-Mvp;'
#        'Trusted_Connection=yes;')

#sql.FillCursos()

# Llenar datos

cantBloquesTotales = 3
cursos = []
profesores = []
aulas = []
bloques = []
resultados = []
anios = []
orientaciones = []
materias = []
profesorxMaterias = []

def fillCursos():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=A-PHZ2-AMI-011;'
                        'Database=ProhOrt-Mvp;'
                        'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Curso')
    #cursos = [curso for curso in cursor]
    for curso in cursor:
        cursos.append(curso)


def fillAulas():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=A-PHZ2-AMI-011;'
                        'Database=ProhOrt-Mvp;'
                        'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Aula')
    
    for aula in cursor:
        aulas.append(aula)

def fillProfesores():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=A-PHZ2-AMI-011;'
                        'Database=ProhOrt-Mvp;'
                        'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Profesor')
    
    for profesor in cursor:
        profesores.append(profesor)

def fillBloques():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=A-PHZ2-AMI-011;'
                        'Database=ProhOrt-Mvp;'
                        'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Bloque')
    
    for bloque in cursor:
        bloques.append(bloque)

def fillAnios():
            conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=A-PHZ2-AMI-011;'
                                'Database=ProhOrt-Mvp;'
                                'Trusted_Connection=yes;')
            
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Anio')
            
            for i in cursor:
                anios.append(i)

def fillOrientaciones():
            conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=A-PHZ2-AMI-011;'
                                'Database=ProhOrt-Mvp;'
                                'Trusted_Connection=yes;')
            
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Orientacion')
            
            for i in cursor:
                orientaciones.append(i)

def fillMaterias():
            conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=A-PHZ2-AMI-011;'
                                'Database=ProhOrt-Mvp;'
                                'Trusted_Connection=yes;')
            
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Materia')
            
            for i in cursor:
                materias.append(i)

def fillProfesorxMaterias():
            conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=A-PHZ2-AMI-011;'
                                'Database=ProhOrt-Mvp;'
                                'Trusted_Connection=yes;')
            
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM ProfesorxMateria')
            
            for i in cursor:
                profesorxMaterias.append(i)

def fillEverything():
    fillCursos()
    fillAulas()
    fillProfesores()
    fillBloques()
    fillAnios()
    fillOrientaciones()
    fillMaterias()
    fillProfesorxMaterias()
    print("Todo fue llenado correctamente")

fillEverything()

class Curso:
    def __init__(self, _id, _nombre, _bloquesOcupados, _disponibilidad, _idOrientacion, idAnio, _minBloquesxDia, _maxBloquesxDia, _minEntrada, _maxEntrada):
        
        self.id = _id
        self.nombre = _nombre
        self.bloquesOcupados = _bloquesOcupados
        self.disponibilidad = _disponibilidad
        self.idOrientacion = _idOrientacion
        self.idAnio = idAnio
        self.minBloquesxDia = _minBloquesxDia
        self.maxBloquesxDia = _maxBloquesxDia
        self.minEntrada = _minEntrada
        self.maxEntrada = _maxEntrada

class Aula:
    def __init__(self, _id, _nombre, _disponibilidad):
        self.id = _id
        self.nombre = _nombre
        self.disponibilidad = _disponibilidad

class Profesor:
    def __init__(self, _id, _nombre, _apellido, _disponibilidad, _minBloquesxDia, _maxBloquesxDia):
        self.id = _id
        self.nombre = _nombre
        self.apellido = _apellido
        self.disponibilidad = _disponibilidad
        self.minBloquesxDia = _minBloquesxDia
        self.maxBloquesxDia = _maxBloquesxDia

def anotarClase(bloque, curso, profesor, aula, numBloque):
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=A-PHZ2-AMI-011;'
                        'Database=ProhOrt-Mvp;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()
    
    bloqueEnCodigo = str(10**(cantBloquesTotales - numBloque))
    
    cursor.execute('UPDATE Curso SET Disponibilidad = Disponibilidad - ' + bloqueEnCodigo + ' WHERE IdCurso = ' + str(curso))
    cursor.execute('UPDATE Profesor SET Disponibilidad = Disponibilidad - ' + bloqueEnCodigo + ' WHERE IdProfesor = ' + str(profesor))
    cursor.execute('UPDATE Aula SET Disponibilidad = Disponibilidad - ' + bloqueEnCodigo + ' WHERE IdAula = ' + str(aula))
    cursor.execute('INSERT INTO Bloque (IdProfesor, IdAula, IdCurso) VALUES (' + str(profesor) + ', ' + str(aula) + ', ' + str(curso) + ')')
    
    conn.commit()

def ponerComoDefault():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=A-PHZ2-AMI-011;'
                        'Database=ProhOrt-Mvp;'
                        'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    cursor.execute('UPDATE Curso SET Disponibilidad = 111')
    cursor.execute('UPDATE Aula SET Disponibilidad = 111')
    cursor.execute('UPDATE Profesor SET Disponibilidad = 111')
    cursor.execute('UPDATE Anio SET CargaHoraria = 333')
    #cursor.execute('UPDATE Orientacion SET [columna] = [valor default]')
    #cursor.execute('UPDATE Materia SET [columna] = [valor default]')
    #cursor.execute('DELETE FROM Bloque')

    conn.commit()

def bajarTabla(tableName):
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=A-PHZ2-AMI-011;'
                        'Database=ProhOrt-Mvp;'
                        'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + tableName)
    
    for i in cursor:
        tableName.append(i)

# Declaraciones Basicas
cantCursos = len(cursos) #3
cantAulas = len(aulas) #5
cantProfesores = len(profesores) #5
cantBloques = len(bloques) #9 (3 por curso)
cantAnio = len(anios)
cantOrientacion = len(orientaciones)
cantMateria = len(materias)
cantProfesorxMateria = len(profesorxMaterias)

class Materia:
    def __init__(self, _id, _nombre, _prioridad, _numBloques):
        self.id = _id
        self.nombre = _nombre
        self.prioridad = _prioridad
        self.numBloques = _numBloques

class DatosBloque:
    def __init__(self, _dia, _numBloque, _numCurso, _idProfesor, _idAula, _idMateria):
        self.dia = _dia
        self.numBloque = _numBloque
        self.numCurso = _numCurso
        self.idProfesor = _idProfesor
        self.idAula = _idAula
        self.idMateria = _idMateria

def error(code):
    print("ERROR CODE " + str(code))
    exit()

def final(msg):
    print(msg)
    print("continue para borrar los datos")
    exit()


maxBloquesDia = [[5, 5, 5, 5, 5, -1, -1], [5, 5, 5, 5, 5, -1, -1], [5, 5, 5, 5, 5, -1, -1]] # falta automatizar por cantidad de cursos
minBloquesDia = [[3, 3, 3, 3, 3, -1, -1], [3, 3, 3, 3, 3, -1, -1], [3, 3, 3, 3, 3, -1, -1]] # falta automatizar por cantidad de cursos
bloquesDiaReal = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] # falta automatizar por cantidad de cursos
cantBloquesReal = [20, 20, 20]  # falta automatizar por cantidad de cursos
cantBloquesOcupados = [0, 0, 0]  # falta automatizar por cantidad de cursos
# horarioEntrada va del -2 a maxBloquesDia, hay 14 valores y representan el bloque de entrada minimo y maximo por dia. -1 indica que ese dia no hay clase, -2 que es cualquier horario (siempre que de resultados), y x>=0 los bloquesAux
horarioEntrada = [[[1, 1], [0, 0], [0, 0], [0, 0], [0, 0], [-1, -1], [-1, -1]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1, -1], [-1, -1]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1, -1], [-1, -1]]]  # falta automatizar por cantidad de cursos y dias

# Variables que se llenan acorde al usuario
# bloquesxDia va del -3 al 7 inclusive: -3 significa que ya fue asignado, -2 significa que no hay clase en todo el dia, -1 significa que en ese bloque no hay clase, 0 que todavia no fue asignado (no deberia quedar ninguno cuando finaliza la ejecucion), y del 1 al 7 la prioridad de llenar el bloque
bloquesxDia = [] #bloquesxDia[numCurso][numDiaDeSemana][numBloque]
bloquesAux = []
diasSemana = len(maxBloquesDia[0])

# Aca empieza la logica
maxBloques = 0
maxCantBloques = 5
diasSemanaEscuela = [0, 0, 0]
cantBloques = [0, 0, 0]

def declaracionesIniciales():
    maxCantBloques = 5
    for numCurso in range(cantCursos):
        for i in range(diasSemana):
            if maxBloquesDia[numCurso][i] != -1:
                diasSemanaEscuela[numCurso] = diasSemanaEscuela[numCurso] + 1
                if(maxBloquesDia[numCurso][i] > maxCantBloques):
                    maxCantBloques = maxBloquesDia[numCurso][i]
        cantBloques[numCurso] = maxCantBloques*diasSemanaEscuela[numCurso]

    for b in range(cantCursos):
        bloquesxDia.append([])
        for i in range(diasSemana):
            bloquesxDia[b].append([])
            for a in range(maxCantBloques):
                bloquesxDia[b][i].append(0)

def condicionalesIniciales():
    for idCurso in range(cantCursos):
        if(cantAulas < cantCursos):
            error(1)
        if(cantProfesores < cantCursos):
            error(2)
        if(cantBloques[idCurso] < cantCursos):
            error(3)
        for diaSemana in range(diasSemana):
            if(maxBloquesDia[idCurso][diaSemana] - minBloquesDia[idCurso][diaSemana] < 0):
                error(10)
            elif((maxBloquesDia[idCurso] == -1 and minBloquesDia[idCurso] != -1) or (maxBloquesDia[idCurso] != -1 and minBloquesDia[idCurso] == -1)):
                error(11)
            elif(horarioEntrada[idCurso][diaSemana][1] - horarioEntrada[idCurso][diaSemana][0] < 0):
                error(12)
            elif(maxBloquesDia[idCurso][diaSemana] - minBloquesDia[idCurso][diaSemana]) < horarioEntrada[idCurso][diaSemana][0]:
                error(9)
            elif(horarioEntrada[idCurso][diaSemana][0] >= 0 and maxBloquesDia[idCurso][diaSemana] >= 0):
                #for numCurso in range(cantCursos):
                    if(maxBloquesDia[idCurso][diaSemana] != -1):
                        for hora in range(horarioEntrada[idCurso][diaSemana][0]):
                            bloquesxDia[idCurso][diaSemana][hora] = -1
                    if(maxBloquesDia[idCurso][diaSemana] - horarioEntrada[idCurso][diaSemana][0] == minBloquesDia[idCurso][diaSemana]):
                        for hora in range(horarioEntrada[idCurso][diaSemana][0], maxCantBloques):
                            bloquesxDia[idCurso][diaSemana][hora] = 7
            elif(maxBloquesDia[idCurso][diaSemana] == -1):
                #for numCurso in range(cantCursos):
                    for bloque in range(maxCantBloques):
                        bloquesxDia[idCurso][diaSemana][bloque] = -2
            else:
                error(13)

def checkearDisponibilidad(disponibilidad, dia, numBloque, numArray, idLlamador):
    if(disponibilidad[dia][numBloque] == 1 or disponibilidad[dia][numBloque] == "1"):
        return True
    elif(disponibilidad[dia][numBloque] == 0 or disponibilidad[dia][numBloque] == "0"):
        return False

def cambiarDatos(dbq):
    cursos[dbq.numCurso][dbq.dia][dbq.numBloque] = 0
    profesores[dbq.idProfesor][dbq.dia][dbq.numBloque] = 0
    aulas[dbq.idAula][dbq.dia][dbq.numBloque] = 0
    materias[dbq.numCurso][dbq.idMateria].numBloques = materias[dbq.numCurso][dbq.idMateria].numBloques - 1
    bloquesxDia[dbq.numCurso][dbq.dia][dbq.numBloque] = -3
    cantBloquesOcupados[dbq.numCurso] = cantBloquesOcupados[dbq.numCurso] + 1
    bloquesDiaReal[dbq.numCurso][dbq.dia] = bloquesDiaReal[dbq.numCurso][dbq.dia] + 1

def guardarBloque(dbq):
    bloquesAux.append([dbq.dia, dbq.numBloque, dbq.numCurso, dbq.idProfesor, dbq.idAula, dbq.idMateria])

def avisarConsola(idBloque):
    if(idBloque == -1):
        idBloque = len(bloquesAux)
    print("Bloque completo: " + str(bloquesAux[idBloque]))

def nuevoBloque(datosBloque, idBloque):
    guardarBloque(datosBloque)
    cambiarDatos(datosBloque)
    avisarConsola(idBloque)

def forzarBloque(dia, numBloque, numCurso, idProfesor, idAula, idMateria):
    if(cursos[numCurso][dia][numBloque] == 0 or profesores[idProfesor][dia][numBloque] == 0 or aulas[idAula][dia][numBloque] == 0 or materias[numCurso][dia][idMateria].numBloques == 0):
        error(8)
    else:
        datosBloque = DatosBloque(dia, numBloque, numCurso, idProfesor, idAula, materias[numCurso][idMateria].id)
        nuevoBloque(datosBloque, -1)

def elegirMateria(numCurso):
    for idMateria in range(len(materias[numCurso])):
        if(materias[numCurso][idMateria].numBloques > 0):
            return idMateria
    return -1

def elegirCursoBloque(dia, numBloque):
    for idCurso in range(len(cursos)):
        if(checkearDisponibilidad(cursos[idCurso], dia, numBloque, idCurso, 0)):
            return idCurso
    return -1

def elegirProfesor(dia, numBloque):
    for idProfesor in range(len(profesores)):
        if(checkearDisponibilidad(profesores[idProfesor], dia, numBloque, idProfesor, 1)):
            return idProfesor
    return -1

def elegirAula(dia, numBloque):
    for idAula in range(len(aulas)):
        if(checkearDisponibilidad(aulas[idAula], dia, numBloque, idAula, 2)):
            return idAula
    return -1

def elegirCurso():
    for numCurso in range(cantCursos):
        if(cantBloquesOcupados[numCurso] < cantBloquesReal[numCurso]):
            return numCurso
    return -1

def llenarDatosBloque(numCurso, dia, numBloque):
    idMateria = elegirMateria(numCurso)
    idProfesor = elegirProfesor(dia, numBloque)
    idAula = elegirAula(dia, numBloque)
    return (DatosBloque(dia, numBloque, numCurso, idProfesor, idAula, idMateria))

def verificacionFinal(todosContados):
    if(todosContados):
        for numCurso in range(cantCursos):
            for numBloque in range(len(bloquesxDia[numCurso])):
                if(bloquesxDia[numCurso][numBloque] == 0):
                    bloquesxDia[numCurso][numBloque] = -4
        print(bloquesxDia)
        print(bloquesDiaReal)
        final("se llenaron todos los bloques")
    print(bloquesxDia)
    print("")
    error(4)

def llenarBloque(vuelta):
    for numCurso in range(cantCursos):
        if(cantBloquesOcupados[numCurso] < cantBloquesReal[numCurso]):
            for preNumBloque in range(cantBloques[numCurso]):
                dia = preNumBloque%maxCantBloques
                numBloque = math.trunc(preNumBloque/maxCantBloques)
                datosBloque = llenarDatosBloque(numCurso, dia, numBloque)
                if(datosBloque.idAula != -1 and datosBloque.idProfesor != -1 and datosBloque.idMateria != -1):
                    if(bloquesxDia[numCurso][dia][numBloque] >= 0):
                        nuevoBloque(datosBloque, vuelta)
                        return 1
    todosContados = True
    for i in range(cantCursos):
        if(cantBloquesOcupados[i] != cantBloquesReal[i]):
            todosContados = False
            print(bloquesxDia)
            error(4)
    verificacionFinal(todosContados)

def stringToArray(string):
    array = []
    for id in range(len(string)):
        array.append(int(string[id]))
    return array

def cambiarDisponibilidades(array, numArray, cant):
    for numArray in range(cant):
        if(len(array[numArray].Disponibilidad) != cant[numArray]):
            array[numArray].Disponibilidad = array[numArray].Disponibilidad[::-1]
            for i in range(cant[numArray] - len(array[numArray].Disponibilidad)):
                array[numArray].Disponibilidad += '0'
            array[numArray].Disponibilidad = array[numArray].Disponibilidad[::-1]
        array[numArray].Disponibilidad = stringToArray(array[numArray].Disponibilidad)

def cambiarDisponibilidades(array, cant):
    for numArray in range(cant):
        if(len(array[numArray].Disponibilidad) != cant[numArray]):
            array[numArray].Disponibilidad = array[numArray].Disponibilidad[::-1]
            for i in range(cant[numArray] - len(array[numArray].Disponibilidad)):
                array[numArray].Disponibilidad += '0'
            array[numArray].Disponibilidad = array[numArray].Disponibilidad[::-1]
        array[numArray].Disponibilidad = stringToArray(array[numArray].Disponibilidad)
    
    for numCurso in range(cantCursos):
        if(len(cursos[numCurso].Disponibilidad) != cantBloques[numCurso]):
            cursos[numCurso].Disponibilidad = cursos[numCurso].Disponibilidad[::-1]
            for i in range(cantBloques[numCurso] - len(cursos[numCurso].Disponibilidad)):
                cursos[numCurso].Disponibilidad += '0'
            cursos[numCurso].Disponibilidad = cursos[numCurso].Disponibilidad[::-1]
        cursos[numCurso].Disponibilidad = stringToArray(cursos[numCurso].Disponibilidad)

def pasarAObjetos():
    cambiarDisponibilidades(cursos, cantCursos)
    cambiarDisponibilidades(profesores, cantProfesores)
    cambiarDisponibilidades(aulas, cantAulas)
    
    
def preInicio():
    declaracionesIniciales()
    condicionalesIniciales()
    pasarAObjetos()
    print(cursos)
    exit()

def llenarBloques():
    preInicio()
    vueltas = -1
    if vueltas != -1:
        for i in range(vueltas):
            llenarBloque(i)
    else:
        i = 0
        while True:
            llenarBloque(i)
            i = i + 1
    print("Llego al final. Continuar para borrar datos")
    print("")

llenarBloques()


#ponerComoDefault() # Devuelve los valores de las disponibilidades al default