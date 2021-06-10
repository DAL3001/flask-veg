from flask import request
from app import app, db
from models import VegModel

@app.route('/addveg', methods=['POST'])
def put():
    if request.is_json:
        data = request.get_json()
        new_veg = VegModel(name=data['name'], colour=data['colour'], length=data['length'])
        db.session.add(new_veg)
        db.session.commit()
        return {"message": f"Vegetable '{new_veg.name}' has been created successfully."}
    else:
        return {"error": "POST request doesn't contain JSON, can't add another vegetable"}


@app.route('/getveg', methods=['GET'])
def retrieve():
    allveg = VegModel.query.all()
    results = [
        {
            "name": veg.name,
            "colour": veg.colour,
            "length": veg.length
        } for veg in allveg
    ]
    return {"allveg" : results}