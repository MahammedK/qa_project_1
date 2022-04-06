from flask import Flask
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=[])
def home():
    return "Home Page"

@app.route('/promotors/<organisation>')
def promotors(organisation):
    if organisation.lower() == "ufc":
        return redirect(url_for("ufc"))
    if organisation.lower() == "bellator":
        return "Welcome to the Bellator fighters page"
    else:
        return f"There are no promotions affiliated with us that go by the name {organisation}"

@app.route('/ufc')
def ufc():
    return "Welcome to the UFC fighters page"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)