from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@127.0.0.1/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonSchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name")


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)


@app.route('/person', methods=['POST'])
def add_person():
    id = request.json['id']
    name = request.json['name']
    persona = Person(id, name)
    db.session.add(persona)
    db.session.commit()
    return person_schema.jsonify(persona)


@app.route('/persona', methods=['GET'])
def get_person():
    all = Person.query.all()
    result = persons_schema.dump(all)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
