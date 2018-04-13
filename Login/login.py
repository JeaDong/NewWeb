from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import ValidationError ,SubmitField,StringField
from wtforms.validators import Length,DataRequired,Email

app = Flask(__name__)
boostrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess'



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = LoginForm()
    return render_template('index.html',form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
    