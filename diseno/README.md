# Diseño de la hoja de ruta como página

Una propuesta de cómo se vería esta hoja de ruta servida como página propia, con la marca de la
casa, en lugar de la interfaz del tablero. **No está en servicio**: el tablero público sigue siendo
la hoja de ruta de verdad. Esto se guarda para no rehacerlo el día que se decida publicarla.

Dos pantallas:

| Archivo | Qué es |
|---|---|
| `Main.dc.html` | Escritorio, 1440 px |
| `Movil.dc.html` | Teléfono, 390 px |
| `canvas.json` | Cómo se acomodan las dos en el lienzo |
| `datos.py` | Mete en las dos pantallas las solicitudes reales del tablero y la fecha |

La página muestra las cifras del momento, cuánto lleva publicado cada herramienta y la lista de
solicitudes, que se puede filtrar por estado y por herramienta. Ninguna cifra está escrita a mano:
todas se calculan de la lista, y la lista sale del tablero.

## Volver a armarla

```bash
gh issue list --repo controldepresupuesto/roadmap-cimelec --state all --limit 100 \
   --json number,title,state,labels > roadmap.json
python datos.py
```

Eso deja las dos pantallas al día. El archivo que se abre en el navegador se genera aparte y no se
guarda aquí —pesa 2,5 MB— igual que el volcado del tablero: los dos salen del comando de arriba.
