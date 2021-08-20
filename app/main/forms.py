from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,TextField,SelectField,PasswordField,FormField
from wtforms.validators import Required


class ProfileUpdate(FlaskForm):
    bio=TextAreaField(label="Bio Data",validators=[Required()])
    
    save=SubmitField('Save')
    
class PitchForm(FlaskForm):
    category=TextField(label="Category",validators=[Required()])
    content=TextAreaField(label='Pitch',validators=[Required()])
    submit=SubmitField('Post')
    
    
class CommentForm(FlaskForm):
    comment=TextAreaField("Comment",validators=[Required()])
    submit=SubmitField('Send')
    
    
#Group 2

class OrderForm(FlaskForm):

    pizza_type = SelectField('Choose your Pizza', choices =[('bacon_supreme:', 'Bacon Supreme'),('veggie_delight', 'Veggie Delight'), ('meat_deluxe', 'Meat Deluxe'), ('pizza_italiano', 'Pizza Italiano'), ('hawaiian', 'Hawaiian')])
    pizza_size = SelectField('Size', choices =[('small:', 'Small'),('medium:', 'Medium'), ('large:', 'Large')])
    pizza_crust = SelectField('Crust', choices =[('crispy', 'Crispy'),('stuffed', 'Stuffed'), ('gluten_free', 'Gluten Free')])
    pizza_toppings = SelectField('Topping', choices =[('bacon', 'Bacon'),('pepperoni', 'Pepperoni'), ('onions', 'Onions'), ('sausage', 'Sausage'), ('mushrooms:', 'Mushrooms')])
    pizza_delivery = SelectField("Delivery/Takeout",choices=[("delivery", "Delivery"), ("takeout", "Take Out")])
    
    submit = SubmitField("ORDER NOW!!")
