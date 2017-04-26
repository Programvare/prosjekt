# BoTA
Making learing better.

## How to Install BoTA Locally:

1. Clone the GitHub repo
2. Open the files in your preffered API. We recommend using PyChar, as this was our development API and it has worked quite well for us.
3. Install Django. This can be done via the 'pip' installer. Simply run the 'pip3 install Django' in the command line, or use PyCharms plugin installer.
4. When everything is installed, you need to setup a run/debug configuration. Choose Django, and make sure that you are using Python 3.4.4. Copy this as your enviromental variables:

```DJANGO_SETTINGS_MODULE=bota.settings;PYTHONUNBUFFERED=1```

5. When this is done, you will need to setup the database. This can be done in command line by running these commands inside the C:\...\YOUR_FOLDER\prosjekt\bota>
```
    python manage.py makemigrations
    python manage.py migrate
```

6. You should now be ready to use BoTA! If you want to create a administrator user, you will need to run the following command in the same folder as earlier, and follow the instructions:

```
python manage.py createsuperuser
```
