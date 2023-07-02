# app.py

from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create a simple User model for demonstration
# class User(UserMixin):
#     def __init__(self, user_id):
#         self.id = user_id
#         self.name = "User" + str(self.id)

# Create a simple User model for demonstration
class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password
        self.name = "User" + str(self.id)

# Dummy user database for demonstration
users = {
    '1': User('1', 'john', 'password'),
    '2': User('2', 'jane', 'password')
}

# User loader function required by Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = next((user for user in users.values() if user.username == username and user.password == password), None)
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return render_template('error.html', error_message='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user_id=current_user.id, username=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if any(user.username == username for user in users.values()):
            return render_template('error.html', error_message='Username already exists')

        user_id = str(len(users) + 1)
        user = User(user_id, username, password)
        users[user_id] = user

        login_user(user)
        return redirect(url_for('dashboard'))
    else:
        return render_template('register.html')
    
if __name__ == '__main__':
    app.run()
