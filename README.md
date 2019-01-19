# Overview

cl_flask is a web application where users can post articles and classifieds similar to [Craigslist.org](htps://www.craigslist.org)

# Start

Language: Python 
version: 3.6
framework: Flask

## Create an environment:
```
cd myproject
```
Mac:
```
python3.6 -m venv venv
```
Windows:
```
py -3 -m venv venv
```
if any issues:
```
sudo apt-get install python3.6-venv

python3.6 -m venv venv
```

## Activate your environment:
Once you initially install/create an environment,
you'll only have to activate to use `venv`

Mac:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```
or maybe:
```
source venv\Scripts\activate
```

## Install Flask:
```
pip install Flask
```
### Latest:
```
pip install -U https://github.com/pallets/flask/archive/master.tar.gz
```

```
cd cl_flask
```
Run Production:
```
export FLASK_APP=app.py flask run
```

## Debug mode:
Development:
```
export FLASK_ENV=development flask run
```