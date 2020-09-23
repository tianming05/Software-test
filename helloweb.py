# A simple Hello World web application

from flask import Flask, request, redirect, url_for, render_template
from hello import Hello

app = Flask(__name__)
hello = Hello("Web")

@app.route("/", methods=["GET", "POST"])
def helloweb():
    """Display a greeting."""

    if request.method == "POST":
        # We have received some form data

        if not request.form["name"]:
            # We didn't get a name, pick a random one
            return redirect(url_for('random'))
        else:
            # We got a name, update our Hello object
            hello.name = request.form["name"]
            hello.add(request.form["name"])

    # Render the page
    return render_template("helloweb.html", hello=str(hello))

@app.route("/random")
def random():
    """Pick a random name and display the greeting."""

    hello.pick_random()
    return render_template("helloweb.html", hello=str(hello))

@app.route("/reset")
def reset():
    """Reset the internal state."""

    global hello
    hello = Hello("Web")
    return redirect(url_for('helloweb'))
