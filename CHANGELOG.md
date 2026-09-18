# Historial de actualizaciones

Lo que ha salido a producción, de lo más reciente a lo más viejo.
Redactado para quien usa la herramienta, no para quien la programa.

Formato de cada entrada: **✨ Nuevo** · **🔧 Mejorado** · **🐞 Corregido** · **⚠️ Cambio de comportamiento**

---

## 2026-09-15

**Asistente por WhatsApp**
- ✨ El **certificado de aportes a seguridad social y parafiscales** (artículo 50 de la Ley 789 de
  2002) lo elabora el asistente: se pide con la empresa y el mes, y llega en PDF en dos versiones,
  con la relación del personal activo de ese mes o general, sin listado. Sale **sin firma** —el
  documento lo responde una persona con su tarjeta profesional— y no se emite si faltan las
  planillas de los seis meses que el texto afirma: en su lugar dice cuáles faltan.
- 🐞 «Parafiscales» nombra dos documentos —la planilla y el certificado— y siempre se entregaba el
  primero. Ahora se distingue por las palabras del mensaje y, cuando no queda claro, se pregunta.
- 🔧 Los documentos se abren en el panel sin tener que descargarlos: planillas, certificados de
  aportes, constancias de la ARL, certificados de parafiscales y documentos de empresa.

---

## 2026-09-11

**Portal de Proveedores**
- 🔧 «Leer de nuevo» relee los documentos del expediente desde la ficha y muestra qué difiere de lo
  que hoy se enviaría, dato por dato, con una casilla para aplicar solo lo que se quiera. Cada dato
  dice de dónde viene: tecleado o leído del documento, por quién y cuándo.
- 🐞 El NIT impreso en una certificación bancaria es el del banco, no el del tercero: dejó de
  cruzarse con el RUT. Una proveedora había quedado apartada por eso teniendo sus documentos en
  regla.
- 🐞 Cuando el ERP ya contestó algo sobre una solicitud, la ficha muestra esa respuesta y no la
  anterior: se ve el paso y el motivo reales.

---

## 2026-09-10

**Portal de Proveedores**
- 🔧 El panel de administración, por pasos: cada solicitud se abre en una ficha de cinco pasos
  —solicitud, documentos, datos, creación en el ERP y cierre— dentro de un panel lateral. Se
  aprovecha el ancho de la pantalla, la búsqueda funciona por NIT y por nombre, y cada persona del
  equipo tiene «Mi cuenta» para su tema, su página de inicio y qué avisos recibe por correo.
- 🔧 «Ampliar» lleva cualquier documento a ventana completa dentro de la misma pantalla, con
  Descargar en su cabecera. El expediente queda en tres columnas: documentos, vista previa y lo
  leído.
- 🔧 Al escribir un NIT que ya existe en el ERP o que ya tiene solicitud, la acción es «Abrir su
  ficha» en vez de un botón apagado sin explicación. Los documentos vigentes se muestran como «ya
  en el expediente» y al crear solo viajan los nuevos.
- ✨ Una pantalla lista cada aviso con su regla y cada correo que intentó salir, con su resultado, y
  permite pausarlos dejando el motivo escrito. «Consultar tercero» reúne todo lo que la plataforma
  tiene de un NIT. Y se puede eliminar —con motivo— una solicitud que no llegó al ERP, una versión
  de documento rechazada y un usuario sin actividad.

**Gestión de Proyectos**
- 🔧 Buscador de variables: las 167 se encuentran sin abrir los 32 grupos, y la lista dice cuántas
  hay apagadas en cada uno.

---

## 2026-09-09

**Portal de Proveedores**
- 🔧 El informe de solicitudes pasa de diez columnas a seis —Tercero · NIT · Situación · Fecha de
  solicitud · Fecha de creación · Auditoría—, con las fechas completas y la auditoría detrás de un
  botón al final de la fila. Las cuatro que se fueron repetían o contaban mal: «Estado» y «En
  SINCO» decían lo mismo en las 24 filas de producción, y «Doc.» contaba dos veces el mismo
  documento en 9 de 22.
- 🐞 Tres fallos que se tapaban unos a otros: un aviso rojo que decía «[object Object]», el
  formulario volviendo al inicio al aprobar un documento, y un tercero que no se podía crear porque
  se había leído «APRECIADO USUARIO» —el saludo de la carta— como el titular de la cuenta.

**Gestión de Proyectos**
- 🐞 La auditoría se cierra a administradores: la pantalla mandaba al tablero a quien tuviera rol de
  gestor, pero el servidor sí le respondía.
- 🔧 Las ocho pantallas revisadas con datos dentro, a siete anchos —de 1600 a 320 puntos— y con los
  cinco roles.

**Registro de Horarios**
- 🔧 La hoja donde se elige la fecha dice «registrar o revisar»: por ahí también se abre un día ya
  guardado para mirarlo.

**Asistente por WhatsApp**
- 🐞 Los RUT, cámaras de comercio y RIT que entrega el asistente llevaban desde el 1 de agosto sin
  actualizarse, sin que nada lo avisara: entregó el RUT del 29 de julio durante 41 días, incluidos
  los 20 que se renovaron el 7 de septiembre. Ahora se piden a Compras cada seis horas, y lo que ya
  no está allí se aparta en vez de borrarse.

---

## 2026-09-08

**Asistente por WhatsApp**
- ✨ **Certificado de accidentalidad de la ARL**, por empresa y por mes, entregado por WhatsApp. Se
  baja solo cada mes y tiene permiso propio, separado del de la planilla de seguridad social.
- 🐞 Un perfil con acceso a nómina y a documentos de empresa recibía «no tiene permiso» al pedir la
  planilla de seguridad social, un minuto después de haber recibido el certificado de
  accidentalidad de esa misma empresa. Nadie perdió accesos: el cambio solo suma.
- 🔧 En el panel de los robots, ficha por empresa: qué hay mes a mes, qué contestó el portal en cada
  intento, quién apagó qué y cuándo, y un botón para reintentar solo esa empresa o un mes puntual.

**Registro de Horarios**
- ⚠️ No se empieza un día teniendo otro sin cerrar. Marcar la entrada y no marcar la salida dejaba
  el día a medias para siempre; medido el 7 de septiembre, cuatro personas siguieron marcando días
  posteriores encima de uno abierto. Ahora se resuelve de uno en uno, del más viejo al más nuevo.
- 🔧 En Preguntas frecuentes, el botón Volver, el título y el buscador se quedan fijos al bajar por
  las 104 preguntas.

---

## 2026-09-07

**Gestión de Proyectos**
- 🔧 Se puede borrar una fase, elegir en qué unidad se muestran las cifras, y Administración avisa
  cuando una operación no sale.

**Asistente por WhatsApp**
- 🐞 El botón para relanzar el robot de las planillas no funcionó nunca desde que se publicó, y el
  semáforo seguía en verde: la orden se quedaba «corriendo» para siempre. Ahora cada corrida tiene
  un tiempo máximo, el botón lanza de verdad, y el panel muestra el estado real de cada robot.

---

## 2026-09-03

**Asistente por WhatsApp**
- 🐞 La misma pregunta daba tres cifras distintas de facturación según por dónde entrara. Una de
  ellas salía de sumar un solo lado de los movimientos contables, que mezcla cartera, ingreso e
  impuesto. Ahora se responde desde la fuente que corresponde, la misma del Tablero DataMart.
- 🐞 Un fallo de lectura se disfrazaba de «no existe»: si la consulta a la nómina no respondía, el
  asistente decía «no encontré a esa persona» y guardaba esa respuesta media hora. Ahora un fallo
  técnico se dice como fallo y no se guarda. Además, cero filas dejó de contarse como un cero, y una
  disculpa dejó de contar como respuesta correcta.
- 🔧 «Del mes pasado» se mide por la fecha del hecho. Antes se tomaba la primera columna que
  empezara por «Fecha», y casi nunca era la que tocaba: en la hoja de vida, la de expedición de la
  cédula; en contratos, la de terminación; en ausentismo, la del regreso.

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
- 🐞 En la ficha, el nombre de cada documento se estrujaba —«Cámara / de / Comercio» a una
  palabra por línea— desde que se alargó el texto de uno de los botones. El aviso bajó al
  bloque del nombre, y en pantalla estrecha la fila se parte.

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
