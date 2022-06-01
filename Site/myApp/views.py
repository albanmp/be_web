from flask import Flask, render_template, request, redirect, session, jsonify
from .model import bdd as bdd
from .controller import function as f
from werkzeug.utils import secure_filename
import pandas, os


app = Flask(__name__)

app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('myApp.config')


@app.route("/")
@app.route("/<infoMsg>")
def index(infoMsg=''):
    return render_template("index.html", info=infoMsg)


@app.route("/connecter")
@app.route("/connecter/<infoMsg>")
def connecter(infoMsg=''):
    return render_template("connecter.html", info=infoMsg)


@app.route("/compte")
def auth_register():
    msg, listeAeroclub = bdd.get_aeroclubData()
    return render_template("compte.html", liste = listeAeroclub)


@app.route("/auth-forgot-password")
def auth_forgot_password():
    return render_template("auth-forgot-password.html")


@app.route("/fichiers")
@app.route("/fichiers/<infoMsg>")
@app.route("/fichiers", methods=['POST'])
def fichiers(infoMsg=''):
    if "testFile" in request.files:
        file = request.files['testFile']
        #enregistrement du fichier dans le répertoire files
        filename = secure_filename(file.filename)
        UPLOAD_FOLDER = 'myApp/static/files/'
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        #enregistrement du fichier sur le serveur
        xls = pandas.read_excel(UPLOAD_FOLDER+file.filename)
        data = xls.to_dict('records')
        print([file.filename,data])
        #Enregistrement des données en BDD
        msg = bdd.saveDataFromFile(data)
        print(msg)
        if msg=="addDataFromFileOK":
            return redirect("/importDataOK")
        else:
            return redirect("/fichiers/importDataEchec")
    else:
        return render_template("/fichiers.html", info=infoMsg)


@app.route("/aeroclubs")
def aeroclubs():
    msg, listeAeroclub = bdd.get_aeroclubData()
    return render_template("aeroclubs.html", liste=listeAeroclub, infoErr=msg)


@app.route("/component-dropdown")
def component_dropdown():
    return render_template("component-dropdown.html")


@app.route("/gérer-profils")
@app.route("/gérer-profils/<infoMsg>")
def gérer_profils(infoMsg=''):
    msg, listeMembre = bdd.get_membreData()
    print(msg)
    return render_template("gérer-profils.html", liste=listeMembre, infoErr=msg, info=infoMsg)


@app.route("/webmaster")
def webmaster():
    return render_template("webmaster.html")

# traitement du formulaire d'authentification


@app.route("/login", methods=["POST"])
def login():
    # f.sessionTest()
    login = request.form['login']
    password = request.form['mdp']
    msg = f.verifAuth(login, password)
    print(msg)
    if "idUser" in session:  # authentification réussie
        return redirect("/authOK")
    else:  # echec authentification
        return redirect("/connecter/authEchec")

#mdp = hashlib.sha256(mdp.encode())
# mdpC = mdp.hexdigest() #mot de passe chiffré
#add_user(email, nom, prenom, statut, login, motPasse, avatar)


@app.route("/addMembre", methods=['POST'])
def addMembre():
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['pseudo']
    motPasse = request.form['mdp']
    statut = request.form['statut']
    avatar = request.form['avatar']
    idAeroclub = request.form['idAeroclub']
    msg = bdd.add_membreData(nom, prenom,
                             mail, login, motPasse, statut, avatar, idAeroclub)
    if msg == "addMembreOK":
        return redirect("/addUserOK")
    else:
        return redirect("/addUserProblem")


@app.route("/logout")  # menu se déconnecter
def logout():
    session.clear()  # suppression de la session
    return redirect("/connecter/logoutOK")


@app.route("/suppMembre")
def suppMembre():
    idUser = request.args.get("userDel")
    msg = bdd.del_membreData(idUser)
    print(msg)
    if msg == "suppMembreOK":
        return redirect("/gérer-profils/delOK")
    else:
        return redirect("/gérer-profils/delProblem")


@app.route("/updateMembre", methods=['POST'])
def updateMembre():
    idUser = request.form['pk']
    champ = request.form['name']
    newvalue = request.form['value']
    msg = bdd.update_membreData(champ, idUser, newvalue)
    print(msg)
    return msg


@app.route("/calendrier")
def calendrier():
    return render_template("calendrier.html")


@app.route("/load_events", methods=["POST"])
def load_events():
    data = bdd.get_eventsData()[1]
    return jsonify(data)


@app.route("/create_events", methods=["POST", "GET"])
def create_events():
    text = request.form['text']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    try:
        msg, lastId = bdd.add_eventData(text, start_date, end_date)
        return jsonify(lastId)
    except:
        return render_template("calendrier.html")

@app.route("/updateAeroclub", methods=['POST'])
def updateAeroclub():
    idAeroclub = request.form['pk']
    champ = request.form['name']
    newvalue = request.form['value']
    msg = bdd.update_aeroclubData(champ, idAeroclub, newvalue)
    return msg


@app.route("/delete_events", methods=["POST"])
def delete_events():
    id = request.form['id']
    try:
        msg = bdd.delete_eventData(id)
        return jsonify(msg)
    except:
        return render_template("calendrier.html")


@app.route("/update_events", methods=["POST"])
def update_events():
    print('on rentre')
    id = request.form['id']
    text = request.form['text']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    try:
        msg = bdd.update_eventData(id, text, start_date, end_date)
        return jsonify(msg)
    except:
        return render_template("calendrier.html")