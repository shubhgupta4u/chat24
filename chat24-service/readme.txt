conda create --prefix ./.venv python=3.8

conda activate ./.venv

pip install -r requirements.txt

$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$

$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000 --debugger

https://medium.com/@shalandy/deploy-git-subdirectory-to-heroku-ea05e95fce1f
heroku login
heroku git:remote -a my-app
git subtree push --prefix path/to/subdirectory heroku master

E:\Repository\Github\chat24\chat24-service>git subtree push --prefix chat24-service heroku master