from flask import Blueprint

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
def index():
	return "Flask Hello World"