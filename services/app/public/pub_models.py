import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from init import db, ma, PREFIX

# model for appointment
class Appointment(db.Model):
    __tablename__ = '{}appointment'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    appointed_from = db.Column(db.DateTime, nullable=False)
    appointed_to = db.Column(db.DateTime, nullable=False)
    google_event_id = db.Column(db.String(100), nullable=False)
    google_calendar_id = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # initialise model
    def __init__(self, data):
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add an appointment
    def addAppointment(self):
        db.session.add(self)
        db.session.commit()

    # get all appointments by patient id
    def getAllAppointmentByPatientId(self, patient_id):
        results = self.query.filter(\
            Appointment.patient_id == patient_id
        ).all()
        results = appointments_schema.dump(results)
        if results.data :
            return True, results.data
        else:
            return False, []

    # get all appointments by patient id
    def getAllAppointmentByPatientId(self, patient_id):
        results = self.query.filter(\
            Appointment.patient_id == patient_id
        ).all()
        results = appointments_schema.dump(results)
        if results.data :
            return True, results.data
        else:
            return False, []

    # get all appointments by doctor id
    def getAllAppointmentByDoctorId(self, doctor_id):
        results = self.query.filter(\
            Appointment.doctor_id == doctor_id
        ).all()
        results = appointments_schema.dump(results)
        if results.data :
            return True, results.data
        else:
            return False, Exception('error')
    
    # delete an appointment
    def deleteAppointmentById(self, id):
        appoint = Appointment.query.get(id)
        db.session.delete(appoint)
        db.session.commit()

class AppointmentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'patient_id', 'doctor_id', 'appointed_from', 'appointed_to', 'created_at', 'google_event_id', 'google_calendar_id')

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)