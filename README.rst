========================
tenerife_japon_status
========================

Dependencies
------------

* Git.
* Python 3, pip and virtualenvwrapper.
* Node and npm (recomendation: use `nvm <https://github.com/creationix/nvm>`__).
* Firefox for E2E test.
* Las version of `Fabfile <https://hg.apsl.net/fabfile>`__ for pre and prod deployments.
* `Editorconfig <http://editorconfig.org/#download>`__ for development.


Installation and run
--------------------

#. Clone project from repo ::

    git clone git@gitlab.apsl.net:group/project.git

#. Setup virtualenv Python ::

    cd appname
    mkvirtualenv "appname" -p python3 -a ./src
    pip install -r requirements/local.txt

#. Setup Javascript environment ::

    npm install

#. Create local configuration ::

    cd src
    cp app.ini.template app.ini
    # Review and edit app.ini

#. Run local server an check tests ::

    python manage.py runserver
    # With runserver running, open another terminal in the same virtualenv and
    # src directory and run
    pytest
    # If some test fails, a browser screenshot will be saved in src/tests_failures.
