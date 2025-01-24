from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {"amulya": "sourabh"}  # Example user data

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if users.get(username) == password:
        return "Login successful"
    else:
        return "Login failed", 401

if __name__ == '__main__':
    app.run(debug=True)
