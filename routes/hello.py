from flask import Blueprint, request, jsonify
from crewai import Agent, Task, Crew, Process

hello_crew = Blueprint('hello', __name__)

@hello_crew.route('/hello', methods=['POST'])
def hello():
    data = request.json
    return jsonify({
        "message": "CrewAI API route is up and running!",
        "data": data
    })
