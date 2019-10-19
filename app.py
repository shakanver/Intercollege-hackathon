from flask import Flask, render_template, request

app = Flask(__name__)

users = [{"username": "shakeel", "password": "shak28"}]



@app.route('/home', methods=['GET'])
def home():
    return render_template("./register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    print(username , password)
    for i in range(0,len(users)):
        if username == users[i]['username'] and password == users[i]['password']:
            return render_template("/test.html")

    return "Invalid username or password"

if __name__ == '__main__':
    app.run(debug=True, port = 2512)
