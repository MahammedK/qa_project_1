from application import app, db
from application.models import Promotions, Fighters, PromotionsForm, FightersForm
from flask import Flask, render_template, request, url_for, redirect
from flask_testing import TestCase

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()

        test_promotion = Promotions(id = 1, promotions_owner = "Peter Murray", promotions_based = "USA")
        test_fighter = Fighters(fighters_name = "Kayla Harrison", fighters_weightclass = "Women's Featherweight", fighters_based = "USA", promotions_id = 1)

        db.session.add(test_promotion)
        db.session.add(test_fighter)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_addpromotions_get(self):
        response = self.client.get(url_for('addpromotions'))
        self.assertEqual(response.status_code, 200)

    def test_viewpromotions_get(self):
        response = self.client.get(url_for('viewpromotions'))
        self.assertEqual(response.status_code, 200)

    def test_delete_promotions_get(self):
        response = self.client.get(url_for('delete_promotions', promotions_id = 1))
        self.assertEqual(response.status_code, 302)

    def test_addfighters_get(self):
        response = self.client.get(url_for('addfighters'))
        self.assertEqual(response.status_code, 200)

    def test_viewfighters_get(self):
        response = self.client.get(url_for('viewfighters'))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', fighters_name="Kayla Harrison"))
        self.assertEqual(response.status_code, 302)

    def test_update_get(self):
        response = self.client.get(url_for('update', fighters_name = "Kayla Harrison"))
        self.assertEqual(response.status_code, 200)