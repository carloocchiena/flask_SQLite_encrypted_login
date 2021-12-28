from flask import Flask, request, render_template

from manage_user import insert_user, retrieve_users

app = Flask(__name__)
app.config["DEBUG"] = True

# render error page 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>OOPS</h1> <p> Page not found </p>", 404

# render signin page (to be completed)
@app.route('/signin', methods = ["GET", "POST"])
def signin():
    
    user_list = ""
    invalid = ""
    
    if request.method == "POST":
        psw = request.form['password']
        
        if psw == "PASSWORD":
            user_list = retrieve_users()
        else:
            invalid = "[!!!] Wrong password"
  
    return render_template("signin.html", user_list = user_list, invalid=invalid)

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
