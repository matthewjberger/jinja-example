from flask import Flask
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json

app = Flask(__name__)
env = Environment(
    loader=FileSystemLoader('templates/'),
    autoescape=select_autoescape(['html', 'xml'])
)

@app.route('/')
def display_shows():
    shows = ['House MD', 'Bojack Horseman']
    return env.get_template('index.html').render(
        shows=map(json.dumps, shows)
    )