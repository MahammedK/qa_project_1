from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class Promotions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    promotions_name = db.Column(db.String(50), unique=True)
    promotions_owner = db.Column(db.String(50), nullable=False)
    promotions_based = db.Column(db.String(50), nullable=False)
    fighters = db.relationship("Fighters", backref="promotionsbr")

class PromotionsForm(FlaskForm):
    promotions_name = StringField("Promotion Name: ")
    promotions_owner = StringField("Owner Name: ")
    promotions_based = StringField("Country promotion is based: ")
    submit = SubmitField("Submit")

class Fighters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fighters_name = db.Column(db.String(50), nullable=False)
    fighters_weightclass = db.Column(db.String(50), nullable=False)
    fighters_based = db.Column(db.String(50), nullable=False)
    promotions_id = db.Column(db.Integer, db.ForeignKey('promotions.id'), nullable=False)

class FightersForm(FlaskForm):
    fighters_name = StringField("Fighter Name: ")
    fighters_weightclass = SelectField("Fighters Weightclass: ", choices=[
        ("flyweight", "Flyweight"),
        ("bantamweight", "Bantamweight"),
        ("featherweight", "Featherweight"),
        ("lightweight", "Lightweight"),
        ("welterwight", "Welterweight"),
        ("middlewight", "Middleweight"),
        ("light heavyweight", "Light Heavyweight"),
        ("heavyweight", "Heavyweight"),
        ("womens strawweight", "Women's Strawweight"),
        ("womens flyweight", "Women's Flyweight"),
        ("womens bantamweight", "Women's Bantamweight"),
        ("womens featherweight", "Women's Featherweight")
    ])
    fighters_based = StringField("Country fighter is based: ")
    promotions_name = SelectField (u'Promotion Name', choices = [])
    submit = SubmitField("Submit")