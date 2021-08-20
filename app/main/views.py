from flask import Blueprint, request, render_template,redirect,url_for,abort
from flask_login import login_required
from .import main
from app import db
from .forms import OrderForm
from app.models import Pizza,Topping,Size,Crust,Order


@main.route('/')
def index():
    title="Home"

    return render_template('index.html',title=title)

@main.route('/home')
@login_required
def homepage():
  
    title="Homepage"

    return render_template('home.html',title=title)

@main.route('/order', methods=['GET','POST'])
@login_required
def order():

    form = OrderForm()
    if form.validate_on_submit():
        #order_list=Order.query.filter_by(order_list=order.pizza_delivery).first_or_404()
        pizza_order = Order(
            pizza_type=form.pizza_type.data,
            pizza_size=form.pizza_size.data,
            pizza_crust=form.pizza_crust.data,
            pizza_toppings=form.pizza_toppings.data,
            pizza_delivery=form.pizza_delivery.data
        )
        #db.session.add(order)
        db.session.commit()

        return redirect(url_for('main.index'))
  
    title="Orders"

    return render_template('order.html',title=title, OrderForm=form)



