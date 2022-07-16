from flask import Flask, request, make_response, redirect
from flask import render_template


app = Flask(__name__)

COOKIE_USER_IP = 'user_ip'

todos = ['TODO1', 'TODO2', 'TODO3']

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	response.set_cookie(COOKIE_USER_IP, user_ip)

	return response


@app.route('/hello')
def hello():
	user_ip = request.cookies.get(COOKIE_USER_IP)
	context = {
		'user_ip': user_ip,
		'todos': todos
	}
	return render_template('hello.html', **context)



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
