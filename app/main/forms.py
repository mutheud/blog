from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,RadioField
from wtforms.validators import  Required

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):

    Title = StringField('Tell us about you.',validators = [Required()])
    blog = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    Title = StringField('Tell us about you.',validators = [Required()])
    comment = TextAreaField('Express your thoughts.',validators = [Required()])
    submit = SubmitField('submit')