from application import app, db
from application.models import Promotions, Fighters, PromotionsForm, FightersForm
from flask import Flask, render_template, request, url_for, redirect

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/addpromotions', methods = ['GET','POST'])
def addpromotions():
    form = PromotionsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_promotion = Promotions(
                name = form.name.data,
                owner = form.owner.data,
                based = form.based.data
            )
            db.session.add(new_promotion)
            db.session.commit()
            return redirect(url_for("addpromotions"))
        else:
            return render_template('addpromotions.html', form=form)
    else:
        return render_template('addpromotions.html', form=form)

@app.route('/promotions')
def promotions():
    list_of_promotions = Promotions.query.all()
    return render_template('viewpromotions.html', list_of_promotions=list_of_promotions)

# @app.route('/updatepromotions')
# def updatepromotions():
#     promotions_to_update = Promotions.query.all()
#     all_promotions = Promotions.query.all()
#     return render_template('updatepromotions.html', updatepromotions=updatepromotions)


# @app.route('/addfighters', methods = ['GET','POST'])
# def addfighters():
#     form = FightersForm()
#     promotions = request.form.get.first('promotions_id')
#     if request.method == "POST":
#         if form.validate_on_submit():
#             new_fighter = Fighters(
#                 name = form.name.data,
#                 weightclass = form.weightclass.data,
#                 based = form.based.data,
#                 promotions_id = promotions
#             )
#             db.session.add(new_fighter)
#             db.session.commit()
#             return redirect(url_for("addfighters"))
#     else:
#         return render_template('addfighters.html', form=form)

# @app.route('/fighters')
# def fighters():
#     list_of_fighters = Fighters.query.all()
#     return render_template('viewfighters.html', list_of_fighters=list_of_fighters)



