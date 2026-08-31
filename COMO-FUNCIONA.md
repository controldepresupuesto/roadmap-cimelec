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

El **estado** vive en dos lados a propósito: en el label (se ve en la lista de issues) y
en el campo del Project (permite agrupar el tablero). El script de cambio de estado los
mueve juntos; si los cambias a mano, cambia los dos.

---

## Rutina semanal (10 minutos)

1. **Vaciar la bandeja.** Todo lo que llegó por WhatsApp o correo se registra:
   doble clic en `NUEVA-SOLICITUD.bat`.
2. **Mover lo que se movió.** Lo que empezó pasa a `en curso`; lo que se terminó, a
   `en prueba`; lo que se publicó, a `publicado` y se cierra.
3. **Poner fecha objetivo** a lo que entró en curso. Sin fecha, la vista Hoja de ruta
   no lo dibuja.
4. **Revisar lo pausado.** Si algo lleva más de dos meses pausado, decide: o vuelve, o
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
| `crear-tablero.ps1` | **Una sola vez** | Crea el tablero con sus campos, lo hace público y le mete las solicitudes |
| `nueva-solicitud.ps1` | Cada vez que llega algo por WhatsApp o correo | Registra la solicitud y devuelve el enlace |
| `publicar-actualizacion.ps1` | Cada vez que sale algo a producción | Entrada en el CHANGELOG + Release |

### El permiso de tableros

`crear-tablero.ps1` necesita un permiso que `gh` no trae por defecto. Una sola vez:

```
gh auth refresh -s project
```

Abre el navegador, confirmas y queda. Sin eso, GitHub no deja crear ni modificar tableros
desde la línea de comandos.

### Las dos cosas que GitHub no deja automatizar

1. **Las vistas del tablero** (Tablero y Hoja de ruta). Se crean con unos clics en la web,
   una sola vez. El script imprime los pasos exactos al terminar.
2. **Poner una solicitud nueva en el tablero.** `nueva-solicitud.ps1` crea la solicitud pero
   no la agrega al tablero. Se arrastra a mano, o se activa el flujo automático del propio
   tablero: en el tablero → `⋯` → *Workflows* → **Item added to project** → activarlo, y
   además **Auto-add to project** con el filtro `is:issue is:open repo:roadmap-cimelec`.

### El límite de escritura caduca

El candado que impide que un tercero escriba tiene dos capas:

- **Interaction limit** de GitHub: efectivo, pero **caduca a los 6 meses**. Se renueva
  volviendo a correr `configurar-repo.ps1`.
- **`.github/workflows/solo-equipo.yml`**: no caduca. Si alguien de afuera escribe, le
  responde, cierra y bloquea el hilo.

La primera es la que evita el ruido; la segunda es la que garantiza que nunca queda abierto.
