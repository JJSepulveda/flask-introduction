# flask-introduction
Introducción al framework flask para desarrollo de aplicaciones web

## Objeto response - cookies
El objeto response es donde estan todos los datos que envia el servidor al cliente en un modelo cliente-servidor

Ejemplo de como guardar y recuperar una cookie
```
# main.py -- guardar cookie
from flask import Flask, request, make_response, redirect

app = Flask(__name__)
COOKIE_USER_IP = 'user_ip'

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	# aqui guardamos la cookie
	response.set_cookie(COOKIE_USER_IP, user_ip)

	return response
```
```
# ...Continuación - recuperar cookie

@app.route('/hello')
def hello():
	user_ip = request.cookies.get(COOKIE_USER_IP)
	return f'Hola tu ip es: {user_ip}'
```

## Jinja2 - estructuras de control - if
 Es un templete-engine inspirado en los Django-templates.
 Las estrucutras de control son las condicionales.

Ejemplo de como usar un if en un template de Jinja2:
```
# ./templates/hello.html
{% if user_ip %}
	<h1>Hello world Platzi, tu IP es {{ user_ip }}</h1>
{% else %}
	<a href="{{ url_for('index') }}">Ir a inicio para obtener tu ip</a>
{% endif %}
```
```
# ./main.py
from flask import Flask, request
from flask import render_template

app = Flask(__name__)
COOKIE_USER_IP = 'user_ip'

@app.route('/hello')
def hello():
	user_ip = request.cookies.get(COOKIE_USER_IP)
	return render_template('hello.html', user_ip=user_ip)

```