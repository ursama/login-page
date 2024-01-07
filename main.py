from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms import validators
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "smok"


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[validators.DataRequired(), validators.Email()],
                       render_kw={'style': 'width: 30ch'})
    password = PasswordField(label='Password', validators=[validators.DataRequired(), validators.Length(min=8)],
                             render_kw={'style': 'width: 30ch'})
    log = SubmitField(label='Log in')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
