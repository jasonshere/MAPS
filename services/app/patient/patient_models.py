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

# model for history
class PatientHistory(db.Model):
    __tablename__ = '{}patient_history'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # initialise the model
    def __init__(self, data):
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add a history
    def addHistory(self):
        db.session.add(self)
        db.session.commit()

    # get all history
    def getAllHistory(self):
        all = self.query.all()
        result = patient_histories_schema.dump(all)
        return result.data

    # get all histories by patient id
    def getAllHistoryByPatientId(self, patient_id):
        results = self.query.filter(\
            PatientHistory.patient_id == patient_id
        ).all()
        results = patient_histories_schema.dump(results)
        if results.data :
            return True, results.data
        else:
            return False, []

class PatientHistorySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'patient_id', 'doctor_id', 'description', 'created_at')

patient_history_schema = PatientHistorySchema()
patient_histories_schema = PatientHistorySchema(many=True)

# model for notes
class Notes(db.Model):
    __tablename__ = '{}note'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    history_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # initialise the model
    def __init__(self, data):
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add a note
    def addNote(self):
        db.session.add(self)
        db.session.commit()

    # get all notes by patient id
    def getAllNotesByPatientId(self, patient_id):
        results = self.query.filter(\
            Notes.patient_id == patient_id
        ).all()
        results = notes_schema.dump(results)
        if results.data :
            return True, results.data
        else:
            return False, []

class NotesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'patient_id', 'doctor_id', 'history_id', 'description', 'created_at')

note_schema = NotesSchema()
notes_schema = NotesSchema(many=True)

# model for diagnoses
class Diagnoses(db.Model):
    __tablename__ = '{}diagnose'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    history_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # initialise the model
    def __init__(self, data):
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add a diagnose
    def addDiagnose(self):
        db.session.add(self)
        db.session.commit()

    # get all diagnoses by patient id
    def getAllDiagnosesByPatientId(self, patient_id):
        results = self.query.filter(\
            Diagnoses.patient_id == patient_id
        ).all()
        results = diags_schema.dump(results)
        if results.data :
            return True, results.data
        else:
            return False, []

class DiagnosesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'patient_id', 'doctor_id', 'history_id', 'description', 'created_at')

diag_schema = DiagnosesSchema()
diags_schema = DiagnosesSchema(many=True)