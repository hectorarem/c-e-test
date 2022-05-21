Backend
====
## Desarrollo

2. Crear un nuevo entorno virtual:

        python3 -m venv env

3. Activar el entorno:

        source env/bin/activate

4. El entorno tiene que estar activado para el resto de los comandos.

5. Instalar las dependencias:

        pip install -r requirements.txt

6. Inicializar la base de datos:

        python manage.py migrate

7. Crear superusuario:

        python manage.py createsuperuser

8. Arrancar el servidor de desarrollo:

        python manage.py runserver

