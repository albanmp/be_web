import mysql.connector
from mysql.connector import errorcode
from ..config import DB_SERVER

###################################################################################
# connexion au serveur de la base de données

def connexion():
    cnx = ""
    try:
        cnx = mysql.connector.connect(**DB_SERVER)
        error=None
    except mysql.connector.Error as err:
        error=err
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)
    return cnx, error
    

#################################################################################
# fermeture de la connexion au serveur de la base de données

def close_bd(cursor, cnx):
    cursor.close()
    cnx.close()

#################################################################################
# Retourne toutes les données de la table membres
def get_membreData():
    
    try:
        cnx, error = connexion()
        if error is not None: 
            return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM identification"
        cursor.execute(sql)
        listeMembre = cursor.fetchall()
        close_bd(cursor, cnx)
        msg = "OKmembres"
    except mysql.connector.Error as err:
        listeMembre = None
        msg = "Failed get membres data : {}".format(err)
    return msg, listeMembre

#################################################################################
#suppression d'un membre
def del_membreData(idUser):
    try:
        cnx, error = connexion()
        if error is not None: 
            return error, None
        cursor = cnx.cursor()
        sql = "DELETE FROM identification WHERE idUser=%s;"
        param = (idUser,)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "suppMembreOK"
    except mysql.connector.Error as err:
        msg = "Failed del membres data : {}".format(err)
    return msg

#################################################################################
#ajout d'un membre
def add_membreData(nom, prenom, mail, login, motPasse, statut, avatar):
    try:
        cnx, error = connexion()
        if error is not None: 
            return error, None
        cursor = cnx.cursor()
        sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        param = (nom, prenom, mail, login, motPasse, statut, avatar)
        cursor.execute(sql, param)
        lastId = cursor.lastrowid  # récupère le dernier idUser, généré par le serveur sql
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "addMembreOK"
    except mysql.connector.Error as err:
        msg = "Failed add membres data : {}".format(err)
    return msg, lastId

#################################################################################
#modification d'une donnée dans la table membre
def update_membreData(champ, idUser, newvalue):
    try:
        cnx, error = connexion()
        if error is not None: 
            return error, None
        cursor = cnx.cursor()
        sql = "UPDATE identification SET "+champ+" = %s WHERE idUser = %s;"
        param = (newvalue, idUser)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "updateMembreOK"
    except mysql.connector.Error as err:
        msg = "Failed update membres data : {}".format(err)
    return msg

def verifAuthData(login, mdp):
    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM identification WHERE login=%s and motPasse=%s"
        param=(login, mdp)
        cursor.execute(sql, param)
        user = cursor.fetchone()
        close_bd(cursor, cnx)
        msg = "authOK"
    except mysql.connector.Error as err:
        user = None
        msg = "Failed get Auth data : {}".format(err)
    return msg, user

##########################################################################
###  enregistrement des données provenant du fichier excel
def saveDataFromFile(data):
    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor()
        # suppression des données précédentes
        sql1 = "TRUNCATE TABLE identification;"
        cursor.execute(sql1)
        # insertion des nouvelles données
        for d in data:
            sql = "INSERT INTO identification (idUser, nom, prenom, mail, login, motPasse, statut, avatar) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s); ;"
            param = (d['nom'], d['prenom'], d['mail'], d['login'], d['motPasse'], d['statut'], d['avatar'])
            cursor.execute(sql, param)
            cnx.commit()
        #changement valeur autoincrement
        sql2="ALTER TABLE identification AUTO_INCREMENT=%s;" 
        param2 = (len(data),)
        cursor.execute(sql2, param2)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "addDataFromFileOK"
    except mysql.connector.Error as err:
        msg = "Failed saveDataFromFile data : {}".format(err)
    return msg
    
