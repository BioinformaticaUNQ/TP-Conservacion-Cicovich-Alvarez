# Graficador de zonas conservadas de proteínas

## Resumen

El programa recibe como input un `PDB_ID` (1LXA por ejemplo) que será utilizado para traer un archivo llamado `seq.fasta`, luego busca por similitud secuencial en la base de datos de PDB, el resultado se alojará en `clustal.fasta`.
Estas secuencias seran filtradas por el parametro `E_VALUE_REQUIRED`, las busquedas que superen ese valor no seran consideradas a la hora de alinear.
En ese momento se utilizara el programa `clustalw` de la linea de comando de linux o windows (indicar su correspondiente path) y escribirá un archivo `aligned.fasta `. Se ejecutará un algoritmo para determinar las zonas conservadas.
Este algoritmo utiliza un valor procentual parametrizable llamado `CONSERVATION_PORCENTAGE`. Este parametro indica el porcentaje minimo requerido de apariciones de un aminoacido para pertenecer a la secuencia consenso.
En el caso de que una columna de aminoácidos tenga mas gaps (-) que aminoacidos, se considerarán solo residuos para calcular el porcentaje.


 
## Comandos utiles

```bash
pip install pipenv #Instalar PipEnv
```
```bash
pipenv shell #Montar ambiente
```
```bash
pipenv update #Actualizar dependencias
```
```bash
pipenv install biopython #Montar agregar dependencia
```
```bash
pipenv run py manage.py runserver #Iniciar django desde pipenv
```
