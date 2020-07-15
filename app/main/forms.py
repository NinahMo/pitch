from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title =StringField('Title', validators=[Required()])
    description = TextAreaField("Write your pitch ?",validators=[Required()])
    category = RadioField('Label', choices=[ ('promotionpitch','promotionpitch'),('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')],validators=[Required()])
    submit = SubmitField('submit')

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class DownvoteForm(FlaskForm):
    submit = SubmitField()