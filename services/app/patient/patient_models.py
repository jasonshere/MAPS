import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from init import db, ma, PREFIX
import hashlib

# model for patient
class Patient(db.Model):
    __tablename__ = '{}patient'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(120), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.Integer, nullable=True)
    calendar_id = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)

    # initialise model
    def __init__(self, data):
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add a patient
    def addPatient(self):
        self.password = hashlib.sha224(self.password.encode('utf-8')).hexdigest()
        db.session.add(self)
        return db.session.commit()

    # login a patient
    def login(self):
        result = self.query.filter(\
                                Patient.username == self.username,\
                                Patient.password == hashlib.sha224(self.password.encode('utf-8')).hexdigest()\
                            ).first()
        result = patient_schema.dump(result)
        print(result)
        if result.data :
            return True, result.data
        else:
            return False, {}

    # get one patient by id
    def getOnePatientById(self, customer_id):
        result = self.query.get(customer_id)
        result = patient_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, {}

    # update patient by id
    def updateSchema(self, patientId, data):
        patient = self.query.get(patientId)
        for field in data:
            setattr(patient, field, data[field])
        return db.session.commit()

    # update patient by username
    def updateByUsername(self, username, data):
        patient = self.query.filter(Patient.username == username).first()
        for field in data:
            setattr(patient, field, data[field])
        return db.session.commit()

    # get all patients
    def getAllPatients(self):
        all = self.query.all()
        result = patients_schema.dump(all)
        return result.data

class PatientSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email', 'name', 'birthday', 'phone', 'age', 'sex', 'password', 'calendar_id')

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
