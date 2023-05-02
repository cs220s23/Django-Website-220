# Final-Project-Dev-Ops

This project is a Django website that uses redis allow connections from anywhere

# Contributors

Davin Glynn - dg25moravian

Jeffery Eisenhardt - eisenhardtj

Dermot Badman - Dbad0210

# Overview

This project is a very simple webpage which can query a mysql server and display results.  

# Steps before you run locally

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# How to run locally

After you do those steps, you will then run 

```
python manage.py runserver
```

# How to run with Gunicorn

```
sudo gunicorn -c conf/gunicorn_config.py personal_portfolio.wsgi
```

# How to run on AWS

```
sudo bash up_aws
```

# Technologies used


Django: https://www.djangoproject.com/
Gunicorn: https://gunicorn.org/
AWS: https://aws.amazon.com/
Docker: https://www.docker.com/
Mysql: https://www.mysql.com/
