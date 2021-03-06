# pythonanywhere


**PythonAnywhere** is an online integrated development environment (IDE) and web hosting service based on the Python programming language . Founded by Giles Thomas and Robert Smithson in 2012, it provides in-browser access to server-based Python and Bash command-line interfaces , along with a code editor with syntax highlighting . Program files can be transferred to and from the service using the user's browser. Web applications hosted by the service can be written using any WSGI-based application framework.
[wikipedia](https://en.wikipedia.org/wiki/PythonAnywhere)


## Features

 - CPython, PyPy and IPython support, including Python versions 2.7, 3.3, 3.4, 3.5, 3.6, 3.7 and 3.8.
 - In-browser interactive consoles with code running on hosted servers, shareable between multiple users.
 - WSGI-based web hosting, e.g. Django, Flask, web2py
 - Support for coding from iPad and other mobile devices.
 - Syntax-highlighting in-browser editor.
 - Many popular Python modules pre-installed.
 - Cron-like scheduled tasks to run scripts at a given time of day.
 - Always-on tasks to run scripts and restart them automatically when they fail.

## How to Deploy project

 1. Create a repository on github or gitlab or ... .
 2. Clone your repository on pythonanywhere bash . 
 3. Create a virtualenv on pythonanywhere . 
> create     : `mkvirtualenv --python=python3.8 (your env name)`

> remove   : `rmvirtualenv (your env name)`

> active     :  `workon (your env name)`

> deactive : `deactivate`

 4. Install Libraries .
 > bash : `pip install -r requirements.txt`
 5. Create web app in **Manual configuration** mod
 6. set **source code** , **virtualenv** and **staticfiles url** .
 > source code : `/home/(Account-name)/(project-name)`
 
 > virtualenv : `/home/(Account-name)/.virtualenvs/(venv-name)`
 
 > staticfiles url :  `url:/staticfiles   path:/home/(Account-name)/(project-name)/staticfiles`
 8. WSGI confguration file (see in wsgi.py).
 > clear : `just keep a django part`
 
 > change :  `change path and os.environ`
 10. Change a path url in setting.py.
 > note :  `we cant use a os.path in setting.py so we should cjange it (see a setting.py)`
