import hashlib
from flask import Flask, request, render_template

from manage_user import insert_user, retrieve_users

app = Flask(__name__)
app.config["DEBUG"] = True

# render error page 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>OOPS</h1> <p> Page not found </p>", 404

# render signin page (to be checked)
@app.route('/signin', methods = ["GET", "POST"])
def signin():
    
    error = ""
    
    if request.method == "POST":
        
        # get username and password from form
        user_name = request.form["username"]
        user_password = request.form['password']
        
        # hash the user name and password
        secure_name = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
        secure_password = hashlib.sha256(user_password.encode('utf-8')).hexdigest()
        
        # check if username already exist
        if user_name != "":
            for user in retrieve_users():
                if user[1] == secure_name:
                    error = "[!] Username already exist"
                
        # formal check over username and password
        elif user_name == "":
            error = "[!] Username cannot be empty!"
       
        elif user_password == "":
            error = "[!] Password cannot be empty!"
        
        elif len(user_password) < 8:
            error = "[!] Password must be at least 8 characters long!"
        
        elif not any(char.isdigit() for char in user_password):
            error = "[!] Password must contain at least a number"
        
        elif not any(char.isupper() for char in user_password):
            error = "[!] Password must contain at least an uppercase letter"
        
        elif any(char==" " for char in user_password):
            error = "[!] Password cannot contain empty spaces"
        
        elif not any(char in "!@#$%^&*()" for char in user_password):
            error = "[!] Password must contain at least one special character"
        
        # if no error, insert user and password into DB
        else:
            insert_user(secure_name, secure_password)
            error = "[*] User Inserted!"

    # if no error, redirect to signin page   
    return render_template("signin.html", error=error)

# render signup page (to be completed)
@app.route('/signup', methods = ["GET", "POST"])
def signup():
    
    user_list = ""
    invalid = ""
    
    if request.method == "POST":
        psw = request.form['password']
        
        if psw == "PASSWORD":
            user_list = retrieve_users()
        else:
            invalid = "[!!!] Wrong password"
  
    return render_template("signup.html", user_list = user_list, invalid=invalid)

# render main page
@app.route('/', methods = ["GET", "POST"])
def main_page():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(use_reloader=False)
