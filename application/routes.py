from application import app, db
from application.models import Promotions, Fighters, PromotionsForm, FightersForm
from flask import Flask, render_template, request, url_for, redirect

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addpromotions', methods = ['GET','POST'])
def addpromotions():
    form = PromotionsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_promotion = Promotions(
                promotions_name = form.promotions_name.data,
                promotions_owner = form.promotions_owner.data,
                promotions_based = form.promotions_based.data
            )
            db.session.add(new_promotion)
            db.session.commit()
            return redirect(url_for("addpromotions"))
        else:
            return render_template('addpromotions.html', form=form)
    else:
        return render_template('addpromotions.html', form=form)

@app.route('/viewpromotions')
def viewpromotions():
    list_of_promotions = Promotions.query.all()
    return render_template('viewpromotions.html', list_of_promotions=list_of_promotions)

@app.route('/delete_promotions/<promotions_name>', methods=['GET', 'DELETE'])
def delete_promotions(promotions_name):
    deletepromotion = Promotions.query.filter_by(promotions_name=promotions_name).first()
    db.session.delete(deletepromotion)
    db.session.commit()
    return redirect(url_for('viewpromotions'))

@app.route('/addfighters', methods = ['GET','POST'])
def addfighters():
    form = FightersForm()
    form.promotions_name.choices = [(promotions.id, promotions.promotions_name) for promotions in Promotions.query.order_by(Promotions.promotions_name).all()]
    if request.method == "POST":
        if form.validate_on_submit():
            new_fighter = Fighters(
                fighters_name = form.fighters_name.data,
                fighters_weightclass = form.fighters_weightclass.data,
                fighters_based = form.fighters_based.data,
                promotions_id = form.promotions_name.data
            )
            db.session.add(new_fighter)
            db.session.commit()
            return redirect(url_for("addfighters"))
        else:
            return render_template('addfighters.html', form=form)
    else:
        return render_template('addfighters.html', form=form)

@app.route('/viewfighters')
def viewfighters():
    list_of_fighters = Fighters.query.all()
    return render_template('viewfighters.html', list_of_fighters=list_of_fighters)

@app.route('/delete/<fighters_name>', methods = ['GET', 'DELETE'])
def delete(fighters_name):
    deletefighter = Fighters.query.filter_by(fighters_name=fighters_name).first()
    db.session.delete(deletefighter)
    db.session.commit()
    return redirect(url_for('viewfighters'))

@app.route('/update/<fighters_name>', methods = ['GET','POST'])
def update(fighters_name):
    form = FightersForm()
    if request.method == 'POST':
        updatefighter = Fighters.query.filter_by(fighters_name=fighters_name).first()
        if updatefighter: 
            updatefighter.fighters_name = form.fighters_name.data
            updatefighter.fighters_weightclass = form.fighters_weightclass.data
            updatefighter.fighters_based = form.fighters_based.data
            updatefighter.promotions_name = form.promotions_name.data
            db.session.commit()
            return redirect(url_for('viewfighters'))
    else:
        return render_template('addfighters.html', form=form, fighters_name=fighters_name)


