# Flask Service

## What is Flask
Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

It does have many cool features like url routing, template engine. It is a WSGI web app framework.

[Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/quickstart/)

## What is WSGI?
WSGI
The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard for Python web application development. WSGI is the specification of a common interface between web servers and web applications.

## What is Jinja2?
jinja2
jinja2 is a popular template engine for Python.A web template system combines a template with a specific data source to render a dynamic web page.

This allows you to pass Python variables into HTML templates like this:
```
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>Hello {{ username }}</h1>
    </body>
</html>
```

## What is a Microframework?
Flask is often referred to as a microframework. It is designed to keep the core of the application simple and scalable.

Instead of an abstraction layer for database support, Flask supports extensions to add such capabilities to the application.


## What will you need
You will need to use PIP to install Flask and requests

Open the terminal and run:
```
pip install Flask
pip install requests
```

## Code break down
### app.py
Main index of our app. 

Here we place our functions and routes to urls

#### Fake/Dummy Data
``` from fake_json import data ```
imports the `data` dictionary from the fake_json file.

We have a dictionary serving as fake JSON so we don't have to make requests.
Since this dictionary is so big, it's nice to make a new file and put it there,
then import it into our app so we don't clutter the logic.

``` deserialized_json = json.loads(data) ```
Turns our fake dictionary into JSON

#### Routing
Here's what our typical routing logic and functions are located.

Route:
```
@app.route('/bored/', methods=['GET', 'POST'])
```
#### The @ sign is a decorator:
a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it

#### Routes and Requests
``` @app ```
Tells to use the instance initialized as the app.

```route('/bored/',```
The route method tells what URL we want to bind

```methods=['GET', 'POST'])```
Tells what kind of requests we want to allow at this endpoint

#### Below the Route We Put our logic
Here we run the function Hero_hall,
we render the html template `index.html` to show the data how we want:
```
def hero_hall():
    return render_template('index.html', deserialized_json=deserialized_json)
```

Here we're passing in our json data which we then manipulate in the `index.html`:
`deserialized_json=deserialized_json` 

#### Parameters at the URL
You can add variable sections to a URL by marking sections with `<variable_name>`. 
Your function then receives the `<variable_name>` as a keyword argument. 
Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>`.

```@app.route('/hero/getHero/<superhero>', methods=['GET'])``

If we want to pass a hero and then search for them by looping through the JSON data.
```
def get_hero(superhero):
    for hero in deserialized_json:
        if (hero['superhero'].lower() == superhero.lower()):
            print(hero['superhero'].lower())
            print(superhero.lower())
            return json.dumps(hero)
    return "Hero not found..."
```
[Flask Variable Documentation](https://flask.palletsprojects.com/en/2.1.x/quickstart/#variable-rules)

### Templates
Often with HTML files we make a directory named templates.

In bigger applications you might have directories inside the template folder.

#### base.html
Here we put the top part of the page with links to different templates or endpoints

#### index.html 
Here we extend our base.html so we can see it at the top of our `index.html` template.

`{% extends 'base.html' %}`

#### What is the {% code_here %}?
The {% and %} with code inside is called _It's a Template Engine system_, and its syntax is based on jinja.

If we want to use some simple logic, like loops or if statements we can wrap it in the `{% %}`
```
{% for hero in deserialized_json %}
        <div class='hero'>
            <h3>{{ hero['superhero'] }}</h3>
            <li>{{ hero['publisher'] }}</li>
            <li>{{ hero['first_appearance'] }}</li>
            <li>{{ hero['characters'] }}</li>
{% endfor %}
```

You can see take the `deserialized_json` we passed, and we loop through naming it `hero`,
then we can grab the values of each hero using the typical JSON key/value pairs: `hero['superhero']`

#### HTML Explanations
`<div>` tag: defines a division or a section in an HTML document.
`<h3>` tag: Defines the inside text to be header 3
`<li>` tag: Puts the items inside a list, often others use `<ul>`, and `<ol>`
`<a>` tag: Defines a hyperlink 
`<br>` tag: Inserts a single line break
`<style>` tag: Used to define style information [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS) for a document.

[W3 Schools element breakdown](https://www.w3schools.com/tags/ref_byfunc.asp)

### fake_json.py
Often when building web apps, developers will make mock/dummy data so model what the app
will look like without having to make requests. Usually this looks like making a dictionary
and using that to make sure the functions handle the data correctly before adding the requests.

This is especially helpful for writing tests, so our tests don't have to make HTTP requests, etc.

## Sources: 
https://flask.palletsprojects.com/en/2.1.x/

https://pythonbasics.org/what-is-flask-python/

https://www.w3schools.com/tags/ref_byfunc.asp
