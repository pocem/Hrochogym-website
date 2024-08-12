from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, NumberRange


app = Flask(__name__)

app.secret_key = 'your_secret_key'

class SignupForm(FlaskForm):
    name = StringField('First name', validators=[DataRequired()])
    surname = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    age = IntegerField('Your age', validators=[DataRequired(), NumberRange(min=15, message='You must be at least 15 years old.')])
    gender = RadioField('Gender', choices=[('M', 'Man'), ('W', 'Woman')], validators=[DataRequired()])
    submit = SubmitField('Sign up!')




@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/location/<city>", methods=['GET', 'POST'])
def choose_gym(city):
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        age = form.age.data
        gender = form.gender.data

        print(f"Name: {name}")
        print(f"Surname: {surname}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Age: {age}")
        print(f"Gender: {gender}")

        flash(f"Account created for {form.name.data}!", 'success')
        return redirect(url_for('choose_gym', city=city))

    return render_template('location.html', city=city, form=form)





if __name__ == '__main__':
    app.run(debug=True)