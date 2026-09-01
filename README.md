# Plataforma CIMELEC — estado y hoja de ruta

Aquí se publica **en qué estamos trabajando, qué acaba de salir y qué viene** en las
herramientas internas del grupo CIMELEC INGENIEROS (CIMELEC, CIMELCON, INGEOCHO,
INNOMACH y consorcios).

Este repositorio **no contiene código**. Es la vitrina: el tablero, el historial de
versiones y el registro de solicitudes. El código vive en repositorios privados.

> 🔒 **Solo lectura.** Cualquiera puede consultar esta página y el tablero. Escribir
> (abrir una solicitud, comentar) está reservado al equipo. Si trabajas en el grupo y
> necesitas pedir algo, mira [Cómo pedir un cambio](#cómo-pedir-un-cambio).

---

## El tablero

👉 **[Ver la hoja de ruta](https://github.com/users/controldepresupuesto/projects/1)**

Se abre sin cuenta. Cada tarjeta es una solicitud, y trae tres datos que se leen de un
golpe:

| Campo | Qué dice |
|---|---|
| **Status** | En qué va: idea, en análisis, en curso, en prueba, publicado, pausado o no va |
| **Herramienta** | A qué app pertenece |
| **Prioridad** | Alta, media o baja — la fija la dirección, no el orden de llegada |

En la parte de arriba del tablero hay pestañas para verlo de dos formas: como **tablero**
(columnas por estado) o como **hoja de ruta** (línea de tiempo con la fecha objetivo de
cada entrega).

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

El campo se llama `Status` (así lo nombra GitHub y no se puede cambiar), y sus valores son:

| Estado | Qué significa |
|---|---|
| 💡 **Idea** | Recibido y anotado. Sin compromiso de fecha todavía |
| 🔍 **En análisis** | Se está definiendo el alcance y estimando |
| 🔨 **En curso** | Alguien lo está construyendo ahora |
| 🧪 **En prueba** | Construido, en verificación antes de publicarlo |
| ✅ **Publicado** | Ya está en producción y se puede usar |
| ⏸️ **Pausado** | Detenido a propósito. En la solicitud está el motivo |
| ❌ **No va** | Se decidió no hacerlo. En la solicitud está el motivo |

Una solicitud **cerrada** puede estar cerrada por *Publicado* o por *No va*.
El estado manda, no el hecho de estar cerrada.

---

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
