import hashlib
from flask import Flask, request, render_template

from manage_user import insert_user, retrieve_username, retrieve_users

app = Flask(__name__)
app.config["DEBUG"] = True

# salt keyword (prod: store it in a .env file)
SALT = "a!M@7p*eUUDRHt"

# render error page 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>OOPS</h1> <p> Page not found </p>", 404

# render signup page (to be checked)
@app.route('/signup', methods = ["GET", "POST"])
def signup():
    
    # create the var to handle user messages
    message = ""
    
    # retrieve all encrypted usernames
    existing_user = retrieve_username()
    
    if request.method == "POST":
        
        # get username and password from form
        user_name = request.form["username"]
        user_password = request.form['password']
        
        # hash the user name and password
        secure_name = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
        secure_password = hashlib.sha256((user_password+SALT).encode('utf-8')).hexdigest()
               
        # formal check over username and password
        # empty username
        if user_name == "":
            message = "[!] Username cannot be empty!"
        
        # empty password                   
        elif user_password == "":
            message = "[!] Password cannot be empty!"
        
        # password min length
        elif len(user_password) < 8:
            message = "[!] Password must be at least 8 characters long!"
        
        # password with no digits
        elif not any(char.isdigit() for char in user_password):
            message = "[!] Password must contain at least a number"
        
        # password with no uppercase
        elif not any(char.isupper() for char in user_password):
            message = "[!] Password must contain at least an uppercase letter"
        
        # password with no spaces
        elif any(char==" " for char in user_password):
            message = "[!] Password cannot contain empty spaces"
        
        # password with no special characters
        elif not any(char in "!@#$%^&*()" for char in user_password):
            message = "[!] Password must contain at least one special character"
        
        # user already exists
        elif any(user[0] in secure_name for user in existing_user):
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

    # create the var to handle user messages
    message = ""
    
    # retrieve all encrypted users
    existing_user = retrieve_users()
    
    if request.method == "POST":
        
        # get username and password from form
        user_name = request.form["username"]
        user_password = request.form['password']
        
        # hash the user name and password
        secure_name = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
        secure_password = hashlib.sha256((user_password+SALT).encode('utf-8')).hexdigest()
        
        # check if user exists and match with password
        for user in existing_user:
            if user[1] == secure_name and user[2] == secure_password:
                message = "[*] User Authenticated!"
            else:
                message = "[!] Username or password is incorrect!"
         
    return render_template("signin.html", message=message)

# render main page
@app.route('/', methods = ["GET"])
def main_page():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(use_reloader=False)
