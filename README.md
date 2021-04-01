Simple aplicacion CRUD de ordenes de pedidos

Pasos
 * Crear modelos : Ordenes, Procesos, Ordenes_procesos
 * Crear index
 * Crear lista/
 * Crear detalle
 * edicion
 * eliminar 

Crear un proj
 * djang-admin startproject $nombre

Pasos para crear una app en el proj
 * python3.9 manage.py startapp $app
 * agregar '$app' en /$proj/settings.py 
   - APP_INSTALLED = [... '$app'] 

== MODELOS ==

Pasos para crear un modelo
 * Definir la neuva clase en app/models.py

Generar SQL de los modelos
 * python3.9 manage.py makemigrations $app
     El sql generado sera guardado en /$app/migrations/000*

Ejecutar SQL para la db
 * python3.9 manage.py migrate 

Ejemplos:

TITLE_COICES = [
	('MR', 'Mr.'),
	('MRS', 'Mrs.'),
]
class Author(models.Model):
	title = models.CharField(max_length=3, choices=TITLE_CHOICES)

===============

Pasos para crear una vista:
 * Definir clase o func en app/views.py
 * Agregar .html en templates/app_name/nombre_$.html
 * Nueva url en app/urls.py
    - from django.urls import render
    - from django.generic.view.detail import DetailView
 * Nueva entrada en app_proj/urls.py
 * Agregar {% url '$app_name:path' var %} a la vista que la referencia

Pasos para crear un form
 * Necesito una vista que contenga al form
 * Un template
 * Un modelo
 * Relacionar el form con el modelo
 * Retornar el template con el form
 * Enviar el form


































