# Cambios posteriores a la demo

## Mejoras en la interacción con el usuario.
- Agregamos labels en la pagina de inicio para reconocer mejor los campos.

![inicio](inicio.png)

- Explicitamos claramente los labels de conservacion 1° y 2°

![conservacion](conservaciones.png)

## Testing

- Agregamos tests a los algoritmos de conservacion primaria y secundaria y al fetching de datos de PDB.

![test](tests.png)

## Gaps de Clustal
Teniamos un inconveniento con `clustalw`, figuraban gaps en todas las secuencias alineadas en una misma posicion.

![gaps](gaps.png)

- Modificamos la penalidad de los gaps en `clustalw` y solucionamos el problema.


 ![clustal](clustal.png)