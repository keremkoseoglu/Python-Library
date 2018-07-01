from flask import Flask, jsonify, render_template, request, session
from data import data_manager

# ---Configuration-----

app = Flask(__name__)
app.secret_key = "VERY_SECRET" # Required for sessions
app.config["CACHE_TYPE"] = "null"

# ---Static HTML-----

@app.route('/disclaimer')
def disclaimer():
    return app.send_static_file("disclaimer.html")

# ---Templates-----

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/ajax_sample')
def ajax_sample():
    return render_template("ajax_sample.html")

@app.route('/html_injection')
def html_injection():
    return render_template("html_inject.html", inject_code="<b>injected code</b>")

@app.route('/list_people')
def list_people():
    people = data_manager.DataManager().get_people()
    return render_template("people.html", people=people)

@app.route('/person')
def person():
    person_id = request.args.get("id", 0, type=int)
    person_obj = data_manager.DataManager().get_person(person_id)
    return render_template("person.html", person=person_obj)

@app.route('/tmp_demo')
def tmp_demo():
    return render_template("tmp_child.html")

# ---JSON-----

@app.route('/json/list_people')
def json_list_people():
    people_as_dict = data_manager.DataManager().get_people_as_dict()
    return jsonify(people_as_dict)

# ---Administration-----

@app.route('/admin')
def admin():
    return render_template("admin/login.html")

@app.route("/admin/login", methods=["POST"])
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    try:
        data_manager.DataManager().login(username, password)
        session["username"] = username
        return render_template("admin/admin_menu.html")
    except ValueError:
        return render_template("admin/login_error.html")

@app.route('/admin/menu')
def admin_menu():
    if "username" not in session:
        return render_template("/admin/login.html")
    return render_template("admin/admin_menu.html")

# ---Execution-----

if __name__ == '__main__':
    app.run()
