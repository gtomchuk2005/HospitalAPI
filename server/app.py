from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# sample patient data
patients = [
    {"id": 1, "name": 'Greg', "pregnancies": 2},
    {"id": 2, "name": 'Nabil', "pregnancies": 5},
    {"id": 3, "name": 'Jackie', "pregnancies": 9}
]

next_patient_id = 4

# GET request all patients
@app.route("/patients", methods=['GET'])
def get_all_patients():
    return jsonify(patients)

def get_patient(id):
    for patient in patients:
        if patient['id'] == id:
            return patient
    return None

# GET request single patient
@app.route("/patients/<int:id>", methods=['GET'])
def get_patient_by_id(id: int):
    patient = get_patient(id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404    
    return jsonify(patient)

def is_valid_patient(patient):
    properties = ['name','pregnancies']
    for key in patient.keys():
        if key not in properties:
            return False
    return True

# POST request 
@app.route("/patients", methods=['POST'])
def create_patient():
    global next_patient_id

    created_patient = json.loads(request.data)
    if not is_valid_patient(created_patient):
        return jsonify({'Error': 'Invalid patient'}), 400
    
    created_patient['id'] = next_patient_id
    next_patient_id += 1

    patients.append(created_patient)
    return '', 201, {'Location': f'/patients/{created_patient["id"]}'}

# PUT request
@app.route("/patients/<int:id>", methods=['PUT'])
def update_patient(id: int):
    patient = get_patient(id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404
    
    updated_patient = json.loads(request.data)
    if not is_valid_patient(updated_patient):
        return jsonify({'Error': 'Invalid patient'}), 400

    patient.update(updated_patient)
    return jsonify(patient)

# DELETE request
@app.route("/patients/<int:id>", methods=['DELETE'])
def delete_patient(id: int):
    patient = get_patient(id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404

    for pat in patients:
        if pat == patient:
            patients.remove(pat)
            return jsonify(patient), 200
    
if __name__ == "__main__":
    app.run(debug=True)