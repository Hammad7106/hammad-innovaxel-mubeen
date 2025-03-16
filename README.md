# hammad-innovaxel-mubeen
Url Shortner Home Assignment

# SET UP INSTRUCTIONS

1- Clone this repository by git clone repo-name.

2- Set up Database in MySQL and integrate with Django. In Project's settings.py add DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

3- Install Project Requirements by pip install -r requirements.txt.
4- Apply migrations by python manage.py migrate.
4- After that run the server by python manage.py runserver.
5- Your Project is now running on your local server.

# PROJECT GO THROUGH
This API's of this project are built in REST with the help of Django Rest Framework.

1- CREATE SHORT URL.
When you will run the project then a front-end page will appear which asks for the url you want to shorten. You will paste your desired url and in return it will generate the Short URl for your original URL.

2- GET ORIGINAL URL, UPDATE URL, DELETE URL
When we click on the Short URl which we got from create url page then we will have all the options to get original url, update the url and delete the url. Instead we can also go to the url like http://127.0.0.1:8000/your_short_url/

3- STATISTICS OF URL
In the RUD Operations above we have also the count of url accessed but if we want it seperately then we can get the statistics by http://127.0.0.1:8000/your_short_url/stats/
