from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def page():
    flag = False
    wrong = False
    if request.method == "POST":
        if "губкина" in request.form.get("street", "").lower():
            flag = True
        else:
            wrong = True
    return render_template("page.html", flag=flag, wrong=wrong)

if __name__ == '__main__':
    app.run()