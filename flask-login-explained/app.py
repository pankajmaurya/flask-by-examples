# app.py

from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create a simple User model for demonstration
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.name = "User" + str(self.id)

# Dummy user database for demonstration
users = {
    '1': User('1'),
    '2': User('2')
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
        user_id = request.form.get('user_id')
        user = users.get(user_id)
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid user ID'
    else:
        return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user_id=current_user.id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
