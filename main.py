from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__, template_folder='web/templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///places.db"  # Using SQLite for simplicity
db = SQLAlchemy(app)

# Model definition
class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255)) #optional
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

#API Routes
# POST METHOD (CREATE) creation of a new place
@app.route("/api/places", methods=["POST"])
def api_create_place():
    data = request.json

    if "name" not in data:
        return jsonify({"error": "Place name not provided"}), 400
    
    if "latitude" not in data:
        return jsonify({"error": "Place latitude not provided"}), 400
    
    if "longitude" not in data:
        return jsonify({"error": "Place longitude not provided"}), 400

    new_place = Place(name=data['name'], description=data.get('description'),
                  latitude=data['latitude'], longitude=data['longitude'])

    db.session.add(new_place)
    db.session.commit()
    return jsonify({"message": "Place created successfully", "id": new_place.id}), 201

# GET METHOD (READ) listing of all available places
@app.route("/api/places", methods = ["GET"])
def api_get_places():
    places = Place.query.all()
    result = [{"id": place.id, "name": place.name, "description": place.description,
               "latitude": place.latitude, "longitude": place.longitude} for place in places]
    return jsonify(result), 200

# PUT METHOD (UPDATE) update of details for a specific place
@app.route("/api/places/<int:place_id>", methods=["PUT"])
def api_update_place(place_id):
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
@app.route("/api/places/<int:place_id>", methods=["DELETE"])
def api_delete_place(place_id):
   place = Place.query.get(place_id)

   if not place:
        return jsonify({"error": "Place not found"}), 404
   
   db.session.delete(place)
   db.session.commit()
   return jsonify({"message": "Place deleted successfully"}), 200  

#Web Interface Routes
API_BASE_URL = 'http://127.0.0.1:5000/api'

# HOME ROUTE
@app.route("/")
def web_home():
    return render_template('base.html')

#Web Create places
@app.route('/create', methods=['GET', 'POST'])
def web_create_place():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "description": request.form['description'],
            "latitude": float(request.form['latitude']),
            "longitude": float(request.form['longitude'])
        }
        response = requests.post(f'{API_BASE_URL}/places', json=data)
        if response.status_code == 201:
            return redirect(url_for('list_places'))
    return render_template('create_place.html')

#Web List of all places
@app.route('/list')
def web_list_places():
    response = requests.get(f'{API_BASE_URL}/places')
    places = response.json()
    return render_template('list_places.html', places=places)

#Web Update place
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def web_update_place(id):
    response = requests.get(f'{API_BASE_URL}/places/{id}')
    place = response.json()

    if request.method == 'POST':
        updated_data = {
            "name": request.form['name'],
            "description": request.form['description'],
            "latitude": float(request.form['latitude']),
            "longitude": float(request.form['longitude'])
        }
        response = requests.put(f'{API_BASE_URL}/places/{id}', json=updated_data)
        if response.status_code == 200:
            return redirect(url_for('list_places'))

    return render_template('update_place.html', place=place)

#Web Delete place
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def web_delete_place(id):
    response = requests.get(f'{API_BASE_URL}/places/{id}')
    place = response.json()

    if request.method == 'POST':
        response = requests.delete(f'{API_BASE_URL}/places/{id}')
        if response.status_code == 204:
            return redirect(url_for('list_places'))

    return render_template('confirm_delete.html', place=place)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)