Backend
====

1. Create a new virtual environment:

        python3 -m venv env

2. Activate the environment:

        source env/bin/activate

3. The environment has to be activated for the rest of the commands.

4. Install dependencies:

        pip install -r requirements.txt

5. Initialize the database:

        python manage.py migrate

6. Create superuser:

        python manage.py createsuperuser

7. Start the development server:

        python manage.py runserver


### Deployed
The application is currently online at the address

    https://harfilemanagement.pythonanywhere.com

## App information.

#### Endpoint

<a target="_blank" href="https://harfilemanagement.pythonanywhere.com/api/v1/auth/">Auth enpoind</a>

<a target="_blank" href="https://harfilemanagement.pythonanywhere.com/api/v1/file/">File enpoind</a>

#### Django Admin

<a target="_blank" href="https://harfilemanagement.pythonanywhere.com/admin/">Login</a>