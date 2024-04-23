# Importing necessary modules from Flask and its extensions.
from flask import Flask, redirect, url_for
from ext.ext import db
from flask_migrate import Migrate
from flask_login import LoginManager
from models.model import User

# Creating a Flask app instance.
app = Flask(__name__)

# Setting a secret key for the app.
app.secret_key = "super secret key"

# Configuring the database URI and track modifications for SQLAlchemy.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Changed from 'flask_migrate' to 'False'.

# initializing LoginManager with Flask app instance
login_manager = LoginManager()
login_manager.init_app(app)


# Initializing SQLAlchemy with the Flask app instance.
db.init_app(app)

# Setting up Flask-Migrate with the app and the SQLAlchemy instance.
migrate = Migrate(app, db)

# Importing the auth blueprint from the auth module.
from auth.auth import auth 

# Registering the auth blueprint with the app, with a URL prefix '/auth'.
app.register_blueprint(auth, url_prefix='/auth')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Redirecting the root route to the 'index' route of the auth blueprint.
@app.route('/')
def Redirect():
	return redirect(url_for('auth.login'))

# Running the Flask app if this script is executed directly.
if __name__ == '__main__':
	with app.app_context():
        # Creating database tables based on the defined models.
		db.create_all()
        # Running the app in debug mode.
		app.run(debug=True)
