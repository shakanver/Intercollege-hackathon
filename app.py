from flask import Flask, render_template, request

app = Flask(__name__)

users = []
messages = []


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
            return render_template("/login.html")
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

@app.route('/sendmessage',methods=['POST'])
def send_message():
    user = request.form['username']
    message = request.form['message']
    user_message = {'user':user,'message':message}
    messages.append(user_message)
    return render_template

@app.route('/messages',methods = ['GET'])
def view_messages():
    return render_template("/messages.html")





if __name__ == '__main__':
    app.run(debug=True, port = 2512)
