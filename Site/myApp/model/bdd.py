import mysql.connector
from flask import session
from mysql.connector import errorcode
from ..config import DB_SERVER
from datetime import datetime

###################################################################################
# connexion au serveur de la base de données


def connexion():
    cnx = ""
    try:
        cnx = mysql.connector.connect(**DB_SERVER)
        error = None
    except mysql.connector.Error as err:
        error = err
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
# suppression d'un membre


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
# ajout d'un membre


def add_membreData(nom, prenom, mail, login, motPasse, statut, avatar, idAeroclub):
    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor()
        sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut, avatar, idAeroclub) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        param = (nom, prenom, mail, login, motPasse, statut, avatar, idAeroclub)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "addMembreOK"
    except mysql.connector.Error as err:
        msg = "Failed add membres data : {}".format(err)
        print(msg)
    return msg

#################################################################################
# modification d'une donnée dans la table membre


def update_membreData(champ, idUser, newvalue):
    try:
        cnx, error = connexion()
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
        sql = "SELECT * FROM Identification WHERE login=%s and motPasse=%s"
        param = (login, mdp)
        cursor.execute(sql, param)
        user = cursor.fetchone()
        close_bd(cursor, cnx)
        msg = "authOK"
    except mysql.connector.Error as err:
        user = None
        msg = "Failed get Auth data : {}".format(err)
    return msg, user

##########################################################################
# enregistrement des données provenant du fichier excel


def saveDataFromFile(data):
    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor()
        # insertion des nouvelles données
        for d in data:
            sql = "INSERT INTO events (id, start_date, end_date, text, color) VALUES (NULL, %s, %s, %s, %s)"
            param = (datetime.strptime(d['start_date'], "%Y-%m-%d %H:%M:%S"), datetime.strptime(d['end_date'], "%Y-%m-%d %H:%M:%S"), d['text'], d['color'])
            cursor.execute(sql, param)
            cnx.commit()
        # changement valeur autoincrement
        sql2 = "ALTER TABLE events AUTO_INCREMENT=%s;"
        param2 = (len(data),)
        cursor.execute(sql2, param2)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "addDataFromFileOK"
    except mysql.connector.Error as err:
        msg = "Failed saveDataFromFile data : {}".format(err)
    return msg

#################################################################################
# Retourne toutes les données de la table events


def get_eventsData():
    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM events"
        cursor.execute(sql)
        listeEvents = cursor.fetchall()
        close_bd(cursor, cnx)
        msg = "OKmembres"
    except mysql.connector.Error as err:
        listeEvents = None
        msg = "Failed get events data : {}".format(err)
    for event in listeEvents:
        event['start_date'] = str(event['start_date'].year)+"-"+str(event['start_date'].month)+"-"+str(
            event['start_date'].day)+" "+str(event['start_date'].hour)+":"+str(event['start_date'].minute)
        event['end_date'] = str(event['end_date'].year)+"-"+str(event['end_date'].month)+"-"+str(
            event['end_date'].day)+" "+str(event['end_date'].hour)+":"+str(event['end_date'].minute)
    return msg, listeEvents


def add_eventData(text, start_date, end_date):
    if session:
        try:
            cnx, error = connexion()
            if error is not None:
                return error, None
            cursor = cnx.cursor()
            sql = "INSERT INTO events (start_date, end_date, text, color) VALUES (%s, %s, %s, %s);"
            sql1 = "SELECT * FROM Aeroclub"
            cursor.execute(sql1)
            listeAeroclub = cursor.fetchall()
            color = "blue"
            for aeroclub in listeAeroclub:
                if aeroclub[0] == session["idAeroclub"]:
                    color = str(aeroclub[2])
            cursor = cnx.cursor()
            param = (str(start_date), str(end_date), text, color)
            cursor.execute(sql, param)
            lastId = cursor.lastrowid
            cnx.commit()
            close_bd(cursor, cnx)
            msg = "addEventOK"
        except mysql.connector.Error as err:
            msg = "Failed add event data : {}".format(err)
            lastId = None
        print(msg)
        return msg, lastId


def get_aeroclubData():

    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM Aeroclub"
        cursor.execute(sql)
        listeAeroclub = cursor.fetchall()
        close_bd(cursor, cnx)
        msg = "OKaeroclub"
    except mysql.connector.Error as err:
        listeAeroclub = None
        msg = "Failed get aeroclub data : {}".format(err)
    return msg, listeAeroclub


def update_aeroclubData(champ, idAeroclub, newvalue):
    try:
        cnx, error = connexion()
        cursor = cnx.cursor()
        sql = "UPDATE aeroclub SET "+champ+" = %s WHERE idAeroclub = %s;"
        param = (newvalue, idAeroclub)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "updateAeroclubOK"
    except mysql.connector.Error as err:
        msg = "Failed update aeroclubs data : {}".format(err)
    return msg


def delete_eventData(id):
    if session:
        try:
            cnx, error = connexion()
            if error is not None:
                return error, None
            cursor = cnx.cursor()
            sql1 = "SELECT * FROM Aeroclub"
            cursor.execute(sql1)
            listeAeroclub = cursor.fetchall()
            color = "blue"
            for aeroclub in listeAeroclub:
                if aeroclub[0] == session["idAeroclub"]:
                    color = str(aeroclub[2])
            cursor = cnx.cursor()
            sql2 = "SELECT * FROM events"
            cursor.execute(sql2)
            listeEvents = cursor.fetchall()
            color1 = "blue"
            for event in listeEvents:
                if int(event[0]) == int(id):
                    color1 = str(event[4])
            if color == color1 or session["statut"]==0:
                cursor = cnx.cursor()
                sql = "DELETE FROM events WHERE id=%s;"
                param = (id,)
                cursor.execute(sql, param)
                cnx.commit()
                close_bd(cursor, cnx)
                msg = "suppEventOK"
        except mysql.connector.Error as err:
            msg = "Failed del event data : {}".format(err)
        return msg


def update_eventData(id, text, start_date, end_date):
    if session:
        try:
            cnx, error = connexion()
            cursor = cnx.cursor()
            sql1 = "SELECT * FROM Aeroclub"
            cursor.execute(sql1)
            listeAeroclub = cursor.fetchall()
            color = "blue"
            for aeroclub in listeAeroclub:
                if aeroclub[0] == session["idAeroclub"]:
                    color = str(aeroclub[2])
            cursor = cnx.cursor()
            sql2 = "SELECT * FROM events"
            cursor.execute(sql2)
            listeEvents = cursor.fetchall()
            color1 = "blue"
            for event in listeEvents:
                if int(event[0]) == int(id):
                    color1 = str(event[4])
            if color == color1 or session["statut"]==0:
                cursor = cnx.cursor()
                sql = "UPDATE events SET start_date = %s, end_date = %s, text = %s WHERE id = %s;"
                param = (start_date, end_date, text, id,)
                cursor.execute(sql, param)
                cnx.commit()
                close_bd(cursor, cnx)
                msg = "updateEventOK"
        except mysql.connector.Error as err:
            msg = "Failed update events data : {}".format(err)
        return msg

def get_avionData():

    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM Avions"
        cursor.execute(sql)
        listeAvions = cursor.fetchall()
        close_bd(cursor, cnx)
        msg = "OKavions"
    except mysql.connector.Error as err:
        listeAvions = None
        msg = "Failed get avions data : {}".format(err)
    return msg,listeAvions
