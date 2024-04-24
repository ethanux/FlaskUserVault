# Import the 'db' instance from the 'ext' module
from ext.ext import db

# Import the 'datetime' module to work with timestamps
from datetime import datetime

# Import 'UserMixin' from Flask-Login for user authentication features
from flask_login import UserMixin

# Define a class named 'User' representing a user in the application
class User(UserMixin, db.Model):
    """
    Represents a user in the application.

    Inherits from UserMixin for user authentication features provided by Flask-Login.
    Inherits from db.Model to define the database model using SQLAlchemy ORM.

    Attributes:
    - id (int): Primary key for the user record.
    - fullname (str): Full name of the user.
    - email (str): Email address of the user.
    - password (str): Password of the user.
    - timestamp (datetime): Timestamp indicating the creation date of the user record.
    """
    # Define a column 'id' of type Integer as the primary key
    id = db.Column(db.Integer, primary_key=True)

    # Define a column 'fullname' of type String with a maximum length of 20 characters
    fullname = db.Column(db.String(20), nullable=False)

    # Define a column 'email' of type String with a maximum length of 50 characters
    email = db.Column(db.String(50), nullable=False)

    # Define a column 'password' of type String with a maximum length of 50 characters
    password = db.Column(db.String(50), nullable=False)

    # Define a column 'timestamp' of type DateTime with a default value of the current timestamp
    timestamp = db.Column(db.DateTime, nullable=True, default=datetime.now())
