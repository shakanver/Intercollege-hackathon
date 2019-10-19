from flask import Flask, render_template, request

app = Flask(__name__)

users = []



@app.route('/home', methods=['GET'])
def home():
    return render_template("./register.html")

@app.route('/user/login', method=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    for i in range(0,len(users)):
        if username == users[i]['username'] and password == users[i]['password']:
            return render_template("./")

    return "Invalid username or password"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username , password)
    return render_template("./test.html")

if __name__ == '__main__':
    app.run(debug=True)
