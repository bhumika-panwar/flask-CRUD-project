from flask_wtf import  FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired
#Class 1
class StudentForm(FlaskForm):
    rollno = StringField('Rollno', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    feesamount = FloatField('Fees Amount', validators=[DataRequired()])
    paymentmode = SelectField('Payment Mode', choices=[('Cash','Cash'),('Card','Card')], validators=[DataRequired()])
    submit=SubmitField('Submit')
#Class 2
class SearchForm(FlaskForm):
    search = StringField('Search By Roll No Or Name',validators=[DataRequired()])
    submit=SubmitField('Search')

#Class N
        


