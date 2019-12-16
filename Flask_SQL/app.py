from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)

# Connect to Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/quan_li_tap_chi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


class TagGia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.String(50))
    nganh_id = db.Column(db.Integer)
    hoc_vi = db.Column(db.String(30))
    truong_dai_hoc = db.Column(db.String(50))
    co_quan_id = db.Column(db.Integer)

    def __init__(self, id, ten, nganh_id, hoc_vi, truong_dai_hoc, co_quan_id):
        self.id = id
        self.ten = ten
        self.nganh_id = nganh_id
        self.hoc_vi = hoc_vi
        self.truong_dai_hoc = truong_dai_hoc
        self.co_quan_id = co_quan_id


# TacGia Schema
class TacGiaSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'ten', 'nganh_id', 'hoc_vi', 'truong_dai_hoc', 'co_quan_id')


# Init schema
tacgia_schema = TacGiaSchema(many=False)
tacgias_schema = TacGiaSchema(many=True)


# Create a TacGia
@app.route('/tacgia', methods=['POST'])
def add_tacgia():
    id = request.json['id']
    ten = request.json['ten']
    nganh_id = request.json['nganh_id']
    hoc_vi = request.json['hoc_vi']
    truong_dai_hoc = request.json['truong_dai_hoc']
    co_quan_id = request.json['co_quan_id']

    new_TacGia = TagGia(id, ten, nganh_id, hoc_vi, truong_dai_hoc, co_quan_id)

    db.session.add(new_TacGia)
    db.session.commit()

    return tacgia_schema.jsonify(new_TacGia)


# Run app
if __name__ == '__main__':
    app.run(debug=True)
