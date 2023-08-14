from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///places.db"  # Using SQLite for simplicity
db = SQLAlchemy(app)

# Model definition
class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

# HOME ROUTE
@app.route("/")
def home():
    #db.create_all()
    return "Welcome to Places API"

# POST METHOD (CREATE) creation of a new place
@app.route("/places", methods=["POST"])
def create_place():
    data = request.json

    if "name" not in data:
        return jsonify({"error": "Place name not provided"}), 400
    
    if "latitude" not in data:
        return jsonify({"error": "Place latitude not provided"}), 400
    
    if "longitude" not in data:
        return jsonify({"error": "Place longitude not provided"}), 400

    new_place = Place(name=data['name'], description=data.get('description'),
                  latitude=data.get('latitude'), longitude=data.get('longitude'))

    db.session.add(new_place)
    db.session.commit()
    return jsonify({"message": "Place created successfully", "id": new_place.id}), 201

# GET METHOD (READ) listing of all available places
@app.route("/places", methods = ["GET"])
def get_places():
    places = Place.query.all()
    result = [{"id": place.id, "name": place.name, "description": place.description,
               "latitude": place.latitude, "longitude": place.longitude} for place in places]
    return jsonify(result), 200

# PUT METHOD (UPDATE) update of details for a specific place
@app.route("/places/<int:place_id>", methods=["PUT"])
def update_place(place_id):
    place = Place.query.get(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404
    
    data = request.json
    place.name = data["name"]
    place.description = data.get("description")
    place.latitude = data["latitude"]
    place.longitude = data["longitude"]
    db.session.commit()
    return jsonify({"message": "Place updated successfully"}), 200                     

# DELETE METHOD (DELETE) deletion of a place
@app.route("/places/<int:place_id>", methods=["DELETE"])
def delete_place(place_id):
   place = Place.query.get(place_id)

   if not place:
        return jsonify({"error": "Place not found"}), 404
   
   db.session.delete(place)
   db.session.commit()
   return jsonify({"message": "Place deleted successfully"}), 200  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)