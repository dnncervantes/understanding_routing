from flask import flask
app = Flask(__name__)

#1
@app.route('/')
def helloWorld():
	return "Hello World"

# @app.route('/success')
# def success():
#     return "Success"

# @app.route('/hello/<string:banana>/<int:num>')
# def hello(banana, num):
#     return f"Hello {banana * num}"

# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

#2

@app.route('/dojo')
def dojo():
    return "Dojo!"

#3

@app.route('/say/flask')
def hi_flask():
    return "Hi Flask!"

@app.route('/say/michael')
def hi_michael():
    return "Hi Michael!"

@app.route('/say/john')
def hi_john():
    return "Hi John!"

#4

@app.route('/repeat/<int:num>/<string:example>')
def rep_hello(example, num):
    return f"{example * num}"

if __name__ == '__main__':
	app.run(debug=True)