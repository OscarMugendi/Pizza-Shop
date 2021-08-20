
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__="users"
    
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),index=True)
    email= db.Column(db.String(50),unique=True,index=True)
    address=db.Column(db.String(255))
    contact=db.Column(db.String(255))
    encryptedpassword= db.Column(db.String(200),index=True)
    
    @property
    def password(self):
        raise AttributeError ("password encrypted!")
    
    @password.setter
    def password(self,password):
        self.encryptedpassword= generate_password_hash(password)
        
    def passwordVerification(self,password):
        return check_password_hash(self.encryptedpassword,password)
    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(int(user_id))
    def __repr__(self):
        return f'User{self.username}'


#Group 2  
        
class Order(db.Model):
    __tablename__="orders"

    id=db.Column(db.Integer, primary_key=True)
    pizza_type = db.Column(db.String(20),index=True)
    pizza_size = db.Column(db.String(9),index=True)
    pizza_crust = db.Column(db.String(9),index=True)
    pizza_toppings = db.Column(db.String(9),index=True)
    pizza_delivery = db.Column(db.String(20),index=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Pizza(db.Model):
    __tablename__="pizzas"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),index=True)
    toppings=db.Column(db.String(9),index=True)
    description=db.Column(db.String(40),index=True)

    #order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Topping(db.Model):
    __tablename__="toppings"

    id=db.Column(db.Integer,primary_key=True)
    pepperoni=db.Column(db.String(10),index=True)
    bacon=db.Column(db.String(9),index=True)
    mushrooms=db.Column(db.String(10),index=True)
    onions=db.Column(db.String(9),index=True)
    sausage=db.Column(db.String(9),index=True)

    #order_id = db.Column(db.Integer,db.ForeignKey("orders.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Size(db.Model):
    __tablename__="sizes"

    id=db.Column(db.Integer,primary_key=True)
    small=db.Column(db.String(9),index=True)
    medium=db.Column(db.String(9),index=True)
    large=db.Column(db.String(9),index=True)

    #order_id = db.Column(db.Integer,db.ForeignKey("orders.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Crust(db.Model):
    __tablename__="crusts"

    id=db.Column(db.Integer,primary_key=True)
    crispy=db.Column(db.String(12),index=True)
    stuffed=db.Column(db.String(12),index=True)
    gluten_free=db.Column(db.String(12),index=True)

    #order_id = db.Column(db.Integer,db.ForeignKey("orders.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()