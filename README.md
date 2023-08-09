## Django API rest

Crear entorno virtual
 > python3 -m virtualenv env

Instalar Django y Framework REST

 > pip install django

 > pip install djangorestframework

Crear proyecto llamado ninjaAPI

(Importante poner un punto al final para que el proyecto se cree en la misma carpeta)

 > django-admin startproject ninjaAPI .

Inicializarlo

 > python3 manage.py runserver

Crear aplicación (CRUD)

>  python3 manage.py startapp projects

Dentro del proyecto (ninjaAPI) en setting añadimos las aplicaciones prjects y rest_framework.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
    'rest_framework',
]

Vamos al modelo de proyecto y creamos nuestro modelo de datos.

Posteriormente guardamos y realizamos la migracion de los modelos con el comando:

> python3 manage.py makemigrations

para utilizarlo escribimos el comando:

> python3 manage.py migrate

Ya tenemos el modelo creado.

Pasamos a crear los endpoints.

Creamos en projects el archivo serializer.py, el cual nos va a permitir llamar a un modelo especial del framework.

Creamos en projects el archivo api.py, el cual nos va a permitir establecer usuarios y permisos.
 
class ProjectViewset(viewsets.ModelViewSet)
    queryset = Project.objects.all()
    permissions_classes = [permissions.AllowAny] Para cualquier usuario
        permissions_classes = [permissions.auth] Para autentificar

Pasamos a crear las url y rutas.

Creamos un archivo urls.py en projects e importamos router desde rest_framework.
.register crea 4 urls (GET, POST, PUT,  DELETE).
Una vez creado patternurls para exportar las rutas a la aplicación principal. Para ello:

 En la carpeta django_api -> urls.py.
 añadimos el path nuevo (importante importarlo primero)

Una vez tenemos el servidor, pasamos a crear el cliente REST (minuto 23:00)

Swagger:

instalar con el comando:

> pip install django-rest-swagger.

Añadir al setting.py (carpeta django-api):

INSTALLED_APPS = [
    ...
    'rest_framework_swagger',
    ...
]

### Documentación Swagger
https://django-rest-swagger.readthedocs.io/en/latest/schema/





Desplegar proyectos con render