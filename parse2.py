#!/usr/bin/env python3
"""Genera data.json: plan + escenario planilla, escenario propuesta y análisis.

Fechas ajustadas al Calendario Académico 2026 de la Escuela Superior de Salud
(Res. CAESS N.º 06/2026 y su ampliatoria Res. CAESS N.º 09/2026 para Medicina):
  1.er cuatrimestre: 16/03 al 03/07 (16 semanas).
  2.º cuatrimestre:  10/08 al 27/11 (16 semanas).
  Receso de invierno: 13/07 al 24/07. Receso de verano: enero y 01-14/02.
  En febrero no hay dictado de clases (son fechas de examen y de borrado de inscripción).
Las bimestrales de un mismo cuatrimestre se verificaron contra el cronograma real de
Medicina 2026 (Res. CAESS 09-26, anexo de 1.º año): 1.4 y 1.5 corren EN PARALELO,
ambas entre octubre y noviembre (fin de cuatrimestre), no una atrás de la otra.
Ese es el patrón que se generaliza acá a todo el plan.
"""
import json, re, sys
import openpyxl

SRC, OUT = sys.argv[1], sys.argv[2]

TP = {
 "1.1":(110,110),"1.2":(60,60),"1.3":(70,30),"1.4":(25,25),"1.5":(25,25),
 "2.1":(240,240),"2.2":(20,20),"2.3":(20,20),"2.4":(35,15),"2.5":(20,20),"2.6":(50,50),"2.7":(20,5),
 "3.1":(120,120),"3.2":(75,75),"3.3":(100,100),"3.4":(45,45),"3.5":(25,25),"3.6":(20,20),"3.7":(50,50),"3.8":(20,5),
 "4.1":(160,160),"4.2":(75,75),"4.3":(50,50),"4.4":(25,25),"4.5":(25,25),"4.6":(15,15),"4.7":(25,25),"4.8":(50,50),"4.9":(20,5),
 "5.1":(120,120),"5.2":(65,65),"5.3":(60,60),"5.4":(20,20),"5.5":(35,35),"5.6":(60,60),"5.7":(50,20),"5.8":(50,50),"5.9":(20,5),
 "6.1":(20,60),"6.2":(116,464),"6.3":(10,30),"6.4":(50,50),"6.5":(256,1028),
}
RES_MESES = {"1.1":6,"1.2":4,"1.3":4,"1.4":2,"1.5":2,"2.1":"A","2.2":2,"2.3":2,"2.4":2,"2.5":2,"2.6":4,"2.7":2,
 "3.1":"A","3.2":4,"3.3":"A","3.4":4,"3.5":2,"3.6":2,"3.7":4,"3.8":2,
 "4.1":"A","4.2":4,"4.3":4,"4.4":2,"4.5":2,"4.6":2,"4.7":2,"4.8":4,"4.9":2,
 "5.1":"A","5.2":4,"5.3":4,"5.4":2,"5.5":2,"5.6":4,"5.7":2,"5.8":4,"5.9":2,
 "6.1":4,"6.2":6,"6.3":3,"6.4":4,"6.5":"A"}
MESES_LETRA = {"A":"A","S":6,"C":4,"T":3,"B":2}
CODE = re.compile(r"\d\.\d+")

wb = openpyxl.load_workbook(SRC); ws = wb["Hoja1"]
clean = lambda v: re.sub(r"\s+"," ",str(v)).strip() if v is not None else ""
codes = lambda v: CODE.findall(str(v)) if v is not None else []

subjects, year = [], None
for r in range(3, ws.max_row+1):
    a = clean(ws.cell(r,1).value)
    if a.upper().startswith("TOTAL"): continue
    if a and re.match(r"(\d)", a): year = int(re.match(r"(\d)", a).group(1))
    code = clean(ws.cell(r,3).value)
    if not code: continue
    apr_raw, reg_raw = clean(ws.cell(r,9).value), clean(ws.cell(r,10).value)
    acred = clean(ws.cell(r,11).value)
    t,p = TP[code]
    subjects.append(dict(
        anio=year, dur=clean(ws.cell(r,2).value), codigo=code,
        cuat=int(re.search(r"\d", clean(ws.cell(r,4).value)).group(0)),
        cf=clean(ws.cell(r,5).value), nombre=clean(ws.cell(r,6).value),
        cursado=clean(ws.cell(r,7).value), hs=int(ws.cell(r,8).value), teo=t, pra=p,
        apr=codes(apr_raw), reg=codes(reg_raw),
        regimen="Promoción" if acred.lower().startswith("prom") else "Examen final",
        todoAprobado=("todo" in apr_raw.lower()), segunReglamento=("reglamento" in reg_raw.lower()),
        optativo=(clean(ws.cell(r,5).value)=="FO"), resMeses=RES_MESES[code]))

by = {s["codigo"]: s for s in subjects}

# ---------------------------------------------------------------- escenarios
# Ventanas en meses (para el diagrama): (mes inicio, mes fin, sin receso de julio, flexible)
# 1.er cuatrimestre marzo(3)-julio(7); 2.º cuatrimestre agosto(8)-noviembre(11).
CUAT = {1:(3,7), 2:(8,11)}
# El año tiene cuatro bimestres: 1.er y 2.º en el primer cuatrimestre, 3.er y 4.º en el segundo.
# Por defecto las bimestrales van al 2.º o al 4.º, que es donde las ubica el calendario real
# (1.4 y 1.5, ambas en el 4.º, en paralelo). El 1.er y el 3.er quedan como opción manual.
COLA  = {1:(5,7), 2:(10,11)}
CABEZA = {1:(3,4), 2:(8,9)}
# Fechas reales (día/mes) para cada ventana-tipo, tomadas o extrapoladas del calendario 2026.
FECHA = {
 (3,7):("16/03","03/07"), (8,11):("10/08","27/11"),
 (3,9):("16/03","11/09"),                      # semestral, 1.er cuatrimestre
 (3,11):("16/03","27/11"),                     # anual
 (5,7):("07/05","03/07"), (10,11):("01/10","27/11"),   # 2.º y 4.º bimestre
 (3,4):("16/03","08/05"), (8,9):("10/08","30/09"),      # 1.er y 3.er bimestre
 (3,5):("16/03","13/06"), (8,10):("10/08","06/11"),     # trimestral
}

def base_win(s):
    d, cu = s["dur"], s["cuat"]
    if s["optativo"]:            return dict(ini=CUAT[cu][0], fin=CUAT[cu][1], sr=False, flex=True)
    if d == "A":                 return dict(ini=3, fin=11, sr=False, flex=False)
    if d == "S":                 return dict(ini=3, fin=9, sr=False, flex=False) if cu==1 else dict(ini=8, fin=12, sr=False, flex=False)
    if d == "C":                 return dict(ini=CUAT[cu][0], fin=CUAT[cu][1], sr=False, flex=False)
    if d == "T":                 return dict(ini=3, fin=5, sr=False, flex=False) if cu==1 else dict(ini=8, fin=10, sr=False, flex=False)
    return None  # bimestrales: se asignan abajo, al 2.º o 4.º bimestre

for s in subjects:
    w = base_win(s)
    if w is None:
        c = COLA[s["cuat"]]
        w = dict(ini=c[0], fin=c[1], sr=False, flex=False)
    s["base"] = w

# --- Propuesta ---------------------------------------------------------------
# Criterio (pedido de la coordinación): una bimestral por bimestre, sin paralelismo, como si
# las bimestrales de cada año formaran un anual en cuatro tramos. Paralelo exige más aulas y
# obliga al estudiante a acomodar dos cursadas a la vez. Para decidir el bimestre se miró:
#  - correlativas: cuándo termina la materia previa y cuántos turnos de examen quedan antes
#    de la semana de inscripción (09-13/03 para el 1.er cuatrimestre, 03-07/08 para el 2.º);
#  - turnos de examen: cada bimestre cae en un turno distinto (1.º→junio, 2.º→julio,
#    3.º→octubre, 4.º→diciembre), así que una por bimestre reparte los finales;
#  - carga mensual del resto del año y afinidad de contenidos (Res. C.S. 093-25).
# 1.º y 2.º año quedan como estaban: la coordinación los está trabajando aparte.
BIMW = {1:(3,4), 2:(5,7), 3:(8,9), 4:(10,11)}
PROP_BIM = {
 "3.6": (3, "3.er bimestre (10/08 al 30/09). Es la bimestral del año con examen final: al ubicarla primero, rinde en el turno de octubre junto con Patología General y deja diciembre para los finales de las anuales (3.1 y 3.3). Sus correlativas (2.3 y 2.4 regulares) se cumplen al terminar 2.º año."),
 "3.5": (4, "4.º bimestre (01/10 al 27/11). Es de promoción, así que no suma un final. Va después de Epidemiología para no cursar las dos a la vez. Pide 2.5 aprobada, que también es de promoción y queda aprobada al terminar 2.º año."),
 "4.4": (1, "1.er bimestre (16/03 al 08/05). Rinde en el turno de junio y evita julio, donde ya caen los finales de Clínica Quirúrgica y Bases para el Diagnóstico II. Sus correlativas (2.2 aprobada, 3.3 y 3.4 regulares) son de años anteriores. Si la cátedra prefiere cursarla con Clínica Quirúrgica más avanzada, se puede cambiar con 4.6."),
 "4.6": (2, "2.º bimestre (07/05 al 03/07). Es la más corta del año (30 h) y la que menos carga agrega al 1.er cuatrimestre, que es el más cargado. Sus contenidos (gestión de crisis y emergencias, seguridad del paciente) siguen a Emergencias Médicas II. Pide 3.1 y 3.6 regulares, ya cumplidas."),
 "4.7": (3, "3.er bimestre (10/08 al 30/09). El 2.º cuatrimestre de 4.º año es liviano (solo corren 4.1 y 4.8). Da el marco legal (historia clínica, consentimiento informado, directivas anticipadas) que retoma Relaciones Humanas III. Pide 3.1 y 3.5 regulares. Es intercambiable con 4.5: no hay correlativa entre ellas."),
 "4.5": (4, "4.º bimestre (01/10 al 27/11). Pide 3.5 aprobada: en el 2.º cuatrimestre la inscripción es en agosto, así que quien no promocionó 3.5 tiene los turnos de diciembre a julio para rendirla, en vez de llegar con lo justo al de marzo. Es intercambiable con 4.7."),
 "5.4": (1, "1.er bimestre (16/03 al 08/05). Es la más corta de las tres (40 h) y la que menos carga agrega al 1.er cuatrimestre, ocupado por Niñez y Mujer. Rinde en junio, antes de los finales de julio de 5.2 y 5.3. Sus correlativas (3.6 aprobada, 4.6 y 4.7 regulares) son de años anteriores, y queda regularizada con tiempo para 6.1, 6.2 y 6.3, que la piden."),
 "5.5": (3, "3.er bimestre (10/08 al 30/09). Sigue al bloque clínico del 1.er cuatrimestre (Niñez y Mujer), con el que comparte violencia y el abordaje por etapas de la vida. Rinde sola en el turno de octubre. Es intercambiable con 5.7."),
 "5.7": (4, "4.º bimestre (01/10 al 27/11). Cierra el año con el protocolo de investigación, que 6.2 retoma en 6.º año (investigación-acción participativa, investigación epidemiológica). Pide 2.4 aprobada y 4.5 regular, de años anteriores. Es intercambiable con 5.5. El 2.º bimestre de 5.º año queda libre: es un buen lugar para el optativo IV."),
}
# Optativos: el apartado 10 los deja libres entre 1.º y 5.º año, sin fijarles cuatrimestre. Para que
# se pueda medir cuánto suman a la carga de aulas de cada bimestre (y no diluirlos en 4 meses como si
# fueran cuatrimestrales), se les da un bimestre real de 2 meses: el que queda con menos carga troncal
# en el mismo año. Siguen marcados "flex" (rayado) porque la fecha es orientativa, y se pueden mover
# a cualquier otro bimestre del año desde la pestaña Orden de bimestrales.
OPT_BIM = {
 "2.7": (3, "3.er bimestre (10/08 al 30/09). Es el único bimestre de 2.º año sin materia troncal: no le suma carga a ningún otro. Sigue siendo de fecha libre; se puede mover a cualquier bimestre del año."),
 "3.8": (2, "2.º bimestre (07/05 al 03/07). El 1.er cuatrimestre de 3.º año no tiene ninguna bimestral troncal: es el tramo con más lugar libre del año. Fecha libre; se puede mover a cualquier bimestre del año."),
 "4.9": (2, "2.º bimestre (07/05 al 03/07). Es el bimestre con menos carga troncal de 4.º año (30 h, Calidad de la Atención Médica): sumarle 25 h es lo que menos aulas agrega. Fecha libre; se puede mover a cualquier bimestre del año."),
 "5.9": (2, "2.º bimestre (07/05 al 03/07). Es el único bimestre de 5.º año sin materia troncal: no le suma carga a ningún otro. Fecha libre; se puede mover a cualquier bimestre del año."),
}
for s in subjects:
    c = s["codigo"]
    if s["optativo"]:
        if c in OPT_BIM:
            k, razon = OPT_BIM[c]
            s["prop"] = dict(ini=BIMW[k][0], fin=BIMW[k][1], sr=False, flex=True)
            s["propBim"] = k
            s["propRazon"] = razon
        else:
            s["prop"] = dict(ini=CUAT[s["cuat"]][0], fin=CUAT[s["cuat"]][1], sr=False, flex=True)
            s["propRazon"] = "El apartado 10 de la resolución permite cursar los optativos entre 1.º y 5.º año. Se los deja como 25 h a ubicar donde convenga, en vez de fijarlos a un cuatrimestre."
    elif c in PROP_BIM:
        k, razon = PROP_BIM[c]
        s["prop"] = dict(ini=BIMW[k][0], fin=BIMW[k][1], sr=False, flex=False)
        s["propBim"] = k
        s["propRazon"] = razon
    elif c == "6.2":
        s["prop"] = dict(s["base"])
        s["propRazon"] = "Mar-sep, igual que la planilla. Termina en septiembre, antes de que el Practicantado empiece con el 4.º bimestre (octubre): por eso alcanza con tenerla regular para iniciarlo."
    elif c == "6.4":
        s["prop"] = dict(s["base"])
    elif c == "6.5":
        s["prop"] = dict(ini=10, fin=11, sr=False, flex=False, cola="junio")
        s["propRazon"] = "Arranca junto con el 4.º bimestre de 6.º año (octubre) y termina en junio del año siguiente. Pide todo aprobado salvo 6.2, que alcanza con tenerla regular."
    elif c == "6.1":
        s["prop"] = dict(s["base"])
        s["propRazon"] = "1.º cuatrimestre de 6.º año, igual que la planilla: del inicio del cuatrimestre hasta su cierre (02/07 en 2027)."
    elif c == "6.3":
        # Trimestral: se mantiene en el 1.º cuatrimestre como en la planilla, pero cierra junto con los
        # cuatrimestrales (no a los tres meses), por decisión de la coordinación.
        s["prop"] = dict(ini=4, fin=7, sr=False, flex=False, pk="t1c")
        s["propRazon"] = "Trimestral. Queda en el 1.º cuatrimestre como en la planilla, pero empieza en la 4.ª semana (05/04 en 2027) y termina con el cierre del cuatrimestre (02/07), para cargar una sola planilla de resultados de cursada en SIU Guaraní."
    else:
        s["prop"] = dict(s["base"])

# ------------------------------------------------------------- correlativas
SUG = [
 dict(code="2.6", tipo="Agregar", campo="regular", valor="2.3",
      t="El ECI II necesita el diagnóstico de situación de salud",
      p="Sus contenidos incluyen «el diagnóstico de situación de salud de pequeñas comunidades y grupos sociales», que es lo que desarrolla Salud Poblacional I. Hoy el ECI II solo pide 1.5 aprobada y el resto de 1.º año regular. Como 2.3 es bimestral del 1.º cuatrimestre, pedirla regular es cumplible."),
 dict(code="3.4", tipo="Agregar", campo="regular", valor="2.3",
      t="Noxas y Defensas pide menos que sus pares del mismo año",
      p="Es la única del 1.º cuatrimestre de 3.º que no exige 2.3: sus pares (3.1, 3.2 y 3.3) la piden aprobada. Sus contenidos incluyen «epidemiología de las enfermedades transmisibles» y «medidas preventivas», que son de Salud Poblacional I."),
 dict(code="3.6", tipo="Elevar", campo="aprobada", valor="2.3",
      t="La continuidad directa de la línea poblacional pide menos que las clínicas",
      p="Salud Poblacional II es la continuación de Salud Poblacional I y hoy solo la pide regular, mientras que 3.1, 3.2 y 3.3 exigen 2.3 aprobada. Conviene unificar: 2.3 aprobada y 2.4 regular."),
 dict(code="4.3", tipo="Unificar", campo="aprobada", valor="3.3",
      t="Bases para el Diagnóstico II exige más que las materias troncales",
      p="Pide 3.3 aprobada, mientras que Salud del Adulto I y Clínica Quirúrgica, que son las troncales del año, piden la misma materia solo regular. Si se mantiene, el estudiante tiene que rendir el final de una materia anual en el turno de febrero para poder cursar. Conviene unificar el criterio entre las tres."),
 dict(code="5.1", tipo="Agregar", campo="aprobada", valor="3.2, 3.3",
      t="Especialidades Médicas no exige ninguna materia aprobada",
      p="Es la materia anual troncal de 5.º año, de 240 h y con promoción, y aborda la patología prevalente de cada especialidad con su etiopatogenia, fisiopatología y terapéutica. Hoy solo pide 4.1, 4.2 y 4.3 regulares. Razonable pedir Patología General y Bases para el Diagnóstico I aprobadas."),
 dict(code="5.6", tipo="Agregar", campo="aprobada", valor="4.1",
      t="Salud del Adulto II no exige aprobada Salud del Adulto I",
      p="Es la continuidad directa I → II y hoy solo pide 4.1 y 4.3 regulares. Como referencia, Salud del Adulto I sí exige 2.1 aprobada. Sus contenidos (paciente crítico, oncológico, cuidados paliativos, polifarmacia) suponen el adulto resuelto."),
 dict(code="6.2", tipo="Agregar", campo="regular", valor="5.2, 5.3, 5.6",
      t="Salud Comunitaria se puede cursar sin tener regular Niñez ni Mujer",
      p="Hoy pide 4.5 aprobada y 5.4 regular. Atiende «individuos, familias y comunidades» y los «problemas de salud prevalentes» de la medicina general, lo que supone la clínica de 5.º año cursada. Conviene exigir regulares las materias clínicas de 5.º."),
 dict(code="3.5", tipo="Flexibilizar", campo="aprobada → regular", valor="2.5",
      t="Relaciones Humanas II podría pedir RH I regular en vez de aprobada",
      p="La línea Relaciones Humanas es progresiva pero no acumulativa en sentido estricto: RH II trabaja comunicación, ciclos vitales y relación médico-paciente-familia, que se apoyan en RH I sin necesitar su examen aprobado. RH I es de promoción, así que la diferencia solo afecta a quien no promocionó: con «regular» puede seguir la línea sin perder un año. Mismo criterio que se propone para 4.5."),
 dict(code="4.5", tipo="Flexibilizar", campo="aprobada → regular", valor="3.5",
      t="Relaciones Humanas III podría pedir RH II regular en vez de aprobada",
      p="RH III (profesionalismo, comunicación de malas noticias, muerte y cuidados paliativos) continúa RH II, que es de promoción. Pedirla regular alcanza para asegurar la secuencia y evita que quien no promocionó RH II quede afuera de RH III, que además es correlativa aprobada de 6.2. Con la ubicación propuesta (4.º bimestre, inscripción en agosto) el problema ya se atenúa; esta flexibilización lo resuelve del todo."),
 dict(code="5.7", tipo="Cambiar", campo="regular", valor="4.5 → 3.6",
      t="Investigación en Ciencias de la Salud se apoya más en Epidemiología que en RH III",
      p="Hoy pide 2.4 aprobada y 4.5 regular. De RH III comparte un solo tema (la comunicación en la investigación clínica). En cambio sus contenidos (estudios epidemiológicos, clínicos y de servicios de salud; bioestadística; validez y confiabilidad de pruebas diagnósticas) son la continuación directa de Salud Poblacional II: Epidemiología (investigación epidemiológica, epidemiología clínica). Se propone cambiar la regular 4.5 por 3.6, o al menos agregar 3.6."),
 dict(code="6.5", tipo="Reformular", campo="aprobada", valor="Todas regularizadas",
      t="«Todo aprobado» bloquea el propio diseño del 6.º año",
      p="Con esa exigencia, el Practicantado no puede convivir con 6.1 a 6.4 del mismo año. Se propuso resolverlo permitiendo inscribirse con todas regularizadas, y exigiendo todas aprobadas recién antes de rendir el final de la PFO. IMPORTANTE: no encontramos en el Reglamento Académico (Res. C.S. 066-22) un artículo general que habilite esto; ver el punto de Revisión sobre el régimen de cursada antes de llevar esta redacción a la comisión."),
]
INCONS = [
 dict(t="El Practicantado pide todo aprobado salvo 6.2 regular",
      p="La planilla dice «Todo aprobado». La Propuesta exige aprobadas 1.1 a 6.1, 6.3 y 6.4 (y las demás del plan) y solo regular 6.2, para que el Practicantado pueda iniciar sin esperar el final de Salud Comunitaria y Familiar. Es una excepción puntual a «Todo aprobado» que conviene dejar escrita en la resolución del plan.",
      codes=["6.2","6.5"]),
 dict(t="Las rotaciones electivas están fuera del Practicantado",
      p="El apartado 10 de la resolución dice que los estudiantes «contarán con espacios optativos durante la PFO» y que «consistirán en rotaciones electivas». En la planilla, 6.1 y 6.3 figuran en el 1.º cuatrimestre de 6.º año, antes del Practicantado, y la Propuesta las mantiene ahí por decisión de la coordinación. Falta ubicarlas dentro del tramo de la PFO o corregir el apartado 10.",
      codes=["6.1","6.3"]),
 dict(t="Los optativos están fijados a un año y la resolución no los fija",
      p="El apartado 10 dice que los optativos se pueden realizar «entre el primero y el quinto año inclusive». La planilla los fija uno por año en 2.º, 3.º, 4.º y 5.º, siempre en el 2.º cuatrimestre, que es justo el tramo más cargado. Dejarlos como 25 h a cumplir en cualquier momento del tramo 1.º-5.º descomprime esos cuatrimestres.",
      codes=["2.7","3.8","4.9","5.9"]),
 dict(t="La duración de Patología General difiere entre los dos documentos",
      p="La planilla la toma como semestral (6 meses), que es la decisión tomada. La tabla del apartado 7 de la Res. C.S. 093-25 dice 4 meses. Hay que corregir la tabla de la resolución para que coincida.",
      codes=["3.2"]),
 dict(t="El Practicantado figura en 6.º año y la resolución lo pone en 7.º",
      p="La planilla lo codifica 6.5 dentro de 6.º año. La tabla de la resolución lo codifica 7.1 y declara 800 h para 6.º año y 1.284 h para 7.º. Si se mantiene 6.5 con inicio en octubre (junto al 4.º bimestre) y cierre en junio del año siguiente, hay que ajustar la tabla de cargas horarias por año de la resolución.",
      codes=["6.5"]),
 dict(t="El plan no fija en qué bimestre va cada bimestral",
      p="La planilla y la resolución marcan las materias como «B» con su cuatrimestre, pero no dicen si van en el 1.º o 2.º bimestre del cuatrimestre. Hoy, por defecto, todas caen al final del cuatrimestre y quedan en paralelo (en 4.º y 5.º año, hasta tres a la vez). La propuesta ubica una por bimestre en 3.º, 4.º y 5.º año, mirando correlativas, turnos de examen y carga mensual; cada movimiento tiene su fundamento en la pestaña Orden de bimestrales. 6.º año no tiene bimestrales. 1.º y 2.º año quedan como en la planilla hasta incorporar lo que trabajó la coordinación. La inscripción es única por cuatrimestre (una semana a principios de marzo para todo el 1.er cuatrimestre y otra en agosto para el 2.º), según lo definió el equipo: por eso una materia del 2.º cuatrimestre deja más turnos para rendir sus correlativas.",
      codes=["3.5","3.6","4.4","4.5","4.6","4.7","5.4","5.5","5.7"]),
]

tot = sum(s["hs"] for s in subjects)
por_anio = {}
for s in subjects: por_anio[s["anio"]] = por_anio.get(s["anio"],0) + s["hs"]
checks = dict(total=tot, porAnio=por_anio, teo=sum(s["teo"] for s in subjects),
              pra=sum(s["pra"] for s in subjects), n=len(subjects))
print(json.dumps(checks, ensure_ascii=False))
for s in subjects:
    if MESES_LETRA[s["dur"]] != s["resMeses"]:
        print("DIFF duración", s["codigo"], s["dur"], "vs res:", s["resMeses"])

# ---------------------------------------------------------------- cambios de correlativas
# Aplicados en «Propuesta» por decisión de la coordinación. La planilla original no se toca.
CORR_CAMBIOS = [
 dict(code="3.5", campo="apr", pasa="2.5", t="Relaciones Humanas I pasa de aprobada a regular",
      p="La línea Relaciones Humanas es progresiva: RH II se apoya en RH I sin necesitar su examen aprobado. RH I es de promoción, así que solo cambia algo para quien no promocionó, que puede seguir la línea sin perder un año."),
 dict(code="4.5", campo="apr", pasa="3.5", t="Relaciones Humanas II pasa de aprobada a regular",
      p="RH III continúa RH II, que es de promoción. Pedirla regular asegura la secuencia y evita que quien no promocionó RH II quede afuera de RH III, que además es correlativa aprobada de 6.2."),
 dict(code="6.5", campo="apr", nuevaApr="TODAS_MENOS_6.2", nuevaReg=["6.2"], t="El Practicantado pide todo aprobado, salvo 6.2 regular",
      p="Para iniciar el Practicantado hay que tener aprobadas de 1.1 a 6.1, 6.3 y 6.4, y regular 6.2 (Salud Comunitaria y Familiar). Es «Todo aprobado» de la planilla con una única excepción: 6.2 alcanza con tenerla regular, para que el Practicantado pueda empezar sin esperar su final."),
]
for s in subjects:
    s["aprP"]=list(s["apr"]); s["regP"]=list(s["reg"])
for c in CORR_CAMBIOS:
    s=by[c["code"]]
    if c.get("quita"):
        assert c["quita"] in s["aprP"], c; s["aprP"].remove(c["quita"])
    for q in c.get("quitaReg",[]):
        assert q in s["regP"], c; s["regP"].remove(q)
    if c.get("nuevaApr"):
        s["aprP"]=[x["codigo"] for x in subjects if x["codigo"] not in (c["code"],"6.2")]; s["regP"]=list(c["nuevaReg"]); s["todoP"]=False
    if c.get("pasa"):
        assert c["pasa"] in s["aprP"], c; s["aprP"].remove(c["pasa"])
        if c["pasa"] not in s["regP"]: s["regP"].append(c["pasa"])
# Criterio de la coordinación: solo flexibilizar o quitar redundancias, sin agregar exigencias.
# Las sugerencias de la primera revisión (casi todas endurecían) se descartan.
SUG = []


json.dump(dict(ver=3, subjects=subjects, corrCambios=CORR_CAMBIOS, sugerencias=SUG, inconsistencias=INCONS, checks=checks,
               fechas={f"{k[0]}-{k[1]}": v for k, v in FECHA.items()}),
          open(OUT,"w"), ensure_ascii=False, indent=1)
print("ok", OUT)
