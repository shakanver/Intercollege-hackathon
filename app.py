from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []
messages = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register' , methods=['GET' , 'POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        college = request.form['college']
        degree = request.form['degree']
        year = request.form['year']

        user = {'username': username, 'password': password, 'college': college, 'degree': degree, 'year':year}

        if user not in users:
            users.append(user)
            print(users)
            return redirect(url_for('login'))
        else:
            return "User already exists!"

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template("/login.html")

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for i in range(0 , len(users)):
            if users[i]['username'] == username and users[i]['password'] == password:
                return render_template("profile.html",payload=users[i])
        return "Invalid username or password"

@app.route('/profile', methods=['GET'])
def user_profile():
    return render_template("/profile.html")

if __name__ == '__main__':
    app.run(debug=True, port = 2512)
