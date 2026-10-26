# Historial de actualizaciones

Lo que ha salido a producción, de lo más reciente a lo más viejo.
Redactado para quien usa la herramienta, no para quien la programa.

Formato de cada entrada: **✨ Nuevo** · **🔧 Mejorado** · **🐞 Corregido** · **⚠️ Cambio de comportamiento**

---

## 2026-10-25

**Panel de Automatizaciones**
- ⚠️ El reenvío de facturas al receptor también pide el permiso aparte y la confirmación para pasar una empresa a reenviar de verdad.

**Asistente por WhatsApp**
- ✨ Sección «Plantillas de informe» en el panel: compartir, dejar de compartir y borrar con «Deshacer».
- 🐞 «Bueno», «solo» o «disponibles» ya no se toman por nombres de personas al pedir documentos.
- 🔧 «El último desprendible» es el del último mes liquidado, y «mi desprendible», el de quien escribe.

---

## 2026-10-24

**Panel de Automatizaciones**
- ✨ Arriba se escoge la empresa con la que se trabaja, y Accesos da a cada persona sus empresas una vez y las áreas que ve.
- ⚠️ Pasar una empresa a envío real pide un permiso aparte y confirmación, en Pedidos, Cobro de cartera, Notificación de pagos y Facturas sin soporte.

**Tablero DataMart**
- ✨ Contratos tiene el subtab **Cajas Menores**: una fila por caja, con los días sin legalizar y la situación
  «quieta» si pasa de 90, y el detalle de cada acta con el tercero de cada factura.
- 🐞 En el Informe, con un filtro de insumo, tipo, agrupación, unidad u origen, la utilidad queda en blanco en vez de
  mostrar una cifra que no se puede calcular a ese nivel.
- 🐞 En CONTROL, el filtro de año ya no saca el presupuesto ni el proyectado, y lo que no tiene fecha dice «Sin fecha»,
  no 1900.
- 🔧 Las tarjetas de las ocho áreas caben en una sola fila desde 1366 px de ancho.

**Asistente por WhatsApp**
- 🐞 La edad del personal se calcula con la fecha de nacimiento completa: venía mal en 401 de 2.071 personas.
- 🐞 Las listas filtradas por mes salen completas: «cumpleaños de noviembre» daba 17 de 27.
- 🔧 Contar y sumar por grupos lo hace el programa, no la inteligencia artificial.
- ✨ Plantillas de informe: se guardan con un nombre y se vuelven a usar con otra empresa, periodo o formato.
- ✨ El informe puede llegar como página para el celular, con buscador, orden, gráfico y totales.
- ✨ Informes de varias empresas a la vez, dentro de las que permite el perfil.

**Gestión de Proyectos**
- 🔧 Aspecto corporativo compacto: azul marino, letra de 13 px, indicadores en una franja, logos de las empresas,
  íconos en vez de emojis y un solo formato de cifras.

**Cajas Menores**
- 🔧 «Separar» propone el corte de cada soporte con la lectura automática, ajustado a la tinta, y marca la hoja 2 y la página en blanco: con 289 páginas ya confirmadas acierta en 224 (antes 148).
- ⚠️ Control ya no pide verificar cuatro avisos que nunca detuvieron un soporte (antigüedad, fecha anterior, placa de otro proyecto y factura no recibida en la DIAN): ahora son solo aviso.
- 🔧 La nota de Control deja de ser obligatoria, y «Todo conforme» deja conformes de una vez los soportes sin problema.
- 🔧 El paso SINCO trae la ruta del ERP para subir el Excel, en seis pasos.

---

## 2026-10-23

**Tablero DataMart**
- 🔧 Compras › Proveedores trae la ficha de cada tercero como quedó en el ERP: 29 columnas y 24 filtros (contacto,
  actividad económica, datos de pago, casillas tributarias).
- 🐞 El total de contratos de cada proveedor va al contratista del contrato y cuadra con el área Contratos. Antes se
  repartía por el tercero de cada línea del acta.
- 🐞 Dos proveedores con el mismo nombre y distinto NIT ya no se funden en una sola fila.
- ⚠️ La caja menor ya no cuenta como contrato del proveedor: va en su propio informe en Contratos.
- 🔧 La consulta de los datos disponibles del DataMart responde en cerca de 1 segundo; tardaba unos 50.

**Portal de Proveedores**
- 🔧 La ficha compara con el ERP el CIIU, seis casillas tributarias y la cuenta bancaria, y dice desde cuándo está el
  tercero en el ERP. Al medirlo, 32 de 68 terceros tenían algo distinto.
- 🐞 El autorretenedor es el código 15 del RUT, no el 46, como decían la ficha y el asistente.

**Asistente por WhatsApp**
- 🔧 El asesor SINCO dice cómo se hace en la empresa («En CIMELEC: …») en 22 clases contables.
- 🐞 Si la inteligencia artificial principal falla, contesta la de respaldo: antes el respaldo fallaba siempre.

**Registro de Horarios**
- 🔧 Planilla, Excel, horas extra, hoja de firmas, cobertura y calendario salen de un mismo cálculo; comparados contra
  los de antes en 1.316 salidas, sin una diferencia en números.
- 🐞 La hoja de firmas sale con el filtro de la planilla, reabrir un día ya no lo deja «devuelto» y un jefe quitado de un
  centro ya no vuelve a aparecer.

**Cajas Menores**
- 🐞 Un código QR que no se dejaba leer trabó la app 19 horas. Ahora cada QR tiene un tope de 20 segundos y, si no se lee, la página sigue sin ese dato.

---

## 2026-10-22

**Asistente por WhatsApp**
- ✨ El asesor SINCO atiende también el módulo contable del ERP (A&F): 71 clases más, con datos de facturas, cuentas por
  pagar y documentos contables para quien tiene acceso.

**Registro de Horarios**
- ✨ Sección «Reglas» en Administración: 22 reglas de marcaje, ley, aprobación, avisos e informes se cambian sin
  programar, con mínimo y máximo; las de ley, con fecha de vigencia.
- ⚠️ El tope de 30 días para registrar un día propio vale por cualquier camino: la planilla dice «Lo registra tu jefe o
  RRHH» y Hoy avisa «Día muy atrás» al abrirlo.
- 🐞 Las horas extra del sábado se perdían si Gestión Humana recibía el viernes y el sábado antes que el resto de la
  semana; 4 sábados corregidos.
- 🔧 Si un día ya recibido cambia porque se cargó o se borró otro de su semana, quien lo recibió recibe un aviso.

**Gestión de Proyectos**
- ✨ Alertas de dato de la PMO: por cada contrato con cifras del ERP que no son creíbles, la causa (ítem e insumo), la
  corrección sugerida y quién la hace, con un Excel para Presupuestos.

---

## 2026-10-21

**Tablero DataMart**
- 🔧 En el panel de Administración, la ficha de cada proyecto lleva los datos del contrato para la oficina de proyectos.

**Asistente por WhatsApp**
- 🔧 «A cuánto compramos X» mira órdenes de compra, subcontratos y cotizaciones vigentes, y responde en segundos.
- 🐞 Una tarifa de alquiler de transporte ya no se presenta como precio de un material.
- 🐞 «Contratos de una empresa en otra» ya no suma las dos empresas.
- 🔧 Si una consulta de contratos admite dos lecturas, el asistente pregunta con botones.
- ⚠️ La encuesta de satisfacción sale una vez, al cerrar la conversación, y solo si hubo una respuesta de verdad.

---

## 2026-10-20

**Panel de Automatizaciones**
- ✨ Los pagos a proveedores se notifican solos cada día hábil a las 19:00, en 20 empresas.
- 🔧 Portal DIAN: quien puede consultar una empresa cancela el proceso que otra persona dejó abierto.

**Portal de Proveedores**
- ✨ El detalle de cada factura dice cuánto se le pagó y cada descuento (anticipo, garantía, retenciones, FIC), sacado del
  asiento contable; también en el Excel de facturas.
- ✨ «Resumen…» en la lista: solicitudes por estado, por tipo de alta y por mes, con rango de fechas.

**Asistente por WhatsApp**
- ✨ Las cámaras de comercio del grupo se descargan solas, una vez al día, de las ya compradas.
- 🔧 Ficha de una persona, cumpleaños del mes, código de un insumo y NIT se responden en segundos; antes tardaban hasta
  90 s o se caían.
- 🔧 El asesor SINCO consulta también contratos, entradas de almacén, actas e ítems del presupuesto.

---

## 2026-10-19

**Tablero DataMart**
- 🔧 La nómina se trae también a las 8, a las 12 y a las 4, y a pedido. Antes, una sola vez en la madrugada.

**Portal de Proveedores**
- ✨ El texto de los ocho correos al proveedor se edita en pantalla, con variables y vista previa.
- ✨ «Desvincular» saca de la red a un proveedor aprobado, con motivo, sin tocar el ERP; se reintegra igual.
- ✨ Cada tercero puede tener un responsable, y la bandeja «Actualizaciones» reúne los creados con algo pendiente.
- ✨ La especialidad escogida en el portal llega a la calificación del tercero en el ERP.

**Asistente por WhatsApp**
- ✨ Los documentos de las empresas se ven en matriz en el panel: empresa por documento, y mes a mes.
- 🔧 Los documentos se piden como se habla: «y el de agosto», listas de personas, varias empresas o meses en un
  mensaje, y nombres con errores de escritura.
- ✨ Lo pedido que todavía no existía se manda solo cuando la persona vuelve a escribir.
- 🔧 La cámara de comercio y el RIT llegan con su fecha de expedición, el más reciente y nunca el de otro NIT.

**Registro de Horarios**
- 🔧 La nómina se trae tres veces al día y «Sincronizar ahora» la pide: quien entra hoy a la nómina puede marcar hoy.
- ⚠️ Cada persona queda en la obra de su contrato cuando ese centro está conectado, no en la de su último desprendible;
  los días ya marcados no se mueven.
- 🔧 Un centro nuevo de la nómina se enlaza solo con su proyecto del ERP cuando coinciden centro, empresa y proyecto.

---

## 2026-10-18

**Panel de Automatizaciones**
- ✨ El empleado nuevo de la nómina se crea solo como tercero en el ERP; el que tiene dudas espera y se completa en su ficha.
- 🔧 Portal DIAN: varias empresas pueden ir a la vez, retomarse o cancelarse.

**Portal de Proveedores**
- ⚠️ RUT y Cámara de Comercio vencen a los 180 días, no a los 30: 34 de 61 documentos vencidos volvieron a vigentes.
- ✨ «Anular» cierra una solicitud sin borrar nada, y «Desaprobar» devuelve una aprobada a revisión, con motivo.
- ✨ «Hoja de vida (PDF)» en el pie de la ficha del tercero.
- 🔧 La lista de solicitudes dice quién creó cada una y cuántos días lleva, con filtro por persona.
- 🔧 Una actualización ya no se frena por un dato que solo se exige al crear: lo demás llega al ERP.

**Asistente por WhatsApp**
- ✨ Asesor SINCO para todo el personal, según su perfil: responde cómo se hace algo en el ERP con los pasos, la ruta del
  menú y el video de la clase dentro de WhatsApp; 202 clases de cuatro cursos.
- 🔧 El asesor SINCO recuerda la conversación, pregunta lo que le falta y, a quien tiene acceso a datos, le dice el estado
  real de la orden, el pedido o el insumo en el ERP.
- ✨ Panel de administración nuevo, por secciones: Inicio, Personas, Conversaciones, Permisos en palabras, Documentos,
  Robots, Ajustes y Archivos y correo.

---

## 2026-10-17

**Portal de Proveedores**
- 🔧 El administrador fija los días de vigencia de cada tipo de documento, con simulación antes de guardar.
- 🔧 La dirección llega al ERP en el estándar de la DIAN.
- 🐞 Si el ERP no acepta una actualización, la ficha lo dice en vez de marcarla como hecha.

**Cajas Menores**
- 🔧 «Terceros» completa dirección, correo y ciudad con la consulta propia del RUES, y toda dirección queda en el estándar de la DIAN, como la guarda el ERP.

---

## 2026-10-16

**Panel de Automatizaciones**
- ✨ Portal DIAN: para las empresas sin certificado, una extensión del navegador baja sola lo que falta mientras la sesión de la DIAN está abierta.

**Consulta RUES**
- ✨ Consulta de terceros en el RUES por NIT, cédula o nombre, desde el asistente y desde Excel, con alertas de matrícula
  cancelada o sin renovar; un listado de hasta 2.000 de una vez.
- 🔧 Contacto, dirección y CIIU de 5.932 terceros del ERP, puestos al día con el registro mercantil.

---

## 2026-10-15

**Asistente por WhatsApp**
- 🐞 Una respuesta que se demora ya no se corta a los 95 segundos sin contestar nada.

---

## 2026-10-14

**Panel de Automatizaciones**
- ✨ Cada proyecto recibe cada semana sus facturas sin acta ni entrada, con su Excel; cada empresa se enciende aparte.
- 🔧 Portal DIAN: la factura que falta se trae una a una, guiada, o sola con el certificado digital de la empresa.

**Asistente por WhatsApp**
- 🐞 Las respuestas llegan en el formato de WhatsApp: sin ###, ---, dobles asteriscos ni fórmulas que en el teléfono
  salían como símbolos sueltos.

**Cajas Menores**
- 🔧 En «Mejorar», cada soporte se gira por su cuenta.

---

## 2026-10-13

**Panel de Automatizaciones**
- ✨ Portal DIAN: cruza lo que la DIAN tiene a nombre de cada empresa contra el receptor del ERP y muestra lo que falta, por rango de fechas.

**Bitácora de Obra**
- ✨ Lo cerrado se copia solo, cada 15 minutos, al sitio de documentos de la empresa: el informe con sus fotos y su PDF
  y los folios con sus adjuntos, ordenados por obra y mes, con un índice por obra.
- 🔧 Administración › Sistema muestra la sincronización con el ERP («Sincronizar ahora»), quién entró esta semana, las
  obras nuevas sin nadie asignado, lo que falta configurar y el registro de cambios en palabras.

**Cajas Menores**
- ✨ Paso «Mejorar»: cada soporte se ve más claro —sin manchas, sombras ni tinta desteñida— con el antes y el después lado a lado; quien digita elige, y nada se redibuja.

**Capacitación**
- ✨ Buscador en Mi curso y en Revisar el curso: encuentra la clase por su título o por lo que dice el video, y muestra en qué paso y minuto está.

---

## 2026-10-12

**Panel de Automatizaciones**
- ✨ La factura que un proveedor manda a otro buzón de la empresa se reenvía sola, cada día, al receptor del ERP (25 empresas, 21 reenviando).

---

## 2026-10-10

**Tablero DataMart**
- ✨ Panel de **Administración**, al final del menú: retegarantía por capítulo e ítem, datos del proyecto y del
  contrato, usuarios y conectores, y un maestro de cuentas contables por empresa. Cada cambio con motivo e historial.
- ⚠️ Las hojas de cálculo compartidas ya no alimentan el tablero: lo que se cambie allá no cambia nada; se corrige en el
  panel.

**Cajas Menores**
- ✨ «Informes» (siete vistas con filtros, para ver, imprimir o bajar en Excel) y «Adjuntos» (la biblioteca de escaneos).
- ✨ «Actas generales en SINCO»: cada acta de caja menor como la muestra el ERP, con sus líneas y acumulados.
- ⚠️ La caja se cierra sola cuando su acta del ERP pasa a CXP o CXP-M; ya no espera a que se crucen las cuentas por pagar.

**Capacitación**
- ✨ Curso de Maquinaria y equipo: 33 clases sobre los formatos y la app del área, con guía en PDF. Lo ven 77 personas de los cargos de maquinaria y los residentes.

---

## 2026-10-09

**Portal de Proveedores**
- 🐞 Relanzar una creación o actualización ya no duplica los documentos en el expediente del ERP.

**Cajas Menores**
- 🐞 El ERP no leía el Excel de la caja. Ahora sale como su plantilla oficial y el ERP lo acepta: las 44 líneas de la primera caja aprobada entraron ese día.
- 🔧 El PDF de soportes conserva el escaneo en blanco y negro tal cual: el de la primera caja pasó de 28,3 MB a 3,3 MB.
- ✨ Paso «Terceros»: el proveedor que no existe en el ERP se completa desde el soporte, el RUT o a mano, y lo crea el robot del Portal de Proveedores sin salir de la caja. El RUT no es obligatorio.
- 🔧 En la revisión de Control, cada alerta pendiente lleva con «Ver ›» al campo que la causa.

**Capacitación**
- ✨ Material para descargar debajo del video de cada clase: formatos, ejemplos y la guía paso a paso en PDF.
- 🔧 Los grupos de cursos se crean y se cambian en Ajustes, con sus secciones y los cargos que los reciben.

---

## 2026-10-08

**Portal de Proveedores**
- ✨ «Actualizar con datos nuevos»: un tercero ya creado se actualiza con documentos nuevos; una cuenta nueva la aprueba
  otra persona de Contabilidad.
- 🐞 Ninguna actualización de un tercero existente llegaba al ERP; ahora va por la plantilla de actualización y solo con
  lo que cambia.
- 🔧 En el paso «Datos» del asistente se ven los documentos al lado de los datos que se validan.
- 🔧 En Usuarios, cada persona ve qué puede hacer y de qué rol le viene.
- 🐞 El formulario de subir un documento ya no se cierra por debajo de quien lo usa.

**Capacitación**
- 🔧 La encuesta de seguridad vial se puede responder sin esperar los videos, y su PDF sale en una sola hoja, igual al formato oficial.
- ✨ Seguimiento muestra quién llenó la encuesta, y hay un consolidado por empresa en pantalla y en Excel.
- 🔧 Una sección se puede asignar a mano a una persona o a un cargo.

---

## 2026-10-07

**Portal de Proveedores**
- 🔧 La ficha y el asistente usan la pantalla completa.

**Cajas Menores**
- ✨ Aviso por correo cuando una caja aprobada pasa varios días sin acta en el ERP.

**Capacitación**
- 🔧 La inducción del SGI quedó en 27 videos cortos (de 110 a 76 minutos) y sin la sección de área. Mi curso dice cuántos minutos faltan, y nadie perdió lo que ya llevaba.
- ✨ La encuesta de seguridad vial del PESV va dentro de la inducción, por temas y una pregunta por pantalla, y sale en PDF junto al diploma.

---

## 2026-10-06

**Bitácora de Obra**
- ✨ «Así queda»: antes de firmar, la primera página del informe junto al botón; tocarla abre el informe completo con
  zoom, sin salir de la app.
- 🔧 El «PDF» de Informes de obra y las fotos se abren en el mismo visor, con anterior y siguiente.
- ✨ «Historia» en Estado y envío: todo lo que le pasó al informe y a sus partes.
- 🔧 Cada cantidad dice lo que le falta según las reglas de la obra (foto, ubicación, código de vía), y «Para ti hoy»
  ofrece «Seguir» en el paso donde quedó el informe.

**Capacitación**
- ✨ Curso contable completo: 13 videos paso a paso, solo para los cargos del área.
- ✨ Junto a cada diploma se descarga la evaluación en PDF, resumida o con las preguntas, con el logo de la empresa de la persona.
- 🔧 Las pantallas de administración también funcionan en el celular.

---

## 2026-10-02

**Registro de Horarios**
- 🐞 30 personas activas aparecían retiradas o sin acceso: con varios contratos ganaba el último en llegar y no el
  vigente, y la terminación de un término fijo contaba antes de su fecha.

**Cajas Menores**
- ✨ «La caja en SINCO»: un Excel que compara lo que dice la app con lo que tiene el ERP y marca en rojo lo que no casa.
- ✨ «Reglas de la caja»: el administrador ajusta topes y avisos desde la app, y cada aviso dice qué hacer.
- ✨ Si los soportes ya están en un acta del ERP, la app avisa que la caja parece ya cargada y ofrece sacarlos o anularla.

**Capacitación**
- 🐞 Un contrato a término fijo ya no se toma como retiro antes de su fecha: aparecieron 30 personas activas más.
- 🔧 En Seguimiento, cada columna se filtra por varios valores a la vez.

---

## 2026-10-01

**Planoteca**
- ✨ Planos de diseño y récord: dos cadenas por plano, cada una con su vigente, y un interruptor en la consulta para pasar de una a otra. El récord solo queda vigente con el oficio de la entidad.
- ✨ Medir sobre el plano a la escala del dibujo, en todos los visores, con lupa; lo medido se puede corregir.
- 🐞 Una fecha escrita mes/día bloqueaba para siempre la subida de ese plano.
- 🐞 Un oficio registrado con el número de otro se reusaba sin avisar; ahora se avisa.
- 🔧 La escala se lee en más hojas: de 166 a 201 en una obra y de 7 a 13 en la otra.

**Capacitación**
- ✨ Curso de Talento Humano: 9 sesiones, sin plazo y en cualquier orden, con su propio diploma. La plataforma ya maneja varios cursos.

---

## 2026-09-30

**Bitácora de Obra**
- ⚠️ Se entra con la cuenta de la empresa o con un código de seis dígitos que llega al correo; la app ya no usa
  contraseña propia.
- 🔧 El nombre del paso del informe se lee en el teléfono en los seis pasos, y las horas de lluvia solo se piden si
  llovió.
- 🐞 El impreso de un informe anulado ya dice ANULADO, y trae la fundida en concreto, que faltaba.
- 🐞 Cada rol deja de ver botones que luego fallaban, como «Nuevo informe» para la interventoría.

**Cajas Menores**
- ✨ Nueva herramienta: cada caja menor del escaneo al acta del ERP. Lee los soportes (QR y lectura automática que una persona valida), los cruza con el ERP, frena los repetidos, pasa por Control y entrega el Excel y el PDF para el ERP.

**Planoteca**
- ✨ La consulta en el teléfono, con el buscador y los filtros fijos abajo.
- ✨ Se instala como app en Android, iPhone y el computador; no guarda planos en el teléfono.
- ✨ Avisos por correo (revisiones por aprobar, copia por recoger, resumen semanal): cada persona enciende los suyos.
- 🔧 «Vigente al» también muestra lo que la planoteca mostraba ese día, además de lo que dicen los oficios.

**Capacitación**
- 🔧 Cada pantalla se rehízo para el celular, con las 23 sesiones de la inducción en video.
- ✨ La app se instala en el celular o en el computador como cualquier otra.
- ✨ Mi obra y A quién acudo tienen botones para llamar y escribir por WhatsApp o por correo con un toque.

---

## 2026-09-29

**Planoteca**
- ✨ «Vigente al»: la planoteca como estaba en una fecha, según los oficios; y «Comparar» dos revisiones de un plano.
- ✨ Remisiones con su acuse, copias en papel con QR y «Faltantes conocidos».
- ✨ Lista maestra en Excel, y la hoja que se abre aparte sale marcada «COPIA NO CONTROLADA».
- 🔧 El número de revisión lo pone la planoteca por la fecha del plano: R-01, R-02…
- 🔧 También se entra con la cuenta de correo de la empresa, sin código.

**Capacitación**
- ✨ Seguimiento cruzado con la nómina, con ingreso y retiro de cada persona. Permite bajar diplomas, mandar recordatorios por correo y sacar el Excel de varias personas a la vez.
- ✨ Informes de vencimientos y de las preguntas que más se fallan, y un modo para revisar todo el curso sin dejar registro.
- ✨ «Preguntar», en cada clase, le manda la duda al SST de la obra.

**Biblioteca de Informes**
- 🐞 Los selectores de la clasificación ya no cortan el nombre de la serie.

---

## 2026-09-28

**Planoteca**
- ✨ Al subir un plano, la app lee su rótulo y propone revisión, fecha y descripción; quien sube confirma.

**Capacitación**
- ✨ Nueva herramienta: la inducción y reinducción del SGI en video, con preguntas, evaluación, firma y diploma. Entran todos los trabajadores activos de la nómina con su cédula.

**Biblioteca de Informes**
- 🔧 Diseño nuevo: nueve documentos enteros a la vista en el celular (antes dos), y el enlace de un documento se copia
  de un toque en el computador.

---

## 2026-09-27

**Portal de Proveedores**
- 🐞 El saludo de una certificación bancaria («Apreciado usuario») ya no se toma como titular de la cuenta.

**Gestión de Proyectos**
- 🔧 Las tarjetas de Usuarios cuentan lo filtrado («4 de 15») y caben en el teléfono.
- 🐞 En los grupos de una sola opción, como la fórmula del costo estimado al terminar, ya no se puede apagar la que
  manda.

**Planoteca**
- ✨ Nueva herramienta: los planos de cada obra con su revisión vigente —la última aprobada con oficio— y el historial de cada plano.
- ✨ Subir planos y revisiones y registrar el oficio que las aprueba, con permisos por persona y por planoteca.

---

## 2026-09-25

**Bitácora de Obra**
- 🐞 Una obra apagada ya no le sale a nadie para trabajar, y «Volver a lo de siempre» ya no la vuelve a encender.
- 🔧 Administración › Obras en una tabla con columnas que se ensanchan a mano; apagar una obra con gente o con informes
  pregunta con los números.

**Registro de Horarios**
- ✨ «Instalar la app»: un botón que deja la app en el celular con su ícono, en cualquier equipo.

---

## 2026-09-24

**Bitácora de Obra**
- 🔧 Espacio compacto y una letra hecha para leerse bien: caben sin deslizar 170 de 207 combinaciones de pantalla y
  ancho (antes 122).
- 🔧 El código de vía propuesto por la malla vial, encendido en las cinco obras de malla vial de Bogotá.

**Registro de Horarios**
- 🔧 En Personas el rol se ve y se cambia desde la lista, con el centro de nómina y el asignado en columnas separadas;
  las tablas se acomodan al ancho y sus columnas se ensanchan a mano.

---

## 2026-09-23

**Bitácora de Obra**
- ✨ El código de vía (CIV) lo propone la malla vial de Bogotá según la ubicación del teléfono, y lo escrito a mano se
  comprueba. Se enciende obra por obra.
- ✨ Preguntas frecuentes: 33 preguntas con buscador, legibles sin entrar, y la ayuda de cada pantalla.
- 🔧 Administración: la obra abre con lo que cambió, y dar acceso a una obra busca y guarda al tocar, sin 69 casillas.
- 🔧 Encabezado y menú en el azul del ERP, seis tamaños de letra y ninguno bajo 12, y un tema oscuro legible a
  contraluz.
- 🔧 La ubicación se busca desde que se abre Registrar cantidad; sin ella se elige el motivo. Los materiales se guardan
  sin señal y lo guardado en el teléfono se puede descartar.
- 🔧 «Devolver con motivo» es el mismo cuadro en el informe y en Informes de obra; el período se escribe igual en todas
  las listas y los filtros viajan en el enlace.
- 🐞 Las fotos de antes del 10 de septiembre ya no repiten código, fecha y código de vía en el pie del impreso.

**Registro de Horarios**
- 🔧 Administración en cinco secciones: Inicio con lo que está quieto y «Recordarles a los jefes», Personas en una sola
  ficha, Centros, Horarios y Sistema con el registro de cambios en palabras.

**Biblioteca de Informes**
- 🔧 Se entra con la cuenta de correo de la empresa, sin pedir código. El código por correo sigue para los invitados de
  fuera del grupo.

---

## 2026-09-22

**Portal de Proveedores**
- 🐞 Una cédula en foto JPG ya no hace fallar la lectura de todo el expediente.
- 🐞 «Reemplazar» un documento toma el archivo nuevo.

**Bitácora de Obra**
- 🔧 Informes de obra: «Lo que falta hoy» por persona, un período a la vista, el calendario del mes y un solo
  «Descargar» que baja lo que se ve.
- 🔧 Sin señal, una franja dice cuántas cosas quedaron en el teléfono y las sube sola al volver la señal; la falta de
  red ya no gasta intentos.
- 🔧 Tema, letra, densidad y pantalla de inicio se guardan en la cuenta y siguen a la persona a otro teléfono.
- ✨ El administrador puede ver la app como la ve otra persona, sin poder guardar nada.

**Registro de Horarios**
- 🔧 El centro de costo lleva la píldora de su empresa y el número de contrato completo en toda la app.
- 🐞 Enviar varios días de un centro sin jefe no le avisaba a nadie; ahora el aviso va por centro y le dice «SIN JEFE»
  al administrador.
- 🔧 El correo de varios días a la vez muestra el rango y las horas sumadas; el reintento solo manda avisos de las
  últimas 48 horas.
- 🔧 «Quién aprueba» muestra a los recién nombrados jefes y busca por cargo y proyecto.

---

## 2026-09-21

**Registro de Horarios**
- ✨ «Qué avisos recibo»: cada persona elige sus avisos por concepto y por canal (app o correo).
- 🐞 El jefe no recibía el «devuelto» de un día que él había aprobado.
- 🐞 Los totales de la planilla salían corridos una columna cuando había columnas ocultas.
- 🔧 La planilla con rejilla como el Excel de Gestión Humana y el TOTAL fijo al pie.

---

## 2026-09-18

**Portal de Proveedores**
- 🔧 Los datos del paso «Datos» del asistente van en campos agrupados, no en una tabla.

**Bitácora de Obra**
- 🔧 Registrar una cantidad: los pasos salen de lo que pide la obra (tres en obra vial), «Guardar» siempre a la vista y,
  al guardar, seguir con otra del mismo ítem o con otro ítem.
- 🔧 La pantalla habla como la obra: un nombre para cada cosa y ninguna sigla interna.
- 🔧 Firmar y enviar, aprobar o aceptar es un solo botón, con el resumen del informe y la firma que va a quedar a la
  vista.
- ✨ Quien firma informes dibuja su firma la primera vez que entra.

---

## 2026-09-17

**Portal de Proveedores**
- 🔧 El administrador decide cuántos días antes y de qué documentos se recuerda el vencimiento, y si va un correo por
  proveedor.
- ✨ A un tercero se le pueden callar los recordatorios, o todos los correos, con el motivo a la vista.

**Bitácora de Obra**
- 🔧 El informe del día se llena en seis pasos, uno a la vez, y «Antes de enviar» lleva a lo que falta.
- ✨ «Para ti hoy»: al abrir, lo que te toca hoy y un botón para hacerlo; además se elige qué pantalla abre la app.

---

## 2026-09-16

**Asistente por WhatsApp**
- ⚠️ El certificado de parafiscales sale firmado por quien firma en cada empresa, y el aviso dice quién lo firmó; si
  falta la firma, dice quién debe ponerla. Corrige el «sale sin firma» del 15 de septiembre.
- 🔧 El correo de la rutina mensual de los robots nombra a las empresas que dejaron de salir frente al mes anterior; se
  apaga desde el panel de robots.

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
