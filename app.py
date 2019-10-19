from flask import Flask, render_template, request

app = Flask(__name__)

# register (username , password) return: url to profile
# send_message (thread, timestamp, content) return: boolean
# get_messages() return: messages[]

@app.route('/home', methods=['GET'])
def home():
    return render_template("./register.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username , password)
    return render_template("./test.html")

if __name__ == '__main__':
    app.run(debug=True)
