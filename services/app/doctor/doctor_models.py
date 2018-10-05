import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from init import db, ma, PREFIX
import hashlib

# model for doctor
class Doctor(db.Model):
    """
    Doctor Model
    """
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
    created_at = db.Column(db.DateTime, nullable=True)

    # initialise model
    def __init__(self, data):
        """
        constructor
        :param data: init data
        """
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add a doctor
    def addDoctor(self):
        """
        add a doctor
        :return: Boolean
        """
        self.password = hashlib.sha224(self.password.encode('utf-8')).hexdigest()
        db.session.add(self)
        return db.session.commit()

    # login a doctor
    def login(self):
        """
        sign in as a doctor
        :return: Boolean, Object
        """
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
        """
        Get one doctor by id
        :param customer_id: doctor id
        :return: Boolean, Object
        """
        result = self.query.get(customer_id)
        result = doctor_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, {}

    # get one doctor by email
    def getOneDoctorByEmail(self, customer_email):
        """
        get one doctor by email
        :param customer_email: email
        :return: Boolean, Object
        """
        result = self.query.filter(\
                    Doctor.email == customer_email
                ).first()
        result = doctor_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, {}

    # update doctor by id
    def updateSchema(self, doctorId, data):
        """
        update fields for doctor
        :param doctorId: doctor id
        :param data: data
        :return: Boolean
        """
        doctor = self.query.get(doctorId)
        for field in data:
            setattr(doctor, field, data[field])
        return db.session.commit()

    # get all doctors
    def getAllDoctors(self):
        """
        Get all doctors
        :return: object
        """
        all = self.query.all()
        result = doctors_schema.dump(all)
        return result.data

class DoctorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email', 'name', 'phone', 'age', 'sex', 'password', 'calendar_id', 'created_at')

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)
