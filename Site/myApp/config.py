ENV = "development"
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 0 #vider le cache SECRET_KEY="maCleSuperSecurisee"
SECRET_KEY = "maCleSuperSecurisee"
 #Configuration du serveur web
WEB_SERVER = {
   "host": "localhost",
   "port":8080,
}
#Configuration du serveur de BDD
DB_SERVER = {
   "user": "root",
   "password": "",
   "host": "localhost",
   "port": 3306, #8889 si MAC
   "database": "gsea_cours",  #nom de la BDD
   "raise_on_warnings": True
}