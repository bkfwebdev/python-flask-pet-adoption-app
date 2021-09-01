""" ADOPTION SHELTER PROJECT"""

from _typeshed import FileDescriptor
from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtensions
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "q36spacemodulator"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Over9000@localhost:5432/adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all() 

toolbar = DebugToolbarExtensions(app)

@app.route("/")
def list_pets():
    """list pet data"""
    
    pets = Pet.query.all()
    return render_template("pet_list.html", pets = pets)


@app.route("/add", methods = ["GET","POST"])
def add_pet():
    """add pet data"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for  k, v in form.data.items() if k != "csrf_token"}
        # new_pet = Pet(name = form.name.data etc...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('lisy_pets'))
    else:
        # go back to showing form for editing
        return render_template("pet_add_form.html", form = form)

@app.route("/<int:pet_id>", methods = ["GET","POST"])
def edit_pet(pet_id):
    """edit pet data"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated")
        return redirect(url_for('list_pets'))
    
    else:
        #go back to form for editing
        return render_template ("pet_edit_form.html", form = form, pet = pet)

@app.route("api/pets/<int:pet_id>", methods = ['GET'])
def api_get_pet(pet_id):
    """return pet data - JSON format"""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age":pet.age}

    return jsonify(info)










