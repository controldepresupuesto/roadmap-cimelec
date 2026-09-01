# Plataforma CIMELEC — estado y hoja de ruta

## 👉 [ABRIR LA HOJA DE RUTA](https://github.com/users/controldepresupuesto/projects/1)

*El tablero está ahí, no en este repositorio. Se abre sin cuenta.*

---

Aquí se publica **en qué estamos trabajando, qué acaba de salir y qué viene** en las
herramientas internas del grupo CIMELEC INGENIEROS (CIMELEC, CIMELCON, INGEOCHO,
INNOMACH y consorcios).

Este repositorio **no contiene código**. Es la vitrina: el tablero, el historial de
versiones y el registro de solicitudes. El código vive en repositorios privados.

> 🔒 **Solo lectura.** Cualquiera puede consultar esta página y el tablero. Escribir
> (abrir una solicitud, comentar) está reservado al equipo. Si trabajas en el grupo y
> necesitas pedir algo, mira [Cómo pedir un cambio](#cómo-pedir-un-cambio).

---

## Qué hay en el tablero

Cada tarjeta es una solicitud, y trae tres datos que se leen de un
golpe:

| Campo | Qué dice |
|---|---|
| **Status** | En qué va, de *en evaluación* a *publicado* — la tabla completa más abajo |
| **Herramienta** | A qué app pertenece — cada una con su icono y su color, para reconocerla sin leer |
| **Prioridad** | Alta, media o baja — la fija la dirección, no el orden de llegada |
| **Periodo** | En qué trimestre está previsto |

Arriba del tablero hay pestañas para verlo de varias formas:

- **General** — todo en una tabla, para buscar y ordenar
- **Por estado** — columnas por etapa: qué está en desarrollo hoy, qué está en pruebas
- **Hoja de ruta** — línea de tiempo por trimestre
- **Una pestaña por herramienta** — solo lo de esa app

Cada app tiene icono y color propios, y se repiten en todas las vistas:

| | App | | App |
|---|---|---|---|
| 📊 | Tablero DataMart | 📚 | Biblioteca de Informes |
| 📓 | Bitácora de Obra | 🌎 | Consulta Geográfica |
| ⏰ | Registro de Horarios | 💬 | Asistente |
| 🚚 | Portal de Proveedores | 🏠 | Menú de entrada |
| 📋 | Gestión de Proyectos | 🔧 | Plataforma (varias a la vez) |

---

## Las herramientas

| Herramienta | Para qué es | Quién la usa |
|---|---|---|
| **Tablero DataMart** | Indicadores del ERP: presupuesto, compras, contratos, nómina, contabilidad | Dirección, control de presupuesto, residentes |
| **Bitácora de Obra** | Informes diarios de obra, avance por ítem, biblioteca de registros | Residentes, interventoría, dirección de obra |
| **Registro de Horarios** | Marcación de asistencia, horas extra, permisos y novedades de nómina | Todo el personal |
| **Portal de Proveedores** | Alta y actualización de proveedores con sus documentos | Compras, proveedores externos |
| **Gestión de Proyectos** | Seguimiento de proyectos y entregables | Dirección, coordinación |
| **Biblioteca de Informes** | Informes publicados con enlace para compartir | Oficina |
| **Consulta Geográfica** | Malla vial de Bogotá: verificación de CIV, vías y localidades | Obra, topografía |
| **Asistente de consulta** | Consultas de datos y documentos por WhatsApp | Oficina, obra |

Los enlaces de acceso están en el menú interno de la empresa; no se publican aquí.

---

## Cómo leer los estados

El campo se llama `Status` (así lo nombra GitHub y no se puede cambiar). Una solicitud
recorre estas etapas, en este orden:

| Estado | Qué significa |
|---|---|
| ⚪ **En evaluación** | Recibido. Estamos validando si entra en los planes. Sin compromiso de fecha |
| 🔵 **En backlog** | Aceptado y priorizado, todavía sin empezar |
| 🟣 **En desarrollo** | Se está construyendo ahora |
| 🟡 **En pruebas** | Construido, en verificación antes de publicarlo |
| 🟠 **En implementación** | Ya salió, y está en marcha con algunas áreas antes que con todas |
| 🟢 **Publicado** | Es parte de las herramientas y cualquiera lo usa |
| 🩷 **Pausado** | Detenido a propósito. El motivo está escrito en la solicitud |
| 🔴 **No va** | Se decidió no hacerlo. El motivo está escrito en la solicitud |

Las dos últimas se publican a propósito. Una lista donde todo lleva años "en evaluación" no
dice nada; saber que algo **no** se va a hacer, y por qué, sirve tanto como saber que sí.

Una solicitud **cerrada** puede estar cerrada por *Publicado* o por *No va*. El estado manda,
no el hecho de estar cerrada.

## Cuándo, no qué día

El tablero no promete fechas exactas: promete **trimestres**. El campo `Periodo` dice en qué
trimestre está previsto algo (`2026 T4 Oct - Dic`, por ejemplo), y la vista **Hoja de ruta**
lo dibuja en línea de tiempo. Un trimestre es una promesa que se puede cumplir; una fecha
exacta a seis meses vista, no.

Una solicitud sin `Periodo` es una que todavía no tiene cuándo — normalmente porque está en
evaluación o en backlog.

## Por temas

Además de la herramienta, cada solicitud lleva etiquetas de **tema** que cruzan todas las
apps: `informes`, `móvil`, `integraciones`, `automatización`, `inteligencia artificial`,
`datos y cifras`, `accesos`, `obra`, `nómina`, `compras`, `contabilidad`, `documentos`.
Sirven para responder "¿qué se está haciendo en materia de X?" sin importar en qué app.

## Cómo pedir un cambio

**Si tienes cuenta de GitHub y estás en el equipo** — abre una solicitud con el
formulario que corresponda:

- 🐞 [Reportar un error](../../issues/new?template=02-error.yml)
- ✨ [Pedir una mejora](../../issues/new?template=01-mejora.yml)
- 💡 [Proponer una idea](../../issues/new?template=03-idea.yml)

**Si no tienes cuenta** — pídelo como siempre (WhatsApp o correo al área de control de
presupuesto). La solicitud se registra aquí igual, con tu nombre como solicitante, y
puedes seguirla por el enlace que te devolvemos.

No hace falta que escribas bien el problema técnico. Con que se entienda **qué estabas
haciendo, qué esperabas y qué pasó** es suficiente.

---

## Actualizaciones

Cada publicación queda con su nota de versión:

- 📋 [Historial completo](CHANGELOG.md)
- 🏷️ [Versiones publicadas](../../releases)

---

## Preguntas frecuentes

**¿Por qué mi solicitud no tiene fecha?**
Porque está en *Idea* o *En análisis*. La fecha aparece cuando pasa a *En curso*.

**¿Puedo saber en qué orden se hacen las cosas?**
Sí: en el tablero, ordenado por prioridad. La prioridad la fija la dirección, no el
orden de llegada.

**¿Esto reemplaza al ERP SINCO?**
No. Todas estas herramientas **leen** del ERP o le **cargan** información. El ERP sigue
siendo el sistema de registro.

**¿Por qué no puedo comentar?**
El repositorio es público para que cualquiera lo consulte, pero cerrado a escritura de
terceros. Si estás en el equipo y necesitas acceso, pídelo al área de control de
presupuesto.

---

<sub>Mantenido por el área de Control de Presupuesto · CIMELEC INGENIEROS</sub>
