from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///database.db"
db = SQLAlchemy(app)

class healthmodel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = True)
    pregnancies = db.Column(db.Integer, nullable = True)
    glucose = db.Column(db.Float, nullable = True)
    BP = db.Column(db.Float, nullable = True)
    ST = db.Column(db.Float, nullable = True)
    insulin = db.Column(db.Integer, nullable = True)
    BMI = db.Column(db.Float, nullable = True)
    DPF = db.Column(db.Float, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    

    def __repr__(self):
        return f"Health status of {self.name}, Number of Pregnancies = {self.pregnancies}, Glucose concentration = {self.glucose}, Blood pressure = {self.BP}, SkinThickness = {self.ST}, Insulin level = {self.insulin}, Body Mass index = {self.BMI}, Diabeties Pedigree Function = {self.DPF}, Age = {self.age}"


health_put_args = reqparse.RequestParser()
health_put_args.add_argument('name', type=str, help = "name is required", required = True)
health_put_args.add_argument('pregnancies', type=int, help = "Number of pregnancies is required", required = True)
health_put_args.add_argument('glucose', type=float, help = "Glucose concentration is required", required = True)
health_put_args.add_argument('BP', type=float, help = "Blood pressure is required", required = True)
health_put_args.add_argument('ST', type=float, help = "SkinThickness is required", required = True)
health_put_args.add_argument('insulin', type=int, help = "Insulin level is required", required = True)
health_put_args.add_argument('BMI', type=float, help = "Body mass index is required", required = True)
health_put_args.add_argument('DPF', type=float, help = "DiabetiesPedigreeFunction is required", required = True)
health_put_args.add_argument('age', type=int, help = "Age is required", required = True)

health_patch_args = reqparse.RequestParser()
health_patch_args.add_argument('name', type=str, required = False)
health_patch_args.add_argument('pregnancies', type=int,required = False)
health_patch_args.add_argument('glucose', type=float,required = False)
health_patch_args.add_argument('BP', type=float, required = False)
health_patch_args.add_argument('ST', type=float, required = False)
health_patch_args.add_argument('insulin', type=int, required = False)
health_patch_args.add_argument('BMI', type=float, required = False)
health_patch_args.add_argument('DPF', type=float, required = False)
health_patch_args.add_argument('age', type=int, required = False)

resource_fields = {
'id': fields.Integer,
'name': fields.String,
'pregnancies': fields.Integer,
'glucose': fields.Float, 
'BP': fields.Float,
'ST': fields.Float, 
'insulin': fields.Integer,
'BMI': fields.Float,
'DPF': fields.Float,
'age': fields.Integer, 
}

class user(Resource):
    #Get request method for information already stored in the database
    @marshal_with(resource_fields)
    def get(self, user_id):
        retrieved = healthmodel.query.filter_by(id = user_id).first()
        if not retrieved: 
            abort(404, message = "ID does not contain a user")
        return retrieved
    

    #Put request method to store new information based on JSON user input
    @marshal_with(resource_fields)
    def put(self, user_id):
        args = health_put_args.parse_args()
        retrieved = healthmodel.query.filter_by(id = user_id).first()
        if retrieved:
            abort(409, message = "User information with this ID already exists")

        healthinfo = healthmodel(id=user_id, name = args['name'], pregnancies = args['pregnancies'],glucose = args['glucose'], BP = args['BP'], ST = args['ST'], insulin = args['insulin'], BMI = args['BMI'], DPF = args['DPF'], age = args['age'] )
        db.session.add(healthinfo)
        db.session.commit()
        return healthinfo
    
    #Delete request to delete already existing data entries 
    @marshal_with(resource_fields)
    def delete(self, user_id):
        retrieved = healthmodel.query.filter_by(id = user_id).first()
        if not retrieved: 
            abort(404, message="ID does not contain a user ")
        db.session.delete(retrieved)
        db.session.commit()
    
    #Update request that allows users to update values of existing data entries
    @marshal_with(resource_fields)
    def patch(self, user_id):
        args = health_patch_args.parse_args()
        retrieved = healthmodel.query.filter_by(id=user_id).first()
        if not retrieved: 
            abort(404, message= "ID not found ")
        if args['name']:
            retrieved.name = args['name']
        if args['pregnancies']:
            retrieved.pregnancies = args['pregnancies']
        if args['glucose']:
            retrieved.glucose = args['glucose']
        if args['BP']:
            retrieved.BP = args['BP']
        if args['ST']:
            retrieved.ST = args['ST']
        if args['insulin']:
            retrieved.insulin = args['insulin']
        if args['BMI']:
            retrieved.BMI = args['BMI']
        if args['DPF']:
            retrieved.DPF = args['DPF']
        if args['age']:
            retrieved.age = args['age']
        
        db.session.commit()

        return retrieved 

    
api.add_resource(user, "/user/<int:user_id>")
        
if __name__ == "__main__":
    app.run(debug=True)

        



