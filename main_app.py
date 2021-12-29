import hashlib
from flask import Flask, request, render_template

from manage_user import insert_user, retrieve_users

app = Flask(__name__)
app.config["DEBUG"] = True

# render error page 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>OOPS</h1> <p> Page not found </p>", 404

# render signup page (to be checked)
@app.route('/signup', methods = ["GET", "POST"])
def signup():
    
    message = ""
    
    if request.method == "POST":
        
        # get username and password from form
        user_name = request.form["username"]
        user_password = request.form['password']
        
        # hash the user name and password
        secure_name = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
        secure_password = hashlib.sha256(user_password.encode('utf-8')).hexdigest()
               
        # formal check over username and password
        # empyy username
        if user_name == "":
            message = "[!] Username cannot be empty!"
        
        # empty password                   
        elif user_password == "":
            message = "[!] Password cannot be empty!"
        
        # password min length
        elif len(user_password) < 8:
            message = "[!] Password must be at least 8 characters long!"
        
        # password with digits
        elif not any(char.isdigit() for char in user_password):
            message = "[!] Password must contain at least a number"
        
        # password with uppercase
        elif not any(char.isupper() for char in user_password):
            message = "[!] Password must contain at least an uppercase letter"
        
        # password with no spaces
        elif any(char==" " for char in user_password):
            message = "[!] Password cannot contain empty spaces"
        
        # password with special characters
        elif not any(char in "!@#$%^&*()" for char in user_password):
            message = "[!] Password must contain at least one special character"
        
        # user already exists    (forse la funzione retrieve uccide tutto, da modificare)
        elif user_name != "":
            for user in retrieve_users():
                if user[1] == secure_name:
                    message = "[!] Username already exist"
            
        # if no error, insert user and password into DB
        else:
            insert_user(secure_name, secure_password)
            message = "[*] User Inserted!"

    # if no error, redirect to signup page
    return render_template("signup.html", message=message)

# render signin page (to be completed)
@app.route('/signin', methods = ["GET", "POST"])
def signin():

    message = ""
    
    if request.method == "POST":
        psw = request.form['password']
        
        if psw == "PASSWORD":
            user_list = retrieve_users()
        else:
            invalid = "[!!!] Wrong password"
  
    return render_template("signin.html", message=message)

# render main page
@app.route('/', methods = ["GET"])
def main_page():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(use_reloader=False)
