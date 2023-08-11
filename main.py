from flask import Flask, request, jsonify

app = Flask(__name__)

# HOME ROUTE
@app.route("/")
def home():
    welcomeMessage = 'Welcome to Places API, here is the available endpoints \n 1. CREATE /create-place'
    #flas2. READ /list-places
    #3. UPDATE /update-place
    #4. DELETE /delete-place
    return welcomeMessage

# POST METHOD (CREATE) creation of a new place
@app.route("/create-place", methods=["POST"])
def create_place():
    #data = request.get_json()
    #DATABASE INSERT TO VALUES
    return "Created place" #jsonify(data), 201

# GET METHOD (READ) listing of all available places
@app.route("/list-places")
def list_places():
    #data  = #DATABASE SELECT FROM
    return "Listed places"#jsonify(data), 200

# PUT METHOD (UPDATE) update of details for a specific place
@app.route("/update-place/<place_id>")
def update_place(place_id):
    #DATABASE UPDATE FROM WHERE place_id
    #data = SELECT FROM WHERE place_id
    return "Updated place"#jsonify(data), 200

# DELETE METHOD (DELETE) deletion of a place
@app.route("/delete-place/<place_id>")
def delete_place(place_id):
    #DATABASE DELETE FROM WHERE place_id
    #data = SELECT FROM WHERE place_id
    return "Deleted place"#jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)