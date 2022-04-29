# Directions!
'''
1. install Flask - open terminal in VS CODE 
Run this command: pip install Flask

to build to this web service quickly I am using FLASK
a lightweight web framework - meaning a third party python library used for 
developing web applications
need a server in place to handle request in response cycle
'''
from flask import Flask, render_template, request, url_for, flash, redirect
import json


from fake_json import data 

#debug mode
# cmd: set FLASK_ENV=development
# Bash: export FLASK_ENV=development
# Powershell: $env:FLASK_ENV = "development"

# Run Flask
# flask run

# this app calls the server
# Whenever the Python interpreter reads a source file, it does two things:
# it sets a few special variables like __name__, and then
# it executes all of the code found in the file
app = Flask(__name__)

deserialized_json = json.loads(data)


# decorator
@app.route('/')
def index():
    return 'Hello!'
    
@app.route("/herohall")
def hero_hall():
    return render_template('index.html', deserialized_json=deserialized_json)


@app.route('/hero/getHero/<superhero>', methods=['GET'])
def get_hero(superhero):
    for hero in deserialized_json:
        if (hero['superhero'].lower() == superhero.lower()):
            print(hero['superhero'].lower())
            print(superhero.lower())
            return json.dumps(hero)
    return "Hero not found..."


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        superhero = request.form['superhero']
        publisher = request.form['publisher']
        alter_ego = request.form['alter_ego']
        first_appearance = request.form['first_appearance']
        characters = request.form['characters']

        if not superhero:
            flash('Name is required!')
        elif not publisher:
            flash('Publisher is required!')
        else:
            deserialized_json.append({'superhero': superhero, 'publisher':publisher, 'alter_ego':alter_ego, 'first_appearance': first_appearance, "characters": characters})
            return redirect(url_for('hero_hall'))

    return render_template('create.html')

app.run(debug=False)