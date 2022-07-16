from flask import Flask, request, make_response, redirect
from flask import render_template


app = Flask(__name__)

COOKIE_USER_IP = 'user_ip'

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	response.set_cookie(COOKIE_USER_IP, user_ip)

	return response


@app.route('/hello')
def hello():
	user_ip = request.cookies.get(COOKIE_USER_IP)
	return render_template('hello.html', user_ip=user_ip)



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
