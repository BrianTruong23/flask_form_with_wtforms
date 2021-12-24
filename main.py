from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email,ValidationError
import email_validator
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "any-string-you-want-just-keep-it-secret"


def my_length_check(form, field):
    if len(field.data) < 8:
        raise ValidationError('Field must be at least 8 characters')

class LoginForm(FlaskForm):
    email = StringField(label = 'Email',validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField(label = 'Password',validators=[DataRequired(), my_length_check])
    submit = SubmitField(label = "Log in")



@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)



@app.route("/")
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug= True)