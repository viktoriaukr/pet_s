from flask import Flask, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Renders the home page."""
    pet = Pet.query.all()
    return render_template('home.html', pets = pet)


@app.route('/add', methods = ['GET','POST'])
def add_new_pet():
    """Adds new pet."""
    form = AddPet()
    if form.validate():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available = available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_new_pet.html", form = form)
    

@app.route("/<int:id>", methods = ['GET','POST'])
def display_edit_pet_info(id):
    """Display pet information and lets users to edit it."""

    pet = Pet.query.get_or_404(id)
    form = EditPet(obj=pet)

    if form.validate():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    
    return render_template("edit_pet_info.html", form = form)