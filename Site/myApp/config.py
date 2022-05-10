ENV = "development"
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 0 #vider le cache
SECRET_KEY = "maCleSuperSecurisee"
 #Configuration du serveur web
WEB_SERVER = {
   "host": "localhost",
   "port":8080,
}
#Configuration du serveur de BDD
DB_SERVER = {
   "user": "IENAC",
   "password": "IENAC",
   "host": "localhost",
   "port": 8889, #8889 si MAC
   "database": "Web",  #nom de la BDD
   "raise_on_warnings": True
}