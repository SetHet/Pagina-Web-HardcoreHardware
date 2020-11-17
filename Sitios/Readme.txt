Descripcion

    Sitio web oficial: prueba_django
	

    Super usuarios de sitio_hh:
        admin : 1234    

Instrucciones

    Para iniciar el servidor:
    >> python manage.py runserver

    Para cerrar el servidor:
    >> CTRL-BREAK (Ctrl+C)

    Migrar
    >> python manage.py migrate

    Crear Administrador
    >> python manage.py createsuperuser
    >> ...Ingresar lo que pida

    Crear nueva aplicacion
    >> python manage.py startapp core

    Migrar models a la BD
    >> python manage.py makemigrations nombre_app_bd
    >> python manage.py migrate nombre_app_bd

Historial de comandos sitio_hh

>> django-admin startproject sitio_hh
>> cd sitio_hh
>> python manage.py runserver
>> CTRL-BREAK
>> python manage.py migrate
>> python manage.py createsuperuser
>>>> admin
>>>> admin@hh.cl
>>>> 1234
>>>> 1234
>> python manage.py startapp core
>> python manage.py runserver
// Creando la base de datos
>> python manage.py startapp productos
    internamente editar productos/models.py
>> python manage.py makemigrations productos
>> python manage.py migrate productos