from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/register',methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = {'username': username, 'password': password}
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
                return render_template("profile.html")
        return "Invalid username or password"

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True, port = 2512)
