DJANGO APPS 
# AS LEARNT YESTERDAY APPS ARE THE BULDING BLOCKS OF OUR PROJECT
THEY CONTAIN THE FEATURES PF OUR APPLICATIONS.
EXAMPLE OF AN APP
 APP/
                  |   |-- __init__.py
                  |   |-- admin.py
                  |   |-- apps.py
                  |   |-- models.py
                  |   |-- tests.py
                  |   |-- views.py
                  |   |migrations/
                          |   |-- __init__.py

            ->admin.py -> register your models to make them accessible via the admin interface
            ->app.py -> contains app configurations
            ->models.py -> contains models for the database
            ->tests.py -> tests are done in this file
            ->views.py -> contains functions or classes that interact with the user.
            ->migrations/ -> contains files used by django to track changes in models and apply them in database.
