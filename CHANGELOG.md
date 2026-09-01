# Historial de actualizaciones

Lo que ha salido a producción, de lo más reciente a lo más viejo.
Redactado para quien usa la herramienta, no para quien la programa.

Formato de cada entrada: **✨ Nuevo** · **🔧 Mejorado** · **🐞 Corregido** · **⚠️ Cambio de comportamiento**

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

## 2026-08-26

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
