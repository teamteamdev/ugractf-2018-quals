import hashlib
from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

USERS = [
    ("", ""),
    ("admin", "12344551342115131"),
    ("flagkeeper", "fhteyrjqoypjryary"),
    ("john", "johnjohnjohn"),
    ("mary", "ery24352ewjtawtew"),
    ("user", "user")
]

HASHES = [""]

for i in range(1, 6):
    HASHES.append(hashlib.sha1(str(i).encode()).hexdigest())


@app.route("/", methods=["GET", "POST"])
def page():
    error = False
    
    if request.method == "POST":
        login = request.form.get("login", "")
        password = request.form.get("password", "")
        try:
            uid = USERS.index((login, password))
            if uid > 0:
                resp = make_response(redirect('/'))
                resp.set_cookie("session", HASHES[uid])
                return resp
        except:
            error = True
    
    try:
        uid = HASHES.index(request.cookies.get("session", ""))
    except:
        uid = 0
        
    message = ""
    guest = False
    if uid == 2:
        message = "ugractf_use_secure_sessions"
    elif uid != 0:
        message = "Вы вошли как " + USERS[uid][0]
    else:
        guest = True
    return render_template("page.html", guest=guest, message=message, error=error)

@app.route('/logout/')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie("session", "")
    return resp
    
if __name__ == "__main__":
    app.run()