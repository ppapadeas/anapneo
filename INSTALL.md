Having a local development deployment of Anapneo, in order to work, is really easy since this a very simple (at least at the moment) web app.

## Python

First thing is to install the necessary python packages.

On Fedora:

`yum install python-virtualenv python-pip`

On Debian:

`aptitude install python-virtualenv python-pip`

## Virtualenv

Now you are ready to create your virtual environment and install the dependencies.

`virtualenv --no-site-packages env`

Now let's get inside this virtualenv.

`source env/bin/activate`

and install all the requirements

`pip install -r requirements.txt`

Now you can exit the virtualenv.

`deactivate`

## Fork and Clone

The best way of contributing to SunObS is to fork it on your account and then clone it locally.

`git clone git@github.com:your_github_username/anapneo.git`

## Run it

Before you run it for the first time you need to setup your local_settings.py.

`mv local_settings.py-example local_settings.py`

and fill the variables with your settings.

Now lets activate our virtualenv again.

`source env/bin/activate`

And from inside of SunObS local repo we run the manage script.

`python manage runserver`

Now all you have to do is open your browser and point it to the address below.

`http://localhost:8000`

## Contribute

Make a new branch named after a specific bug or feature. This way you can work on multiple things before you decide to do the final push.

`git branch -b random_feature`

Hack around, make all the changes you want and commit them. Finally push the code back to your own forked repo.

Finally just do a Pull Request to my repo :-)


