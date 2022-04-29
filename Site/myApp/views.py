from flask import Flask, render_template, request, redirect, session, jsonify
from .model import bdd as bdd
from .controller import function as f
from werkzeug.utils import secure_filename



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

@app.route("/compte")
def auth_register():
    return render_template("compte.html")

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
        return redirect("/authOK")
    else: # echec authentification
        return redirect("/connecter/authEchec")

#mdp = hashlib.sha256(mdp.encode())
#mdpC = mdp.hexdigest() #mot de passe chiffré
#add_user(email, nom, prenom, statut, login, motPasse, avatar)