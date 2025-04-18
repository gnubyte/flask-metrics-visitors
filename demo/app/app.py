from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_metrics_visitors import MetricsVisitors

app = Flask(__name__)
app.config['SECRET_KEY'] = 'demo-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metrics.db'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize MetricsVisitors with the same db instance
metrics = MetricsVisitors(db=db)
metrics.init_app(app, db)

# Simple User model for demo
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables
with app.app_context():
    db.create_all()
    
    # Create demo user if not exists
    if not User.query.filter_by(username='admin').first():
        demo_user = User(username='admin', password='admin')
        db.session.add(demo_user)
        db.session.commit()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 