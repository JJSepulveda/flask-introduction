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