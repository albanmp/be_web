from flask import Flask, render_template
app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('myApp.config')
 
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/auth-login")
def auth_login():
    return render_template("auth-login.html")

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

@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/webmaster")
def webmaster():
    return render_template("webmaster.html")