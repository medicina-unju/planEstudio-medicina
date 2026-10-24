# Plan de estudios de Medicina — Escuela Superior de Salud, UNJu

Tablero web para trabajar la secuencia de cursada, las correlatividades y las cargas horarias
de la carrera de Medicina (Res. C.S. N.º 0191-24 y su modificación, Res. C.S. N.º 093-25).

Es una sola página, sin backend ni instalación. Se puede publicar en GitHub Pages y compartir por enlace.

## Qué hay en cada pestaña

| Pestaña | Para qué sirve |
| --- | --- |
| Secuencia | Diagrama mes a mes, filtrable por año y por período con casillas (1.º cuatrimestre: anuales, cuatrimestrales, 1.er y 2.º bimestre, semestrales; 2.º cuatrimestre: cuatrimestrales, 3.er y 4.º bimestre, anuales, semestrales y Práctica Final; anuales y semestrales figuran en los dos porque se inscriben en marzo y cierran el acta en el 2.º). Abajo, el seguimiento de actas por turno, del 1.º al 8.º: en cada turno, qué materias llegan por primera vez y cuándo cierra su acta de cursada. |
| Plan completo | El plan con el mismo formato de la planilla de correlativas (Excel). En modo edición cada casilla de texto (espacio curricular, cursado, horas, correlativas, acreditación) se puede reescribir en «Propuesta»; lo cambiado queda en amarillo y la flecha ↺ devuelve esa casilla a como estaba. En «Propuesta» toma el cuatrimestre y el bimestre de la propuesta guardada y resalta en amarillo lo que cambia respecto de la planilla. Se imprime en PDF. |
| Correlativas | Mapa de dependencias. Al elegir una materia marca de qué depende y qué habilita. |
| Horas | Horas por año según campo de formación, régimen de acreditación o teórica/práctica. |
| Calendario | Tabla de períodos lectivos para SIU Guaraní y el calendario académico con el formato de la resolución oficial (Anexo Único). Se imprime en PDF. |

## Los dos escenarios

- **Planilla actual**: la planilla de correlativas tal cual está.
- **Propuesta**: una bimestral por bimestre en 3.º, 4.º y 5.º año, el Practicantado de octubre
  a junio del año siguiente, y encima los cambios que haga cada persona (cambiar el bimestre o
  las fechas de una materia). Las materias que movió quedan marcadas «tu cambio».
  Las Rotaciones Electivas (6.1 y 6.3) pasan al 13.º cuatrimestre, el medio año que cierra la
  carrera (marzo a junio del año siguiente), porque son parte de la Práctica Final Obligatoria. La
  trimestral (6.3) empieza en la 4.ª semana del cuatrimestre (05/04 en 2027) y termina con él
  (02/07), para tener una sola planilla de resultados de cursada en el SIU; la fecha es editable; en el SIU figura como «Trimestrales del 1.º · cierran con el cuatrimestre».

«Planilla actual» no cambia nunca: si se mueve algo estando ahí, el tablero pasa solo a
«Propuesta».

**Dónde se guarda la propuesta.** Lo que se ajusta en «Propuesta» (bimestres, fechas, texto del
plan) se guarda en el navegador y en la dirección donde se abrió el tablero. El sitio de GitHub
Pages y el artefacto de Claude son dos direcciones distintas, así que cada una tiene su propia
copia y los cambios de una no aparecen en la otra; lo mismo con otro navegador u otra
computadora. Nada se borra: para llevar la propuesta de un lado al otro están «Guardar copia»
(descarga un .json) y «Cargar copia».

**Cambios manuales que esconden un período.** Un cambio cargado a mano manda sobre la propuesta.
Si ese cambio mueve la única materia que ocupaba un período (por ejemplo, la trimestral), ese
período deja de figurar en el cuadro de SIU y en el calendario. Arriba del cuadro aparece un
aviso que lo dice y ofrece «Volver a la propuesta» para esa materia. Si una materia queda en
fechas que no coinciden con ningún período, se lista aparte en el cuadro bajo «Sin período
lectivo», así nunca queda invisible.

**Fechas cargadas a mano y la barra del diagrama.** La barra ocupa meses enteros, así que un mes
del borde cuenta solo si la materia lo cubre más o menos hasta la mitad: una materia que termina
el 02/07 llega hasta junio y no pinta julio, y una que empieza el 20/04 arranca en mayo. La fecha
exacta se lee al lado del nombre y es la que va al plan, al SIU y a los PDF.

## Solo lectura en el sitio publicado

El tablero se abre en **modo lectura**: se puede mirar, filtrar e imprimir, pero el botón
«Editar» no aparece y ningún campo se puede escribir. Para habilitar la edición en una
computadora se abre una vez con `?editar` al final de la dirección:

    https://medicina-unju.github.io/planEstudio-medicina/?editar

Queda recordado en ese navegador. Para volver a bloquearlo, `?editar=no`. El pie de la página
dice en qué modo está.

Es un recaudo para que nadie toque sin querer, **no una contraseña**: todo el código viaja al
navegador de quien abre la página, así que quien sepa buscarlo puede habilitar la edición igual.
De todos modos, lo que cualquiera edite queda solo en su navegador y no afecta al archivo
publicado ni a la propuesta de nadie más.

**Lo que ve el público es la propuesta que trae el archivo**, no los cambios guardados en un
navegador. Para que una propuesta armada a mano se publique, hay que incorporarla al archivo
(exportarla con «Guardar copia» y regenerar `index.html`).

Abajo de todo figura la **versión** del archivo (fecha y hora de compilación): sirve para
confirmar que el navegador no está mostrando una copia vieja en caché.

## Copia de seguridad

Lo que se cambia queda guardado en el navegador. Para llevarlo a otra computadora o pasárselo
al equipo: **Guardar copia** descarga un archivo con la propuesta y las fechas; en el otro
navegador, **✎ Editar → Cargar copia** y después **Guardar cambios**.

## Editar y guardar

Los campos están bloqueados para no cambiar nada sin querer. Para modificar algo:

1. **✎ Editar**, arriba a la derecha.
2. Cambiar lo que haga falta: el bimestre de una materia o sus fechas (en el panel de detalle),
   o cualquier fecha del calendario.
3. **✓ Guardar cambios**, o **Descartar** para volver a como estaba al tocar Editar.

Mientras se edita también están **Deshacer** (de a un cambio, incluso después de cerrar el
navegador) y **Borrar mis cambios** (también se puede deshacer). La etiqueta «movida» indica una
diferencia con la planilla actual; «tu cambio», una diferencia con la propuesta base.

## Correlativas modificadas en la propuesta

En «Propuesta» rigen estas correlativas (la planilla original no se toca; en el plan se ven
en amarillo, con el valor original al pasar el mouse):

| Espacio | Planilla | Propuesta | Motivo |
| --- | --- | --- | --- |
| 3.1 Introducción a la Clínica | 2.3 aprobada | — | Alcanza con 2.1 y 2.2 regulares |
| 3.2 Patología General | 2.3 aprobada | — | ídem |
| 3.3 Bases para el Diagnóstico I | 2.3 aprobada | — | ídem |
| 3.5 Relaciones Humanas II | 2.5 aprobada | 2.5 regular | Flexibilización de la línea RH |
| 4.3 Bases para el Diagnóstico II | 3.3 aprobada | 3.3 regular | Alcanza con tenerla regular, como ya pide 3.4 |
| 4.5 Relaciones Humanas III | 3.5 aprobada | 3.5 regular | Flexibilización de la línea RH |
| 6.5 Practicantado Rotatorio | Todo aprobado | Todas las de 1.º a 5.º año y 6.4 aprobadas, y 6.2 regular | 6.4 cierra el 02/07 y llega con el final rendido; 6.2 queda regular porque ahí está Medicina General y Familiar |
| 6.1 Rotaciones Electivas I | 5.1 - 5.2 - 5.3 - 5.4 regulares | 6.5 en curso | Se cursan dentro de la PFO (apartado 10 de la Res. 093-25) |
| 6.3 Rotaciones Electivas II | 5.1 - 5.2 - 5.3 - 5.4 regulares | 6.5 en curso | ídem |

2.5 vuelve a pedir 1.3, 1.4, 1.5 y 2.3 regulares, y 5.2, 5.3 y 5.5 vuelven a pedir 3.3 aprobada,
como en la planilla.

Las correlativas se pueden editar a mano en modo edición, desde la casilla de la pestaña «Plan
completo» o desde el panel de detalle de cada materia. Lo escrito se guarda con la propuesta,
entra en «Guardar copia» y se ve en todas las pestañas.

## Bimestres en el diagrama

En la Secuencia cada bimestre ocupa siempre sus dos meses (1.er marzo-abril, 2.º mayo-junio,
3.er agosto-septiembre, 4.º octubre-noviembre), aunque la fecha precisa termine unos días en el
mes siguiente (por ejemplo, el 1.er bimestre 2027 va del 15/03 al 07/05). La fecha exacta sale
del calendario y es la que figura en el plan, en la tabla de SIU y en el PDF; aparece también al
pasar el mouse por la barra. El bimestre de cada materia se identifica por su lugar, no por los
meses: cambiar el mes de inicio de una bimestral la pasa al bimestre que corresponde, y cargarle
una fecha a mano la ubica en el bimestre que contiene esa fecha.

## Calendario académico

La pestaña **Calendario** estima el ciclo a partir del Calendario Académico 2026
(Res. CAESS N.º 06/2026). Cada hito del calendario oficial cae en una semana fija respecto del
inicio de su cuatrimestre; se verificó que con esas posiciones se reproducen exactamente todas
las fechas de 2026, y se aplicaron las mismas al ciclo siguiente.

Tiene dos partes:

- **Períodos lectivos para SIU Guaraní**: una fila por período (anual, cuatrimestres, bimestres,
  semestral, Práctica Final Obligatoria), con las cinco etapas en orden: inscripción a materias,
  período lectivo, carga de resultados de cursada por los docentes, inscripción a la mesa de
  examen y mesa de examen. Cada período queda enlazado con el primer turno al que llegan los
  alumnos una vez cerrada el acta de cursada.
- **El calendario con el formato de la resolución** (Anexo Único): primer cuatrimestre, receso,
  segundo cuatrimestre, turnos de examen y feriados, con los mismos rótulos que el oficial y
  los agregados de Medicina (bimestres y matriculación en el aula virtual).

En modo edición todas las fechas son editables, y lo que depende de ellas se recalcula.

**Coherencia de fechas.** Cada fecha se guarda una sola vez, así que se ve igual en el cuadro de
SIU, en el calendario con formato de resolución, en el plan y en los PDF. Al cambiar una se
mueven las que dependen de ella:

- El inicio del 1.er bimestre es el inicio del 1.º cuatrimestre, y el fin del 2.º bimestre es el
  fin del cuatrimestre (lo mismo para el 3.º y el 4.º con el 2.º cuatrimestre). Si se corre el fin
  de un bimestre, el siguiente empieza el día hábil posterior.
- Al cambiar el último día de inscripción a materias, los dos días de cierre y aula virtual se
  corren con él, y la inscripción de ingresantes acompaña a la inscripción a materias.
- Al mover la semana de examen de un turno, su inscripción, el último día de borrado y la
  generación del acta se recalculan sobre ella.
- Al cambiar el fin de un cuatrimestre se corren la planilla de resultados, la renuncia de
  regularidad y las jornadas posteriores, y cada período vuelve a enlazarse con el primer turno
  al que llega. La planilla de resultados que comparten varios períodos se edita en un solo lugar.
- Un cuadro de **control de fechas** arriba del SIU avisa si alguna fecha cargada a mano contradice
  a otra (por ejemplo, una generación del acta que llega a la semana de examen).

**Regla administrativa** (definida por la coordinación): la inscripción, a materias y a
exámenes, dura **cinco días hábiles corridos** —por defecto, de jueves a miércoles— y deja libres los **dos días hábiles siguientes** (por defecto, jueves y viernes)
para cerrar el acta, descargar la lista definitiva, procesarla y matricular en el aula virtual.
Hasta el miércoles los alumnos pueden darse de baja; el lunes la mesa o el cursado arrancan con
la lista definitiva. Si cae un feriado, la ventana se corre hacia atrás y se mantienen los cinco
días de inscripción y los dos de margen.

**Ingresantes.** Se inscriben en la misma ventana que las materias (para 2027, del 04/03 al
10/03) y se los matricula en el aula virtual en los mismos dos días hábiles. La jornada de
ambientación y las clases inaugurales se superponen con las primeras semanas de dictado; las
fechas exactas las define la Escuela y en el tablero son editables.

**Ciclo lectivo.** El calendario 2026 fija el inicio del ciclo 2027 el 15/03/2027, que es la
misma fecha que da la estimación.

**Borrado y acta.** El Art. 27 del Reglamento (Res. C.S. N.º 066-22) deja el plazo de borrado al
Calendario Académico. Criterio aplicado: el estudiante puede borrarse de la mesa hasta dos días
hábiles antes de la fecha de examen (para un examen del lunes, hasta el jueves), y el acta
volante se genera un día hábil antes del turno (el viernes), para que los docentes consulten la lista
definitiva de estudiantes inscriptos. Ambas fechas se calculan desde el primer día de examen del turno, con feriados.

**13.º cuatrimestre.** La carrera dura seis años y medio: después del 6.º año hay medio año más,
que es el 1.º cuatrimestre del 7.º año (marzo a junio del año siguiente). El diagrama lo dibuja a
la derecha, separado por el verano. Ahí van las Rotaciones Electivas I y II y el cierre de la
Práctica Final Obligatoria. No entra en el cuadro de SIU de este ciclo —se carga en el del ciclo
siguiente—, así que figura como nota debajo del cuadro.

**Correlativas para cursar y para rendir.** El plan distingue tres condiciones para cursar
—aprobada, regular y en curso (cursada simultánea)— y una para rendir. Son las mismas que usa
SIU Guaraní en «Asignar correlativas», así que la tabla del plan se puede cargar tal cual.
El Practicantado (6.5) pide todas las de 1.º a 5.º año aprobadas y 6.2 regular para cursar, y
toda la carrera aprobada para rendir el final integrador (Art. 22 del reglamento de PFO).
Las Rotaciones Electivas piden 6.5 en curso y nada más: el control de 1.º a 5.º año queda en un
solo lugar. Sus finales no piden la carrera completa; si la pidieran, no podrían aprobarse nunca,
porque el final de 6.5 exige tenerlas aprobadas.

**Encabezado fijo y columna ajustable.** El diagrama tiene su propio desplazamiento: el
encabezado (período, inscripción y meses) y la columna de espacios curriculares quedan fijos
mientras se recorren los años. El borde derecho de esa primera columna se arrastra para
cambiar su ancho, entre 120 y 560 px; el valor queda guardado en ese navegador y no viaja en
la propuesta.

**Columna de nombres y desplazamiento.** El nombre de cada espacio se ve entero: pasa a dos
líneas en lugar de cortarse. Cuando se muestra 6.º año aparecen las cinco columnas del 13.º
cuatrimestre y el diagrama se desplaza de costado, para que los meses conserven su ancho en
lugar de achicarse. De 1.º a 5.º año esas columnas no existen y entra todo sin desplazamiento.

**Módulos de la PFO.** El filtro «Ver los módulos de la PFO» abre, debajo del Practicantado,
los seis módulos del Art. 1 del reglamento (Res. C.S. 095-25): Clínica Médica, Quirúrgica,
Pediátrica, Gineco-Obstétrica, Psiquiatría y Salud Mental, y Emergencias. Cada uno son 214 h:
90 de guardia y 82 de concurrencia al servicio (80% práctica), más 30 de clases teóricas y 12 de
estudio y preparación (20% teórica). Se reparten en partes iguales sobre el tramo de la PFO,
porque el orden de las especialidades no está fijado; con el tramo de octubre a junio dan unas
6,5 semanas cada uno, contra las diez del Art. 17. Las Rotaciones Electivas I y II corren en
paralelo, dentro del mismo tramo.

**Navegadores.** La página usa `replaceChildren` y `flatMap`, que no están en los navegadores
anteriores a 2020 (tablets con Chrome o WebView viejo, iPad con iOS 13). Las dos tienen un
reemplazo propio al inicio del script, y si aun así algo falla al arrancar, la página muestra un
cartel con el detalle del error en vez de quedar en blanco.

**Panel de detalle.** En pantalla ancha, la lengüeta del borde izquierdo del panel lo esconde y
lo vuelve a mostrar; con el panel escondido, el diagrama ocupa todo el ancho. Si hay una materia
elegida mientras está escondido, la lengüeta queda marcada.

**Columna de nombres.** El filtro «Angostar la columna de nombres» deja solo el código de cada
espacio y le da el ancho ganado a los meses: sirve para ver todo el año y el 13.º cuatrimestre
sin desplazarse, sobre todo en el celular.

**Carga estimada por mes.** Las horas totales de cada espacio se reparten entre sus meses de
cursada (julio no cuenta: es el receso). El Practicantado Rotatorio se reparte sobre todo su
tramo, de octubre a junio del año siguiente, así que parte de sus horas cae fuera del ciclo.
La carga por cuatrimestre es la suma de esa carga mensual: de febrero a julio y de agosto a
diciembre.

**Planilla de resultados.** Para los cuatrimestres se toman las fechas del calendario oficial;
para bimestres y semestral, la semana hábil siguiente a su cierre.

Los días no laborables con fines turísticos los fija el Poder Ejecutivo por decreto y no estaban
publicados al armar esta estimación, así que no están descontados.

## Imprimir

El botón **Imprimir** arma una versión para papel o PDF del escenario que se esté viendo: la
secuencia de cada año en una hoja apaisada, la tabla de cambios respecto de la planilla con su
fundamento, las propuestas sobre correlatividades, las inconsistencias y el calendario académico. En el diálogo de impresión se puede elegir
«Guardar como PDF». Conviene hacerlo desde el sitio de GitHub Pages: dentro de la vista previa
de Claude el navegador puede bloquear la impresión.

## Cómo se ubican las bimestrales

El año tiene cuatro bimestres, con fechas fijas tomadas del calendario académico:

| Bimestre | Cursada | Cuatrimestre |
| --- | --- | --- |
| 1.er bimestre | 16/03 al 08/05 | 1.º |
| 2.º bimestre | 07/05 al 03/07 | 1.º |
| 3.er bimestre | 10/08 al 30/09 | 2.º |
| 4.º bimestre | 01/10 al 27/11 | 2.º |

El plan marca las materias como «B» pero no fija en cuál de los cuatro van. En la planilla
actual todas caen al final de su cuatrimestre y quedan en paralelo (hasta tres a la vez en
4.º y 5.º año).

La **propuesta** ubica una por bimestre, sin paralelismo, como si las bimestrales de cada año
formaran un anual en cuatro tramos. Para elegir el bimestre se miró:

- **Correlativas**: cuándo termina la materia previa y cuántos turnos de examen quedan antes
  de la ventana de inscripción (04-10/03 para el 1.er cuatrimestre, 28/07-03/08 para el 2.º).
- **Turnos de examen**: cada bimestre rinde en un turno distinto (junio, julio, octubre y
  diciembre), así que una por bimestre reparte los finales.
- **Carga mensual** del resto del año y afinidad de contenidos (Res. C.S. N.º 093-25).

| Año | 1.er bim. | 2.º bim. | 3.er bim. | 4.º bim. |
| --- | --- | --- | --- | --- |
| 3.º | — | — | 3.6 | 3.5 |
| 4.º | 4.4 | 4.6 | 4.7 | 4.5 |
| 5.º | 5.4 | (libre, sugerido para el optativo IV) | 5.5 | 5.7 |

6.º año no tiene bimestrales. 1.º y 2.º año siguen como en la planilla hasta incorporar lo
que trabajó la coordinación. Cualquiera se puede cambiar de bimestre desde el panel de detalle, en modo edición: toma las fechas
predefinidas del bimestre nuevo y la barra del diagrama se corre sola.

## Publicarlo en GitHub Pages

1. Crear un repositorio y subir `index.html`, `data.json` y este `README.md` a la raíz.
2. En **Settings → Pages**, elegir *Deploy from a branch*, rama `main`, carpeta `/ (root)`.
3. A los pocos minutos queda en `https://<usuario>.github.io/<repositorio>/`.

`index.html` es autosuficiente: trae los datos adentro. **Para actualizar el sitio alcanza con
reemplazar `index.html`**; `data.json` y este README quedan en el repositorio como documentación
y como fuente para regenerar el HTML, pero la página no los lee.

## Cambiar los datos

En `data.json`, cada espacio curricular es un objeto con estos campos:

```json
{
  "anio": 2,
  "codigo": "2.3",
  "nombre": "Salud Poblacional I",
  "dur": "B",
  "cuat": 1,
  "cf": "FBC",
  "cursado": "Presencial",
  "hs": 40, "teo": 20, "pra": 20,
  "apr": ["1.2"],
  "reg": ["1.3", "1.4", "1.5"],
  "regimen": "Examen final",
  "base": { "ini": 5, "fin": 6, "sr": false, "flex": false },
  "prop": { "ini": 3, "fin": 4, "sr": false, "flex": false },
  "propRazon": "Abre el año: continúa en forma directa 1.2…"
}
```

- `dur`: `A` anual, `S` semestral, `C` cuatrimestral, `T` trimestral, `B` bimestral.
- `cf`: `FBC` formación básica y clínica, `FO` formación optativa, `PFO` práctica final obligatoria.
- `base` y `prop`: ventana de cursada de cada escenario. `ini` y `fin` son números de mes (2 = febrero).
  `sr: true` significa que se cursa también en julio. `flex: true` lo dibuja rayado, a elección del estudiante.
- `apr` y `reg`: códigos de las correlativas aprobadas y regulares.

Los bloques `sugerencias` e `inconsistencias` aparecen en el panel de cada materia y en el PDF
«Imprimir todo».

## Fechas para SIU Guaraní

Están en la pestaña **Calendario** (ver arriba). Cada espacio tiene además, en el panel de
detalle, dos campos de fecha (inicio y fin) para cargar la fecha definitiva cuando esté
acordada; mientras no se cargue, se usa la estimada.

## Fuentes

- Planilla de correlativas de la carrera (archivo `CORRELATIVAS.xlsx`).
- Res. C.S. N.º 0191-24: creación de la carrera y aprobación del plan de estudios.
- Res. C.S. N.º 093-25: modificación del plan de estudios. De ahí salen las horas teóricas
  y prácticas, los contenidos mínimos y el régimen de espacios optativos.
- Res. CAESS N.º 06/2026: Calendario Académico 2026 de la Escuela Superior de Salud.
- Res. CAESS N.º 09/2026: ampliación del calendario para Medicina, con el cronograma real
  de los cinco espacios de 1.º año (es la fuente del criterio de bimestrales en paralelo).
- Res. C.S. N.º 066-22: Reglamento Académico de Regímenes de Cursado, Aprobación de Materias
  y Condición de Alumnos de las Escuelas Superiores.

## Punto abierto sobre el régimen de cursada

El Art. 5.º del Reglamento 066-22 establece que la inscripción por materia se hace «teniendo
en cuenta las correlativas y demás requisitos que estableciera el Plan de Estudios». La única
flexibilización que aparece es el Art. 29.º, y es acotada: quien rindió seis veces la
correlativa anterior sin aprobarla, pero sigue regular en ella, puede inscribirse en la
materia siguiente e incluso regularizarla, pero no rendir su final hasta aprobar la anterior.
No encontramos un artículo general que habilite inscribirse sin la correlativa cumplida.
De eso depende la salida propuesta para el Practicantado (6.5), así que conviene confirmar
la norma exacta antes de llevar esa redacción a la comisión.

## Advertencia

Las fechas son una estimación construida sobre el calendario académico 2026, para discutir
la organización del dictado. No son un calendario académico aprobado para el plan nuevo.

## Dependencia externa

Para generar los archivos Excel, la página carga
[SheetJS](https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js) desde cdnjs.
Sin conexión, el resto del tablero funciona igual y solo quedan sin generarse los Excel.
