import os
from dotenv import load_dotenv
from flask import Flask, redirect
from routes.index import all_blueprints
from commands import cli_commands

load_dotenv()
app = Flask(__name__)

for blueprint in all_blueprints:
    app.register_blueprint(blueprint)

cli_commands(app)

@app.route('/')
def home():
     return "Home !!"