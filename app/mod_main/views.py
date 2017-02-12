from flask import Blueprint, Response, render_template, request, redirect, url_for
from app import mongo
from bson import ObjectId

mod_main = Blueprint('main', __name__)


@mod_main.route('/')
def index():
	return render_template("index.html")

@mod_main.route('/form',methods=['GET','POST'])
def form():
	if request.method == 'GET':
		emri="Roza"
		return render_template("form.html", emri=emri)
	elif request.method == 'POST':
		db = mongo.db.arkep
		form_data = request.form.to_dict()
		data = {

          "nderrmarja":{

            "emri": form_data['emri_ndermarrjes'],

            "numri_regjistrimi":form_data['nr_regjistrimit'],

            "adresa":form_data['adresa'],

            "personi_kontaktues":form_data['personi_kontaktues'],

            "telefoni":form_data['telefoni'],

            "email":form_data['email']

            }

        }
		print data
		
		db.insert(data)
		return render_template("form.html", mesazhi="Faleminderit,forma u insertua!")
	else:
		return"Go home, you're drunk"

@mod_main.route('/list', methods=['GET'])
def list():
	db= mongo.db.arkep
	rekordet=db.find()
	return render_template('list.html', rekordet=rekordet)

@mod_main.route('/remove/<string:remove_id>', methods=['POST'])
def remove(remove_id):
	db= mongo.db.arkep
	remove= db.remove({"_id" : ObjectId(remove_id)})
	return Response(200)

@mod_main.route('/raporti/<string:report_id>')
def raporti(report_id):
	db = mongo.db.arkep
	report=db.find_one({"_id": ObjectId(report_id)})

	return render_template('raporti.html', report=report)
