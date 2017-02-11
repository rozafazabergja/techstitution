from flask import Blueprint, render_template
from app import mongo

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
def index():
	return render_template("index.html")

@mod_main.route('/form')
def form():
	db = mongo.db.arkep
	db.insert({"name":"arkep"})
	return render_template("form.html")