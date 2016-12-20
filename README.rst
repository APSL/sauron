==========
onlysmellz
==========

Dependencies
------------

* Python 3, pip and virtualenvwrapper.


Installation and run
--------------------

#. Clone project from repo ::

    git clone git@gitlab.apsl.net:group/project.git

#. Setup virtualenv Python ::

    cd appname
    mkvirtualenv "appname" -p python3 -a ./src
    pip install -r requirements/local.txt

#. Create local configuration ::

    cd src
    cp app.ini.template app.ini
    # Review and edit app.ini

#. Run local server an check tests ::

    python manage.py runserver
    # With runserver running, open another terminal in the same virtualenv and
