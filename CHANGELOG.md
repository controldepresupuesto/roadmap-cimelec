# Historial de actualizaciones

Lo que ha salido a producción, de lo más reciente a lo más viejo.
Redactado para quien usa la herramienta, no para quien la programa.

Formato de cada entrada: **✨ Nuevo** · **🔧 Mejorado** · **🐞 Corregido** · **⚠️ Cambio de comportamiento**

---

## 2026-09-02

**Registro de Horarios**
- ⚠️ La firma dejó de ser opcional: el primer ingreso pide correo, clave propia y firma, y no deja
  registrar nada hasta completarlas. Si la firma falta o se borra, la app vuelve a pedirla. Antes
  había días confirmados que se imprimían con la casilla de la firma en blanco.
- 🐞 El día registrado desde el calendario quedaba en el centro de costo base del empleado y no en
  el que correspondía. Ahora el centro se elige al registrar, también al marcar varios días de una
  vez, y cada opción dice si ese día ya tiene jornada en ese centro.
- 🔧 El turno se elige en el momento de marcar: quien tiene turno diurno y trabajó de noche ya no
  ve su día liquidado con la cuota del diurno.
- ✨ La segunda jornada se agrega desde el calendario con el día en borrador, sin tener que enviarlo
  y reabrirlo.
- 🔧 La hora se elige en una rueda de hora y minuto, en vez del control del teléfono, que mostraba
  19:30 como «07:30 p. m.».
- 🔧 Mi planilla trae los cortes **21 al 20** y **15 al 14** como atajo, con la misma regla de los
  informes.
- 🐞 «Ver detalle» de la planilla no abría nada, ni desde el botón ni desde la fila, y tampoco
  avisaba del error.
- 🐞 El resumen del mes contaba dos veces el día que tiene jornada y novedad a la vez: decía «4 de
  31» habiendo 2 días.
- 🔧 En el celular, el cuadro de la firma guardaba el trazo estirado y en tema claro no se veía
  dónde firmar.

**Portal de Proveedores**
- 🔧 En el teléfono, las tablas de Órdenes, Facturas, Actas y Contratos se leen como tarjetas: con
  las siete columnas de Órdenes había que arrastrar de lado, y lo que quedaba fuera era justo el
  total y el pendiente.
- 🔧 Cuando el ERP rechaza la creación de un tercero, la ficha dice el campo y la regla que lo
  causaron, en vez de «presenta inconsistencias». El botón del paso se queda a la vista, en gris y
  con el motivo.
- 🐞 Un tercero sin cuenta bancaria era rechazado siempre, porque el correo de tesorería viajaba
  solo. Ahora solo se envía cuando la cuenta está completa; el correo sigue viajando en los campos
  donde ya iba.
- 🐞 El enlace a la DIAN nunca había abierto, y el título de una orden descargaba el PDF en vez de
  abrir la ficha.

---

## 2026-09-01

**Menú de entrada**
- ✨ Tarjeta **Hoja de ruta** en el grupo *Sitio público*: desde el menú se puede ver en qué va
  cada desarrollo. Se abre sin cuenta.

**Registro de Horarios**
- 🔧 Las convenciones del calendario: el relleno de la celda dice el estado del día y una banda de
  color dice el tipo de novedad. Antes el dorado era «enviado», domingo y permiso a la vez, y dos
  tipos de novedad se veían del mismo tono.
- 🐞 En el celular las horas del día («8h 30m») se partían en dos renglones y el segundo se cortaba.
- 🐞 Un festivo trabajado nunca mostraba su marca, y a 320 px las celdas del calendario se
  solapaban.

---

## 2026-08-31

**Menú de entrada**
- ✨ El menú de acceso a las herramientas ahora tiene su propio ingreso con usuario y clave.
- ✨ Se agregó la tarjeta de **Consulta Geográfica** al menú.
- 🔧 El estado de cada herramienta (disponible / caída) ahora lo mide el servidor, no el navegador.

**Consulta Geográfica (malla vial de Bogotá)**
- ✨ Consulta abierta de la malla vial: se resuelve el CIV de un punto GPS, se validan listados de CIV
  y se dice en qué localidad y UPL cae una coordenada.

**Registro de Horarios**
- 🐞 Con la primera jornada cerrada y la segunda abierta, la pantalla decía «falta la salida» sin
  dar con qué marcarla, el día no salía como pendiente y las horas se calculaban sobre la jornada
  equivocada.
- 🐞 El encabezado parpadeaba al cambiar de pantalla. Ya no.
- 🔧 La app dice en qué versión está, para poder reportar un problema con precisión.

**Administración de la plataforma**
- ✨ Consola interna para ver y ajustar las cuentas de administrador de cada herramienta, con registro de auditoría.

---

## 2026-08-29

**Registro de Horarios**
- 🐞 Un mismo centro de trabajo aparecía dos veces con nombres distintos. Se unieron sin perder
  la historia de ninguno de los dos.
- 🔧 Buscar a una persona por su cédula ahora la encuentra.

---

## 2026-08-28

**Registro de Horarios**
- ✨ Pestaña **Quién ha entrado**: muestra quién de la nómina nunca ha usado la app, y permite
  invitar en bloque. Al mirarlo por primera vez, 231 de 260 personas nunca habían entrado.

**Portal de Proveedores**
- ✨ Tema oscuro.
- 🔧 El verde de la marca se aclaró para que el texto sobre él se lea de verdad.

**Gestión de Proyectos**
- ✨ Matriz de interesados.
- 🐞 Tres cifras del mismo tablero se desmentían entre sí. Corregidas.
- 🐞 Un proyecto al que le cambiaron el nombre en el ERP se contaba dos veces.
- 🔧 Todo lo que se toca con el pulgar mide al menos 40 px.

**Tablero DataMart**
- ✨ Alerta por correo cuando falla una fuente de datos puntual, no solo cuando falla todo el proceso.
- ✨ Cada cifra y cada filtro del tablero explican qué miden al pasar el mouse. Un revisor
  automático comprueba que no quede ninguna sin texto.

**Tablero DataMart**
- ✨ Opción **Tamaño del tablero**: se puede agrandar la letra y la interfaz. Las opciones que no caben
  en tu monitor salen apagadas en lugar de cortar el menú.
- 🔧 El tablero se adapta al monitor: la letra de cada tabla se calcula según lo que la tabla necesita.
- 🔧 Cambiar el tamaño de la ventana ya no tarda: la medición pasó de ~11 segundos a menos de 1.

---

## 2026-08-27

**Registro de Horarios**
- ✨ Los permisos se registran **por horas**, no solo por día completo, y se ven en la vista del mes.
- ✨ Se pueden marcar varios días de una vez.
- ⚠️ Quién aprueba una novedad y quién recibe el aviso son ahora **dos listas distintas**. Antes
  estaban mezcladas; revisa la tuya.
- 🐞 Un día con el registro abierto pero vacío se contaba como cubierto. Ya no.

**Gestión de Proyectos**
- ⚠️ El avance se mide de **una sola forma**: por valor ganado. Antes tres cifras del mismo
  tablero se desmentían entre sí y el presupuesto se contaba de dos maneras.
- 🐞 Un proyecto al que le cambiaron el nombre en el ERP se contaba dos veces.
- 🔧 El semáforo ahora dice **«no sé»** cuando le faltan datos, en vez de pintar un color inventado.
- ⚠️ El permiso por proyecto ya se aplica de verdad. Antes se veía en la configuración y no
  restringía nada.
- ✨ Pestaña de documentos del proyecto.

---

## 2026-08-26

**Portal de Proveedores**
- 🔧 «Faltan» y «vencidos» dejaron de ser la misma palabra: no es lo mismo un documento que nunca
  se subió que uno que se venció.
- 🔧 La cédula dice **qué** falta, no solo que falta algo. Y el SG-F-01 se puede subir ya firmado.
- ✨ A quien pidió un alta se le avisa el resultado.

**Registro de Horarios**
- ✨ Calendario del mes, con el día al lado, los turnos en un renglón y un contador de cobertura.
  Desde ahí se registran novedades y el compensatorio.

---

## 2026-08-25

**Registro de Horarios**
- ✨ **Los informes de nómina los arma la app.** Antes una persona los copiaba a mano cada mes.
  Tres vistas en pantalla, dos Excel con fórmulas vivas, hoja de firmas que respeta el corte,
  y filtros de con/sin registro y con extras.
- ⚠️ En domingo y festivo todo el tiempo trabajado se liquida como **extra dominical**.

**Portal de Proveedores**
- ✨ **Alta de empleados**, que no tienen RUT y antes se hacían por fuera. Con cédula,
  certificación bancaria y hoja de vida; la ciudad sale de la tabla del DANE.

**Gestión de Proyectos**
- ✨ Panel de variables: la fórmula del valor ganado y las reglas del semáforo se configuran
  desde la app, sin tocar el código.
- ✨ Los proyectos se agrupan en portafolios por la naturaleza del gasto.

---

## 2026-08-26 · Biblioteca

**Biblioteca de Informes**
- ✨ Los informes se publican con un enlace para compartir. Se puede abrir o cerrar el enlace público
  de cada documento; volver a subir el mismo título genera una versión nueva en la misma dirección.

---

## 2026-08-21

**Portal de Proveedores**
- ✨ La firma del representante legal se propone automáticamente a partir de la cédula; el proveedor
  la confirma o la reemplaza.
- 🐞 El paso del RUT ya no se traba: antes decía "no pudimos leer" y a la vez mostraba un resumen, con
  el campo que pedía oculto.
- 🔧 Los correos del portal salen desde la cuenta de compras, con el diseño corporativo.

---

## 2026-08-20

**Portal de Proveedores**
- ⚠️ El formulario SG-F-01 quedó igual al oficial: dos empresas, una sola firma. Se eliminó la
  autorización de datos suelta (ya va dentro del formulario).
- ✨ 34 campos se llenan solos a partir del RUT y la cédula.
- 🔧 El NIT se valida con dos o tres lecturas independientes del documento: solo se bloquea si dos
  coinciden en un NIT distinto al tecleado.

---

## 2026-08-19

**Tablero DataMart**
- ⚠️ Todo el contenido del tablero exige haber ingresado con usuario y clave, incluidos los
  archivos de datos que alimentan las tablas.
- 🐞 Filtros que descuadraban el tablero: las órdenes de compra ahora se filtran por orden completa.

---

## 2026-08-18

**Tablero DataMart**
- ✨ Panel de estado rediseñado, con actualización de una sola tabla en lugar de todo el proceso
  (11 segundos en vez de 37 minutos).
- 🐞 Cuando una cifra mezcla unidades distintas, la medida ahora aparece **vacía** en lugar de mostrar
  un número que no significa nada.

---

<sub>Las entradas anteriores a agosto de 2026 no están publicadas aquí.</sub>

<sub>Cada entrada de este historial está verificada contra el registro de cambios del código. Si
encuentras algo que no cuadra con lo que viviste, dilo: preferimos corregirlo.</sub>
