import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from init import db, ma, PREFIX
import hashlib

# model for doctor
class Doctor(db.Model):
    __tablename__ = '{}doctor'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    calendar_id = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    # initialise model
    def __init__(self, data):
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add a doctor
    def addDoctor(self):
        self.password = hashlib.sha224(self.password.encode('utf-8')).hexdigest()
        db.session.add(self)
        return db.session.commit()

    # login a doctor
    def login(self):
        result = self.query.filter(\
                                Doctor.username == self.username,\
                                Doctor.password == hashlib.sha224(self.password.encode('utf-8')).hexdigest()\
                            ).first()
        result = doctor_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, {}

    # get one doctor by id
    def getOneDoctorById(self, customer_id):
        result = self.query.get(customer_id)
        result = doctor_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, {}

    # update doctor by id
    def updateSchema(self, doctorId, data):
        doctor = self.query.get(doctorId)
        for field in data:
            setattr(doctor, field, data[field])
        return db.session.commit()

    # get all doctors
    def getAllDoctors(self):
        all = self.query.all()
        result = doctors_schema.dump(all)
        return result.data

class DoctorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email', 'name', 'phone', 'age', 'sex', 'password', 'calendar_id', 'created_at')

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)

# model for doctor's busy time
class DoctorBusyTime(db.Model):
    __tablename__ = '{}busytime'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, nullable=False)
    busytime_from = db.Column(db.DateTime, nullable=False)
    busytime_to = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # initialise model
    def __init__(self, data):
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # set busytime fro doctor
    def setBusy(self):
        db.session.add(self)
        return db.session.commit()

    # get all busytime of doctor
    def getAllBusyTime(self):
        all = self.query.all()
        result = doctor_busytimes_schema.dump(all)
        return result.data

    # delete busytime
    def deleteBusyTime(self, busytime_id):
        busytime = DoctorBusyTime.query.get(busytime_id)
        db.session.delete(busytime)
        db.session.commit()

class DoctorBusyTimeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'doctor_id', 'busytime_from', 'busytime_to', 'created_at')

doctor_busytime_schema = DoctorBusyTimeSchema()
doctor_busytimes_schema = DoctorBusyTimeSchema(many=True)