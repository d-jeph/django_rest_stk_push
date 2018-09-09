## Django Rest API for STK-Push
This app is a django-rest-framework api that supports the following technologies:
* django-rest-framework
* Safaricom's STK Push on [Daraja](https://developer.safaricom.co.ke/)
* [Docker](https://www.docker.com/) containers
* [Travis-Ci](https://travis-ci.org/) for continuious intengration
* [Django Swagger](https://django-rest-swagger.readthedocs.io/en/latest/) for Api Documentation

To test the application locally you will need to have the following tools installed: 
* Docker and Docker Compose
* [Ngrok](https://ngrok.com/) for local tunnelling

After installing the above tools, follow the following steps to run the application:
* At the root directory of the application run the command: 
 ```sh
$ docker-compose run web python /code/manage.py migrate --noinput
```
This will migrate the database on Docker
The run 
 ```sh
$ docker-compose up -d --build
```
If all went well the app should be running at http://127.0.0.1:8000/
At this point naviagate to where you extracted Ngrok and create a tunnel for you localhost by running the command: 
```sh
$ ngrok.exe http 8000
```
This will generate a temporary url id which you will need to update in the settings file a value named NGROK.

That's it!

To access the Api Swagger documentation just access the root url: http://127.0.0.1:8000/ or t



