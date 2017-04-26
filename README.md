# BoTA
Making learing better.

You can find us online at: http://bota-app.com. 
To try out the admin features, login as ‘admin’ with the password ‘passord1’. 
Otherwise, to use the website as a regular user, simply sign up.

## How to Install BoTA Locally:

1. Clone the GitHub repo
2. Open the files from the bota folder(deployment folder is for heroku only) in your preffered API. We recommend using PyCharm, as this was our development API and it has worked quite well for us.
3. Install Django. This can be done via the 'pip' installer. Simply run the 'pip3 install Django' in the command line, or use PyCharms plugin installer.
4. When everything is installed, you can either skip this part if you intend to use the Terminal. Otherwise, if you intend to use PyCharm to run the site, you need to setup a run/debug configuration. Choose Django, and make sure that you are using Python 3.4.4. Copy this as your environmental variables:

```
    DJANGO_SETTINGS_MODULE=bota.settings;PYTHONUNBUFFERED=1
```

5. When this is done, you will need to setup the database. This can be done in command line by running these commands inside the C:\...\YOUR_FOLDER\prosjekt\bota>
```
    python manage.py makemigrations
    python manage.py migrate
```

6. You should now be ready to use BoTA! If you want to create a administrator user, you will need to run the following command in the same folder as earlier, and follow the instructions:

```
    python manage.py createsuperuser
```

7. You can now run the site through PyCharm or if you are using the Terminal, you need to run the following command in the same folder to run the local server:

```
    python manage.py runserver
```


## Coverage

We have also included a whole website with coverage data. This website can be found by:
1. Open the cover folder
2. Open index.html in the browser of your own choosing

