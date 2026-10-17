# Plan de estudios de Medicina — Escuela Superior de Salud, UNJu

Tablero web para trabajar la secuencia de cursada, las correlatividades y las cargas horarias
de la carrera de Medicina (Res. C.S. N.º 0191-24 y su modificación, Res. C.S. N.º 093-25).

Es una sola página, sin backend ni instalación. Se puede publicar en GitHub Pages y compartir por enlace.

## Qué hay en cada pestaña

| Pestaña | Para qué sirve |
| --- | --- |
| Secuencia | Diagrama mes a mes por año o por conjuntos de años. Muestra cuántos espacios corren en simultáneo y cuántas horas suman. |
| Orden de bimestrales | Propuesta de ubicación de cada materia bimestral, con el motivo. Se puede mover cualquiera a otro bimestre. |
| Plan completo | Tabla filtrable con códigos, duración, campo de formación, horas y correlativas. |
| Correlativas | Mapa de dependencias. Al elegir una materia marca de qué depende y qué habilita. |
| Horas | Horas por año según campo de formación, régimen de acreditación o teórica/práctica. |
| Calendario | Calendario académico estimado del ciclo: inscripciones, cursada, receso, turnos de examen y feriados, más la fecha de cada espacio curricular. Se configura desde ahí. |
| Descargas | Excel con siete hojas (incluye el calendario académico), Excel de fechas para SIU Guaraní, imagen de la secuencia (PNG y SVG) y la configuración en JSON. |

## Los dos escenarios

- **Planilla actual**: la planilla de correlativas tal cual está.
- **Propuesta**: ubica una bimestral por bimestre en 3.º, 4.º y 5.º año, sin paralelismo, y
  pone el Practicantado Rotatorio de agosto a junio del año siguiente.

- **Mi propuesta**: una bimestral por bimestre en 3.º, 4.º y 5.º año, más los cambios que haga
  cada persona en el tablero (arrastrar una bimestral, cambiar meses o cargar fechas). Las
  materias que movió quedan marcadas «tu cambio».

«Planilla actual» no cambia nunca: si se mueve algo estando ahí, el tablero pasa solo a
«Mi propuesta».
La etiqueta «movida» indica una diferencia con la planilla actual; «tu cambio», una diferencia
con la Propuesta. En la barra del escenario están **Deshacer** (vuelve atrás de a un cambio,
incluso después de cerrar el navegador), **Borrar mis cambios** (también se puede deshacer)
e **Imprimir**. La pestaña Orden de bimestrales tiene además una lista «Tus cambios» con un
botón para volver atrás cada materia por separado.

## Calendario académico

La pestaña **Calendario** estima el ciclo completo a partir del Calendario Académico 2026
(Res. CAESS N.º 06/2026): mantiene la misma posición del año y corre cada hito al lunes o
viernes que corresponde. Incluye inscripciones, cursada de cada período, receso, ocho turnos
de examen, feriados y la fecha de cada espacio curricular.

**Regla administrativa aplicada** (definida por la coordinación): la inscripción —a materias y
a exámenes— abre el lunes de la semana anterior y cierra dejando **dos días hábiles libres**.
Esos dos días son para cerrar el acta, descargar la lista definitiva, procesar las inscripciones
por sistema y matricular en el aula virtual. El cursado o la mesa arrancan el lunes siguiente
con la lista ya cerrada. Normalmente el margen cae jueves y viernes; si alguno es feriado, se
corre hacia atrás y la inscripción se acorta.

Los días hábiles que informa cada período descuentan fines de semana, feriados y el receso de
invierno. Los feriados nacionales salen de la Ley 27.399, con los trasladables ya corridos al
lunes que corresponde. Los **días no laborables con fines turísticos** los fija el Poder
Ejecutivo por decreto y no estaban publicados al armar esta estimación, así que no están
descontados.

En **Configuración del ciclo** se editan el año, los dos cuatrimestres, el receso y los cuatro
bimestres. Todo lo demás se recalcula a partir de eso: semanas de inscripción, días de proceso,
turnos de examen y fechas de cada materia. Si una bimestral se mueve de bimestre, toma las
fechas del bimestre nuevo; si además cambia de cuatrimestre, le cambia la semana de inscripción.

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
que trabajó la coordinación. Cualquiera se puede cambiar de bimestre arrastrándola del
tirador ⠿ en la pestaña Orden de bimestrales, o con el selector de esa pestaña y del panel
de detalle: toma las fechas predefinidas del bimestre nuevo y la barra se corre sola.

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

Los bloques `sugerencias` e `inconsistencias` alimentan la pestaña Revisión.

## Compartir los cambios del equipo

Lo que cada persona ajusta en el tablero (orden de bimestrales, fechas, ciclo lectivo)
se guarda en su navegador y no viaja con el enlace. Para compartirlo:

1. **Descargas → Descargar configuración (JSON)**.
2. Subir ese archivo al repositorio o pasarlo al equipo.
3. Cada persona lo carga con **Descargas → Cargar configuración**.

## Fechas para SIU Guaraní

Las fechas estimadas salen del Calendario Académico 2026 de la Escuela Superior de Salud
(Res. CAESS N.º 06/2026) y de su ampliatoria para Medicina (Res. CAESS N.º 09/2026):

| Período | Inscripción | Cursada |
| --- | --- | --- |
| 1.º cuatrimestre (16 semanas) | 09/03 al 13/03 | 16/03 al 03/07 |
| 2.º cuatrimestre (16 semanas) | 03/08 al 07/08 | 10/08 al 27/11 |

- Semestral: 16/03 al 11/09, como Ciencias Biológicas este año.
- Bimestral: según el bimestre, 16/03 al 08/05, 07/05 al 03/07, 10/08 al 30/09 o 01/10 al 27/11.
- Receso de invierno 13/07 al 24/07; receso de verano en enero. **En febrero no hay dictado
  de clases**: las fechas de febrero del calendario son de examen y de borrado de inscripción.
- La inscripción es única por cuatrimestre, como lo definió el equipo: una semana a principios
  de marzo para las anuales y todas las del 1.er cuatrimestre, y otra en agosto para el 2.º. El ciclo lectivo y
  ambas semanas se configuran en la pestaña Descargas.

Cada espacio tiene en el panel de detalle dos campos de fecha (inicio y fin) para cargar la
fecha definitiva cuando esté acordada. Mientras no se cargue, se usa la estimada; las cargadas
a mano quedan marcadas como tales en el Excel.

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
