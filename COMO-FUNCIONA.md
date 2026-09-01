# Cómo se mantiene este tablero

Runbook para quien administre el roadmap. Diez minutos por semana bien puestos y esto se
mantiene solo; sin eso, en un mes está desactualizado y deja de servir.

---

## Las piezas y para qué sirve cada una

| Pieza de GitHub | Aquí se usa para |
|---|---|
| **Issue** | Una solicitud: una mejora, un error o una idea. Es la unidad de todo |
| **Labels** | Clasificar: `app:` (qué herramienta) · `tipo:` · `estado:` · `prioridad:` |
| **Project** (Projects v2) | El tablero. Se alimenta solo de los issues. Tiene vista Tablero y vista Hoja de ruta |
| **Milestone** | Agrupar por mes de entrega |
| **Release** | Cada publicación, con su nota de versión |
| **CHANGELOG.md** | Lo mismo que los Releases, pero en una sola página que se lee de corrido |

**La etiqueta es la fuente de verdad, el tablero es su reflejo.** El estado se cambia en la
etiqueta del issue (`estado: en desarrollo`) y `SINCRONIZAR-TABLERO.bat` lo copia al campo del
tablero. Nunca al revés: si lo cambias solo en el tablero, la siguiente sincronización lo
devuelve a lo que diga la etiqueta.

Dos rarezas del tablero, por si extrañan:

- El campo de estado se llama **`Status`**, en inglés, y no se puede cambiar. GitHub no
  permite renombrar ni borrar ese campo: la operación de renombrado **responde que tuvo
  éxito y no hace nada**. Las opciones sí son las nuestras, en español. Se dejó el de
  fábrica y se eliminó el duplicado en español, para no tener dos campos de estado.
- Las etiquetas `app:` alimentan el campo **Herramienta** y las `prioridad:` el campo
  **Prioridad**. Mismo principio: se cambia la etiqueta.

---

## Rutina semanal (10 minutos)

1. **Vaciar la bandeja.** Todo lo que llegó por WhatsApp o correo se registra:
   doble clic en `NUEVA-SOLICITUD.bat`.
2. **Mover lo que se movió.** Cambia la **etiqueta** de estado: lo que empezó pasa a
   `estado: en desarrollo`; lo que se terminó, a `estado: en pruebas`; lo que salió pero
   solo para unas áreas, a `estado: en implementacion`; lo que ya usa todo el mundo, a
   `estado: publicado` y se cierra.
3. **Reflejarlo en el tablero.** Doble clic en `SINCRONIZAR-TABLERO.bat`. Agrega lo nuevo,
   corrige lo que cambió y no toca lo demás.
4. **Poner el `Periodo`** (el trimestre) a lo que entró en backlog o en desarrollo, en el
   tablero. Sin `Periodo` la vista Hoja de ruta no lo dibuja. Es lo único que se escribe en
   el tablero y no en la etiqueta.
5. **Revisar lo pausado.** Si algo lleva más de dos meses pausado, decide: o vuelve, o
   pasa a `no va` con el motivo escrito.

## Cuando se publica algo

1. Doble clic en `PUBLICAR-ACTUALIZACION.bat`. Pide la fecha y los cambios, arma la
   entrada del `CHANGELOG.md` y crea el Release.
2. Cierra los issues que salieron en esa versión y menciona el número de versión en
   cada uno. Así el usuario que pidió algo ve dónde salió.

---

## Reglas de redacción

Esto lo lee gente de obra y de contabilidad, no de sistemas.

1. **Nombra la herramienta, no el componente.** "Tablero DataMart", no el nombre del
   servicio ni del contenedor.
2. **Nada de infraestructura.** Ni servidores, ni puertos, ni proveedores de nube, ni
   nombres de base de datos, ni URLs internas. Este repositorio es público.
3. **Nada de datos reales de terceros.** Ni NIT, ni cédulas, ni nombres de personas, ni
   valores de contratos. En los pantallazos, tapar.
4. **Ni una cifra de dinero** que no sea ya pública.
5. **Un cambio, una línea.** Si no se puede resumir en una línea, son dos cambios.
6. **Se escribe qué cambió para el usuario**, no qué se tocó por dentro. "Ahora el botón
   Editar abre el registro que estabas viendo" — no "se agregó un parámetro a la URL".
7. **Lo que no se va a hacer también se publica**, con el motivo. Es la parte que genera
   confianza; una lista donde todo está "en análisis" para siempre no la genera.

---

## Qué NO va en este repositorio

- Código. Vive en los repositorios privados.
- Credenciales, claves, tokens, cadenas de conexión — jamás, ni en un pantallazo.
- Documentos de la empresa: RUT, cámaras de comercio, cédulas, firmas, contratos.
- Respaldos, exportaciones de datos, archivos de Excel con información real.
- El detalle de un incidente de seguridad mientras esté abierto.

---

## Si alguien de afuera escribe

El flujo `.github/workflows/solo-equipo.yml` le responde, cierra y bloquea. No hay que
hacer nada. Si es alguien del equipo que aún no está invitado, invítalo como
**colaborador con rol Triage** (puede abrir y clasificar, no puede tocar el contenido).

---

## Los scripts

Todos viven en `scripts/`. Los tres con `.bat` en la raíz se corren con doble clic.

| Script | Cuándo se corre | Qué hace |
|---|---|---|
| `configurar-repo.ps1` | Una vez, y cada 6 meses | Etiquetas, hitos, apaga la wiki y limita la escritura al equipo |
| `crear-tablero.ps1` | **Ya se corrió** (31-ago-2026) | Creó el tablero. No volver a correrlo: crearía un segundo tablero |
| `sincronizar_tablero.py` | Cada vez que cambias una etiqueta | Copia estado, herramienta y prioridad de las etiquetas al tablero. Repetible |
| `configurar_tablero.py` | Al cambiar estados, o al añadir una herramienta | Estados, campo `Periodo` con sus trimestres, y las vistas. Repetible |
| `auditar_etiquetas.py` | Solo, con cada sincronización | Falla si el vocabulario se degrada: dos estados a la vez, una etiqueta que el mapa no conoce |
| `vigilante_roadmap.py` | Solo, los lunes a las 8:30 | Revisa que el roadmap no se esté podriendo. Avisa en el escritorio **solo** si hay algo que exige acción |
| `proponer_desde_commits.py` | Solo, los lunes | Lee lo que se construyó y propone qué falta contar en el roadmap |

### Cómo entra lo que se construye, sin que nadie lo apunte

El registro de lo que se hizo **ya existe**: son los commits de los repositorios. Los escribió
quien hizo el trabajo, están fechados, y no dependen de que alguien se acuerde de anotar nada.

`proponer_desde_commits.py` los lee y los reparte en tres cajones:

| Cajón | Qué cae ahí |
|---|---|
| **Probablemente sí** | Cambios que un usuario notaría. Van a `_PROPUESTAS-ROADMAP.md` con una casilla |
| **Probablemente no** | Despliegues, notas, versiones. Se listan aparte, por si acaso |
| **Nunca** | Infraestructura, pruebas, credenciales. Solo se cuentan — la regla del repositorio público los excluye por definición |

**No publica nada.** Marca en el archivo lo que quieras que entre, dímelo, y lo redacto en
lenguaje de negocio y lo cargo. Capturar es lo que se olvida; revisar son treinta segundos.

Se descartó hacerlo con un *hook* de la sesión: capturaría menos que los commits, añadiría peso
a cada sesión, no funcionaría hacia atrás, y dependería de que la sesión terminara bien.

### Lo que corre solo, sin que nadie lo pida

Dos tareas programadas de Windows, con el mismo patrón que las del bot y del panel:

| Tarea | Cuándo | Qué hace |
|---|---|---|
| `Roadmap CIMELEC - Sincronizar tablero` | cada 10 min y al iniciar sesión | Proyecta las etiquetas sobre el tablero |
| `Roadmap CIMELEC - Vigilante` | lunes 8:30 | Revisa que nada se esté podriendo |

Ninguna necesita un token nuevo: usan el `gh` de la máquina, que ya está autorizado.

**Cómo saber si están vivas**, sin entrar a ninguna parte:

| Archivo | Qué dice |
|---|---|
| `_estado-sincronizacion.txt` | Se reescribe siempre. Si la fecha se queda vieja, la sincronización murió |
| `sincronizacion.log` | Solo anota cuando hubo cambios o fallos |
| `_VIGILANTE-ROADMAP.txt` | El informe del lunes, completo, haya avisado o no |

Ninguno de los cuatro se publica.

**El límite conocido:** las dos dependen de que este computador esté encendido y con la sesión
abierta. El vigilante lo detecta a sí mismo — si la sincronización lleva más de 3 horas sin correr,
lo reporta. Y si un lunes no llega ni el aviso ni el informe, el vigilante también está caído.
La alternativa que no depende de esta máquina es el flujo de GitHub Actions, que está escrito y
apagado esperando un token.
| `nueva-solicitud.ps1` | Cada vez que llega algo por WhatsApp o correo | Registra la solicitud y devuelve el enlace |
| `publicar-actualizacion.ps1` | Cada vez que sale algo a producción | Entrada en el CHANGELOG + Release |

### El permiso de tableros

`crear-tablero.ps1` necesita un permiso que `gh` no trae por defecto. Una sola vez:

```
gh auth refresh -s project
```

Abre el navegador, confirmas y queda. Sin eso, GitHub no deja crear ni modificar tableros
desde la línea de comandos.

### El modelo: de dónde salió

Está copiado del **roadmap público de Sincosoft**, los autores del ERP SINCO
(`github.com/orgs/SincosoftSAS/projects/3`): estados con descripción, un campo de trimestre
para la línea de tiempo, etiquetas temáticas, y una vista por producto además de las tres
globales.

Dos cosas se hicieron distinto, a propósito:

1. **Ellos no publican lo que se descarta.** Aquí sí: `Pausado` y `No va` existen, con el
   motivo escrito. Saber que algo no se va a hacer sirve tanto como saber que sí.
2. **Su campo de trimestre quedó abandonado** — la última iteración que definieron es
   `2024 T2`, y su vista Roadmap no tiene nada que la dibuje. Aquí los trimestres se
   **pre-generan** hasta `2028 T4`, que es exactamente el modo de falla que se les vio.
   Cuando se acaben, se amplía `TRIMESTRES_HASTA` en `configurar_tablero.py` y se vuelve a
   correr.

Ellos tienen un repositorio público por producto (28 en total) y filtran cada vista por
`repo:`. Aquí todo vive en un solo repositorio y las vistas filtran por
`label:"app: ..."` — mismo resultado con una novena parte de la configuración.

### Lo único que sigue siendo manual

Nada del tablero: estados, campos y vistas se crean por API con `configurar_tablero.py`.

Lo único que conviene activar a mano, una vez, es que las solicitudes nuevas entren solas al
tablero: en el tablero → `⋯` → *Workflows* → **Auto-add to project**, filtro
`is:issue is:open repo:roadmap-cimelec`. Sin eso, `SINCRONIZAR-TABLERO.bat` las mete igual,
pero solo cuando lo corras.

### El límite de escritura caduca

El candado que impide que un tercero escriba tiene dos capas:

- **Interaction limit** de GitHub: efectivo, pero **caduca a los 6 meses**. Se renueva
  volviendo a correr `configurar-repo.ps1`.
- **`.github/workflows/solo-equipo.yml`**: no caduca. Cubre las tres formas de escribir que
  tiene un desconocido — abrir una solicitud, comentar y abrir un *pull request* desde un
  fork — y en cada caso responde, cierra y bloquea. Un comentario ajeno no se borra: se
  colapsa como fuera de tema, así queda consultable sin quedar destacado.

  Los *forks* **no se pueden desactivar** en un repositorio público de cuenta personal
  (GitHub solo lo permite en organizaciones), así que cerrar los PR es la única defensa
  posible por ese lado.

La primera es la que evita el ruido; la segunda es la que garantiza que nunca queda abierto.
