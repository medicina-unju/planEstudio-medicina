# Plan de estudios de Medicina — Escuela Superior de Salud, UNJu

Tablero web para trabajar la secuencia de cursada, las correlatividades y las cargas horarias
de la carrera de Medicina (Res. C.S. N.º 0191-24 y su modificación, Res. C.S. N.º 093-25).

Es una sola página, sin backend ni instalación. Se puede publicar en GitHub Pages y compartir por enlace.

## Qué hay en cada pestaña

| Pestaña | Para qué sirve |
| --- | --- |
| Secuencia | Diagrama mes a mes, filtrable por año y por período con casillas (1.º cuatrimestre: anuales, cuatrimestrales, 1.er y 2.º bimestre, semestrales; 2.º cuatrimestre: cuatrimestrales, 3.er y 4.º bimestre, anuales, semestrales y Práctica Final; anuales y semestrales figuran en los dos porque se inscriben en marzo y cierran el acta en el 2.º). Abajo, el seguimiento de actas por turno, del 1.º al 8.º: en cada turno, qué materias llegan por primera vez y cuándo cierra su acta de cursada. |
| Plan completo | El plan con el mismo formato de la planilla de correlativas (Excel). En «Mi propuesta» toma el cuatrimestre y el bimestre de la propuesta guardada y resalta en amarillo lo que cambia respecto de la planilla. Se imprime en PDF. |
| Correlativas | Mapa de dependencias. Al elegir una materia marca de qué depende y qué habilita. |
| Horas | Horas por año según campo de formación, régimen de acreditación o teórica/práctica. |
| Calendario | Tabla de períodos lectivos para SIU Guaraní y el calendario académico con el formato de la resolución oficial (Anexo Único). Se imprime en PDF. |

## Los dos escenarios

- **Planilla actual**: la planilla de correlativas tal cual está.
- **Mi propuesta**: una bimestral por bimestre en 3.º, 4.º y 5.º año, el Practicantado de agosto
  a junio del año siguiente, y encima los cambios que haga cada persona (cambiar el bimestre o
  las fechas de una materia). Las materias que movió quedan marcadas «tu cambio».

«Planilla actual» no cambia nunca: si se mueve algo estando ahí, el tablero pasa solo a
«Mi propuesta».

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

**Regla administrativa** (definida por la coordinación): la inscripción, a materias y a
exámenes, abre el lunes de la semana anterior y cierra dejando **dos días hábiles libres**
para cerrar el acta, descargar la lista definitiva, procesarla y matricular en el aula virtual.
El cursado o la mesa arrancan el lunes con la lista cerrada. Si cae un feriado, el margen se
corre hacia atrás.

**Período de borrado.** El calendario 2026 lo extendía hasta 48 h antes del examen, lo que
permitiría bajarse de la mesa hasta el sábado y abriría el acta ya cerrada. El Art. 27 del
Reglamento (Res. C.S. N.º 066-22) deja ese plazo al Calendario Académico, así que en la
estimación 2027 el borrado cierra con la inscripción. Es un cambio de criterio respecto de 2026
que tiene que aprobar la comisión.

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
  de la semana de inscripción (09-13/03 para el 1.er cuatrimestre, 03-07/08 para el 2.º).
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

La página carga primero los datos que trae embebidos y después intenta leer `data.json`.
Si el archivo está, manda `data.json`. Así se pueden corregir los datos sin tocar el HTML.

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
