from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('Hoo u searchin 4!?', validators=[Required()])
    submit = SubmitField('Submit')
