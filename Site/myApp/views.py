from flask import Flask, render_template, session, request, redirect
from .controller import function as f
app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('myApp.config')
 
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/connecter")
def auth_login():
    return render_template("connecter.html")

@app.route("/auth-register")
def auth_register():
    return render_template("auth-register.html")

@app.route("/auth-forgot-password")
def auth_forgot_password():
    return render_template("auth-forgot-password.html")

@app.route("/ui-file-uploader")
def ui_file_uploader():
    return render_template("ui-file-uploader.html")

@app.route("/aeroclubs")
def aeroclubs():
    return render_template("aeroclubs.html")

@app.route("/component-dropdown")
def component_dropdown():
    return render_template("component-dropdown.html")

@app.route("/gérer-profils")
def gérer_profils():
    return render_template("gérer-profils.html")

@app.route("/webmaster")
def webmaster():
    return render_template("webmaster.html")

@app.route("/logout") # menu se connecter @app.route("/connecter/<infoMsg>")
def logout():
    session.clear()
    return redirect("/connecter/logoutOK")

# traitement du formulaire d'authentification
@app.route("/login", methods=["POST"])
def login():
    #f.sessionTest()
    login = request.form['login']
    password = request.form['mdp']
    msg = f.verifAuth(login,password)
    print(msg)
    if "idUser" in session: # authentification réussie
        return redirect("/index/authOK")
    else: # echec authentification
        return redirect("/connecter/authEchec")