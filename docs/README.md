# Guía de instalación de la página de adopción

## Tabla de contenido

1. [Instalación de dependencias](#instalación-de-dependencias)
    1. [Instalación de python](#instalación-de-python)
    2. [Instalación de mkvirtualenv](#instalación-de-mkvirtualenv)
2. [Clonar el proyecto](#clonar-el-proyecto)
3. [Crear y decargar dependencias del entorno](#crear-y-descargar-dependencias-del-entorno)
4. [Aplicar la última migración de la base de datos](#aplicar-la-última-migración-de-la-base-de-datos)

## Instalación de dependencias

### Instalación de python

```commandline
sudo apt install python
```

### Instalación de mkvirtualenv

```commandline
pip install virtualenv
```

## Clonar el proyecto

Nos colocamos en la carpeta donde deseemos tener el proyecto almacenado y ejecutamos el siguiente comando
*TODO: Agregar dirección de github donde tenga mi repositorio almacenado*

```commandline
git clone 
```

## Crear y decargar dependencias del entorno

Nos colocamos en la carpeta donde tendremos el proyecto y ejecutamos

```commandline
mkvirtualenv adopciones -p=2.7
```

Instalamos las dependencias que requiere python para poder usarse

```commandline
pip install -r requirements.txt
```

**NOTA:**
Para apagar el entorno que hemos creado podemos usar el siguiente comando, devemos tener el entorno activado

```commandline
deactivate
```

Para prender el entorno que creamos usaremos el siguiente comando

```commandline
workon adopciones
```

Verifica que se haya descargado la versión 2.7 de python

```commandline
python -V
```

Ejecutamos el siguiente comando para descargar las dependencias del proyecto

```commandline
pip install
```

## Aplicar la última migración de la base de datos

Estando el entorno activado y dentro de la carpeta raíz donde se encuentra el archivo manage.py, ejecutamos el siguiente
comando

```commandline
python manage.py migrate 
```

## Inicializar el proyecto

Estando el entorno activado y dentro de la carpeta raíz donde se encuentra el archivo manage.py, ejecutamos el siguiente
comando

```commandline
python manage.py runserver
```