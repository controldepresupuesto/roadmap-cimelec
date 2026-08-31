# Plantilla de nota de versión

Copiar, llenar y pegar al principio del `CHANGELOG.md`.
Borrar las secciones que no apliquen — una sección vacía es ruido.

```markdown
## AAAA-MM-DD

**Nombre de la herramienta**
- ✨ Algo que antes no existía.
- 🔧 Algo que ya existía y ahora funciona mejor o más rápido.
- 🐞 Algo que estaba mal y quedó bien. Decir qué se veía mal.
- ⚠️ Algo que cambió de comportamiento y hay que saberlo antes de usarlo.

**Otra herramienta**
- ✨ ...
```

## Los cuatro marcadores

| Marcador | Cuándo |
|---|---|
| ✨ **Nuevo** | No existía. Una pantalla, un informe, un campo, un filtro |
| 🔧 **Mejorado** | Existía y quedó mejor: más rápido, más claro, con menos pasos |
| 🐞 **Corregido** | Estaba mal. **Decir qué se veía mal**, para que quien lo sufrió lo reconozca |
| ⚠️ **Cambio de comportamiento** | Algo funciona distinto a como el usuario lo aprendió. Va primero en la lista |

## Ejemplos

**Mal** — dice lo que se tocó por dentro:
> - Refactor del cálculo de la medida de facturación acumulada.

**Bien** — dice qué cambió para quien la usa:
> - 🐞 La facturación acumulada sumaba dos veces las notas crédito del mes de cierre.
>   Las cifras de junio y julio quedaron corregidas.

**Mal** — no se entiende el impacto:
> - Se agregó validación al formulario.

**Bien**:
> - ⚠️ El formulario ya no deja guardar un registro sin CIV. Si estabas dejándolo en
>   blanco para llenarlo después, ahora hay que ponerlo desde el principio.
