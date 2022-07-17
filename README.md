# flask-introduction
Introducción al framework flask para desarrollo de aplicaciones web

## Flask.request
Flask incluye el objeto request que extiende el request de la libreria Werkzeug de python con algunas cosas para flask.

### request.remote_addr
Para obtener la ip del usuario.

Ejemplo:
```
from flask import Flask, request

app = Flask(__name__)
COOKIE_USER_IP = 'user_ip'

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	response.set_cookie(COOKIE_USER_IP, user_ip)

	return response
```

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
	response.set_cookie(COOKIE_USER_IP, user_ip)

	return response
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

## Jinga2

### Estructura de control - if
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

### Estructura de control - for
Estrucutra de control "for" en Jinga2

Ejemplo:
```
{% for key, segment in segment_details.items() %}
	<tr>
			<td>{{ key }}td>
			<td>{{ segment }}td>
	<tr>
{% endfor %}`
```

### Macros
Definición de la macro:
```
# templates/macro_render_todo.html
{% macro render_todo(todo) %}
	<li>Tarea: {{ todo }}</li>
{% endmacro %}
```
Implementación de la macro:
```
# templates/hello.html
...
{% import 'macro_render_todo.html' as macro_todo %}
...
{% block content %}
	...
	<ul>
		{% for todo in todos %}
			{{ macro_todo.render_todo(todo) }}
		{% endfor %}
	</ul>
{% endblock content %}
```

### Include 
Puedes incluir pedazos de codigo html con la etiquete include

```html
#templates/navbar.html
<nav>
	<ul>
		<li>
			<a href="{{ url_for('index') }}">
				Inicio
			</a>
		</li>
		<li>
			<a href="{{ url_for('hello') }}" target="_blank">
				hello
			</a>
		</li>
	</ul>
</nav>
```

```
# templates/base.html
...
<header>
	{% include 'navbar.html' %}
</header>
...
```
### Archivos estaticos
Para manejar los archivos estáticos hay que crear una carpeta en la raíz con el nombre de static y dentro guardar todos los archivos estáticos.

Nota: los archivos estáticos se guardan en el cache del navegador, por lo que puede que abecés se tenga que hacer un hard-reload para visualizarlos.

Ejemplo de como insertar una imagen en la pagina desde un archivo estático:

```
# templates/navbar.html
<img 
			src="{{ url_for('static', filename='images/red-amongus.png') }}" 
			alt="logo" 
/>
```

Ejemplo de como importar un css.
```
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
```