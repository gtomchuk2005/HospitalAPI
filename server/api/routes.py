from flask import Flask, Blueprint, jsonify, request
import json
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from . import db
from .models import Patient

app = Blueprint('routes', __name__)

# create authorized user which generates JWT token
@app.route("/login", methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "admin":
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# GET request all patients
@app.route("/patients", methods=['GET'])
@jwt_required()
def get_all_patients():
    patients = []
    for patient in Patient.query.all():
        patient = patient.to_dict()
        patients.append(patient)
    return jsonify(patients)

# GET request single patient
@app.route("/patients/<int:id>", methods=['GET'])
@jwt_required()
def get_patient_by_id(id: int):
    patient = db.get_or_404(Patient, id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404
    return jsonify(patient.to_dict())

def is_valid_patient(patient):
    properties = ['id', 'pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree_function', 'age']
    for key in patient.keys():
        if key not in properties:
            return False
    return True

# POST request 
@app.route("/patients", methods=['POST'])
@jwt_required()
def create_patient():
    created_patient = json.loads(request.data)
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
    return jsonify(new_patient.to_dict())

# PUT request
@app.route("/patients/<int:id>", methods=['PUT'])
@jwt_required()
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
    return jsonify(patient.to_dict())

# DELETE request
@app.route("/patients/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_patient(id: int):
    patient = db.get_or_404(Patient, id)
    if patient is None:
        return jsonify({'Error': 'Patient does not exist'}), 404

    db.session.delete(patient)
    db.session.commit()
    return jsonify(patient.to_dict())