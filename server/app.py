from flask import Flask
# from .blueprints import create_routes // Blueprint infrastructure setup for possible later use
from .resources import create_resources
from .database.connect import connect_to_db

print("Creating app....")
app = Flask(__name__)

# Connect to DB
print("Testing connection to database....")
connect_to_db()

# Create API
print("Creating API....")
create_resources(app)
