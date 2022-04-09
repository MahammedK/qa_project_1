from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class Promotions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    owner = db.Column(db.String(50), nullable=False)
    based = db.Column(db.String(50), nullable=False)
    fighters = db.relationship("Fighters", backref="promotionsbr")

class PromotionsForm(FlaskForm):
    name = StringField("Promotion Name: ")
    owner = StringField("Owner Name: ")
    based = StringField("Country promotion is based: ")
    submit = SubmitField("Submit")

class Fighters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    weightclass = db.Column(db.String(50), nullable=False)
    based = db.Column(db.String(50), nullable=False)
    promotions_id = db.Column(db.Integer, db.ForeignKey('promotions.id'), nullable=False)

class FightersForm(FlaskForm):
    name = StringField("Fighter Name: ")
    weightclass = SelectField("Fighters Weightclass: ", choices=[
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
    based = StringField("Country fighter is based: ")
    submit = SubmitField("Submit")