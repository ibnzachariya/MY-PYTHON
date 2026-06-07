from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equipment.db'
db = SQLAlchemy(app)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Available")

with app.app_context():
    db.create_all()

@app.route('/api/equipment')
def api_equipment():
    items = Equipment.query.all()
    return jsonify([{"id": i.id, "name": i.name, "status": i.status} for i in items])

@app.route('/')
def index():
    items = Equipment.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_equipment():
    new_item = Equipment(name=request.form['name'], status=request.form['status'])
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
