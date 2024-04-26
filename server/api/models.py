from . import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregnancies = db.Column(db.Integer, nullable=True)
    glucose = db.Column(db.Float, nullable=True)
    blood_pressure = db.Column(db.Float, nullable=True)
    skin_thickness = db.Column(db.Float, nullable=True)
    insulin = db.Column(db.Integer, nullable=True)
    bmi = db.Column(db.Float, nullable=True)
    diabetes_pedigree_function = db.Column(db.Float, nullable=True)
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Health status of patient of ID:{self.id}, Number of Pregnancies = {self.pregnancies}, Glucose Concentration = {self.glucose}, Blood Pressure = {self.blood_pressure}, Skin Thickness = {self.skin_thickness}, Insulin level = {self.insulin}, Body Mass index = {self.bmi}, Diabeties Pedigree Function = {self.diabetes_pedigree_function}, Age = {self.age}"
    
    def to_dict(self):
        data = {}

        data['id'] = self.id
        data['pregnancies'] = self.pregnancies
        data['glucose'] = self.glucose
        data['blood_pressure'] = self.blood_pressure
        data['skin_thickness'] = self.skin_thickness
        data['insulin'] = self.insulin
        data['bmi'] = self.bmi
        data['diabetes_pedigree_function'] = self.diabetes_pedigree_function
        data['age'] = self.age

        return data