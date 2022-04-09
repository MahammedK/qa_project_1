from app import app, db, #dog
from flask import Flask, render_template, request, url_for, redirect
from flask_testing import TestCase

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

        def setUp(self):
            db.create_all()

            test_dog = Dog(#Name=, age=, breed=)

            db.session.add(test_dog)
            db.session.commit()

        def tearDown(self):
            db.sessin.remove()
            db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
    response = self.client.get(url_for(#'hello_internet'))
    self.assertEqual(respose.status_code, 200)

    def test_home_get(self):
    response = self.client.get(url_for(#'about'))
    self.assertEqual(respose.status_code, 200)

    def test_post_req(self):
        response = self.client.post(url_for(#'dog_form'), data = dict(name="Fido", age=7, breed="lab"), follow_redirects=True)
        self.assertIn(b'Hello', response.data)
    
#url endpoints, tests above 3 marks
# integration testing (having a test that aceesses a database) def setUp 4th mark
#disussion in readme

class TestData(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('about'))
        assert #"Fido" in response.data.decode()