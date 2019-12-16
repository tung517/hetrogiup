from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
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
        model = Person


@app.route('/')
def index():
    person = Person.query.all()
    person_schema = PersonSchema(many=True)
    output = person_schema.dump(person)
    return jsonify({'person': output})


if __name__ == '__main__':
    app.run(debug=True)
