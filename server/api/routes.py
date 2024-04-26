from flask import Flask, Blueprint, jsonify, request, Response
import json
from . import db
from .models import Patient

app = Blueprint('routes', __name__)

# GET request all patients
@app.route("/patients", methods=['GET'])
def get_all_patients():
    patients = []
    for patient in Patient.query.all():
        patients.append(json.dumps(patient.to_dict(), indent=4, sort_keys=False))
    patients = '\n'.join(patients)
    return Response(patients, mimetype='application/json')

# GET request single patient
@app.route("/patients/<int:id>", methods=['GET'])
def get_patient_by_id(id: int):
    patient = db.get_or_404(Patient, id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404
    patient = json.dumps(patient.to_dict(), indent=4, sort_keys=False)
    return Response(patient, mimetype='application/json')

def is_valid_patient(patient):
    properties = ['id', 'pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree_function', 'age']
    for key in patient.keys():
        if key not in properties:
            return False
    return True

# POST request 
@app.route("/patients", methods=['POST'])
def create_patient():
    created_patient = json.loads(request.data)
    print(created_patient)
    if not is_valid_patient(created_patient):
        return jsonify({'Error': 'Invalid patient'}), 400

    new_patient = Patient(
        pregnancies=created_patient['pregnancies'],
        glucose=created_patient['glucose'],
        blood_pressure=created_patient['blood_pressure'],
        skin_thickness=created_patient['skin_thickness'],
        insulin=created_patient['insulin'],
        bmi=created_patient['bmi'],
        diabetes_pedigree_function=created_patient['diabetes_pedigree_function'],
        age=created_patient['age']
    )

    db.session.add(new_patient)
    db.session.commit()
    created_patient = json.dumps(created_patient, indent=4, sort_keys=False)
    return Response(created_patient, mimetype='application/json')

# PUT request
@app.route("/patients/<int:id>", methods=['PUT'])
def update_patient(id: int):
    patient = db.get_or_404(Patient, id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404
    
    updated_patient = json.loads(request.data)
    if not is_valid_patient(updated_patient):
        return jsonify({'Error': 'Invalid patient'}), 400
    
    pregnancies = updated_patient['pregnancies']
    glucose = updated_patient['glucose']
    blood_pressure = updated_patient['blood_pressure']
    skin_thickness = updated_patient['skin_thickness']
    insulin = updated_patient['insulin']
    bmi = updated_patient['bmi']
    diabetes_pedigree_function = updated_patient['diabetes_pedigree_function']
    age = updated_patient['age']

    patient.pregnancies = pregnancies
    patient.glucose = glucose
    patient.blood_pressure = blood_pressure
    patient.skin_thickness = skin_thickness
    patient.insulin = insulin
    patient.bmi = bmi
    patient.diabetes_pedigree_function = diabetes_pedigree_function
    patient.age = age

    db.session.commit()
    updated_patient = json.dumps(updated_patient, indent=4, sort_keys=False)
    return Response(updated_patient, mimetype='application/json')

# DELETE request
@app.route("/patients/<int:id>", methods=['DELETE'])
def delete_patient(id: int):
    patient = db.get_or_404(Patient, id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404

    db.session.delete(patient)
    db.session.commit()
    patient = json.dumps(patient.to_dict(), indent=4, sort_keys=False)
    return Response(patient, mimetype='application/json')