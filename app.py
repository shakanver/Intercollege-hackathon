from flask import Flask, render_template, request

app = Flask(__name__)

users = []

@app.route('/register',methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    username = request.form['username']
    password = request.form['password']
    users.append({'username': username, 'password': password})
    print(users)
    for i in range(0,len(users)):
        if username == users[i]['username'] and password == users[i]['password']:
            return render_template("/test.html")

    return "Invalid username or password"

if __name__ == '__main__':
    app.run(debug=True, port = 2512)
