Lista de ambientes virtuales

enviroment Server 0:
    Es el VENV inicial del servidor de Django
    Se creo con la base de Python 3.8.5
    Tiene instalado 
        Django 2.2.16
        Pip 20.2.4
        Pylint 2.6.0
            >> astroid-2.4.2 colorama-0.4.4 isort-5.6.4 lazy-object-proxy-1.4.3 mccabe-0.6.1 pylint-2.6.0 six-1.15.0 toml-0.10.2 wrapt-1.12.1
        ..


Comandos:

>> cd mis_ambientes
>> python -m venv venv_nombre
>> venv_nombre\Scripts\activate
>> python -m pip install --upgrade pip
>> pip install django==2.2.16
>> pip install pylint
>> cd ..
>> python Sitios\sitio_hh\manage.py runserver