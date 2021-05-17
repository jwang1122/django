# Learn Djando

## Table of Contents- [Learn Djando](#learn-djando)
  - [Table of Contents](#table-of-contents)
  - [install Django module 3.2.3](#install-django-module-323)
  - [django-admin](#django-admin)
  - [Start your own application](#start-your-own-application)
  - [Image Magick](#image-magick)

## install Django module 3.2.3
```
pip install django- [Learn Djando](#learn-djando)
  - [django-admin](#django-admin)
  - [Start your own application](#start-your-own-application)
  - [Image Magick](#image-magick)
python -m pip install --upgrade pip
```

check all modules that pip installed
```
pip freeze
```

## django-admin

```
django-admin
mkdir src
cd src
django-admin startproject <project name> .
python manage.py runserver
```
Open browser, type in "localhost:8000"

[localhost:8000](http://localhost:8000)
![First Django Page](./images/first-django.png)
[admin](http://localhost:8000/admin/login/?next=/admin/)

Stop the app by click Ctrl+c on terminal

```
python manage.py migrate
python manage.py createsuperuser
```

## Start your own application
```
python manage.py startapp products
```
* ./products/models.py
    ![MVC design pattern](./images/mvc.jpg)
    
## Image Magick
Conver images from png to gif
```
magick F_*.png motion.gif
magick pencil.png favicon.ico
```
