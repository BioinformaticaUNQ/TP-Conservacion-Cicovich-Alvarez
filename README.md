# Graficador de zonas conservadas de proteínas

## Backend

Las rutas estan ubicadas en el archivo `urls.py`. Alli se encuentran los endpoints necesarios para utilizar el programa desde el frontend.
Por e

## `main.py`
 El archivo `main.py` contiene los pasos necesarios para generar las zonas conservadas de una proteína y viene configurado con un ejemplo.
 Se pueden modificar los parametros: PDB_ID, e-value maximo, porcentaje de conservación para la secuencia consenso.
 
 Con solo correrlo el programa descargará los archivos necesarios de Blast, Clustal y PDB para poder hacer las comparaciones.
 Todos los archivos serán alojados en una carpeta `repository`.
 El programa `main` imprimirá por consola los resultados, primero una lista de tuplas (Aminoacido, porcentaje) donde se mostrará el porcentaje de conservación del aminoacido con mas apariciones.
 Tambien se verá la secuencia consenso que supere el valor porcentual que se ingreso.
 
 ## `dssp.py`
 Es obligatorio correr el archivo `dssp.py` luego de haber ejecutado `main.py`. Este programa nos mostrara la estructura secundaria consenso y la lista de pares (Estructura del aminoacido, porcentaje) en el mismo formato que `main.py`  
 

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
