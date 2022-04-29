from flask import session
from ..model import bdd as bdd
import hashlib

def sessionTest():
    # déclaration des variables de sessions
    session["idUser"]=2
    session["prenom"]="Louis"
    session["nom"]="Blériot"
    session["mail"]="louis.bleriot@enac.fr"
    session["avatar"]="8.png"

    # appel des variables de sessions (dans .py)
    nomComplet = session["prenom"]+" "+session["nom"]
    # Modification d'une variable de session
    session["mail"]="bleriot@gmail.com"
    # test de l'existence de session["idUser"]
    if "idUser" in session:
        print("idUser existe dans la session")
    else:
        print("session['idUser'] n'existe pas")
    # suppression de session["mail"] uniquement
    session.pop("mail")
    # suppression de toutes les variables de session
    session.clear()

#authentification des utilisateurs
def verifAuth(login, mdp):
    session.clear() #suppression des sessions précédentes
    msg, user = bdd.verifAuthData(login, mdp)
    print(msg)
    
    try:
        session["idUser"] = user["idUser"]
        session["nom"] = user["nom"]
        session["prenom"] = user["prenom"]
        session["mail"] = user["mail"]
        session["statut"] = user["statut"]
        session["avatar"] = user["avatar"]
        info = msg
    except TypeError as err:
        info="authEchec"
        print("Failed verifAuth : {}".format(err))
        
    return info

mdp = hashlib.sha256(mdp.encode())
mdpC = mdp.hexdigest() #mot de passe chiffré
add_user(email, nom, prenom, statut, login, motPasse, avatar)