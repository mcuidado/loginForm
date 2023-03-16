from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = "MyS3cretK3y123!"

class LoginForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Submit", validators=[DataRequired()])



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    
    SUCCESS="False"
    login_form = LoginForm()

    if request.method == "POST" and login_form.validate_on_submit() == True:
        SUCCESS="True"
        return render_template("success.html", form=login_form, success=SUCCESS)

    return render_template("login.html", form=login_form, success=SUCCESS)

@app.route("/success", methods=["GET", "POST"])
def success_login():
    return render_template("success.html")
    


if __name__ == "__main__":
    app.run(debug=True)