from flask import Flask

app = Flask(__name__)

users = []



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/login', method=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    for i in range(0,len(users)):
        if username == users[i]['username'] and password == users[i]['password']:
            return render_template("./")

    return "Invalid username or password"


if __name__ == '__main__':
    app.run(debug=True)
