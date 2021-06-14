# Python 101

## Setup Virtual env (Windows): 

Create the environment:
```powershell
py.exe -m venv flask-env
```
  
Activate the environment:
```powershell
.\flask-env\Scripts\Activate.ps1
```

## Setup Virtual env (Linux): 

Create the environment:
```shell
python3 -m venv env 
```
  
Activate the environment:
```shell
source env/bin/activate
```

## Run with embedded flask server for testing
```
cd flask-veg/app
flask run
```

## Run with gunicorn
```
cd flask-veg/app
/usr/local/bin/gunicorn --workers 5 --bind 0.0.0.0:5000 wsgi:app
```

## DB
Managed through SQLAlchemy - see here for init and change instructions:  
https://flask-migrate.readthedocs.io/en/latest/

# Deploy

Edit deploy/ansible/inventory to include the correct host address and database connection details.

Deploy with below command, passing in extra params specific to the target host specified in the inventory - username, key files etc...

`ansible-playbook deploy/ansible/flaskveg.yaml`