# hammad-innovaxel-mubeen
Url Shortner Home Assignment

# 📌 Features

🔗 Create a Short URL: Converts long URLs into short, manageable links.

🔄 Retrieve Original URL: Redirects or fetches the original URL using the short code.

✏️ Update Short URL: Modify the original URL associated with a short link.

❌ Delete Short URL: Remove a short URL from the database.

📊 View URL Statistics: Track how many times a short URL has been accessed.

# 🚀 Setup Instructions

1️⃣ Clone the Repository

2️⃣ Set Up MySQL Database
In Project's settings.py add.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver

# 🖥️ Project Walkthrough
This API's of this project are built in REST with the help of Django Rest Framework.

1️⃣ Create a Short URL

Visit http://127.0.0.1:8000/
Enter your long URL in the input box.
Click Shorten URL to generate a short link.

2️⃣ Retrieve, Update, or Delete a Short URL

Click on the generated short URL to access update and delete options.
Alternatively, visit http://127.0.0.1:8000/<your_short_code>/

3️⃣ View URL Statistics

As the above endpoints will show the access count of each url but alternatively we can access at:
http://127.0.0.1:8000/<your_short_code>/stats/

