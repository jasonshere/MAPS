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
    appointed_from = db.Column(db.String(100), nullable=False)
    appointed_to = db.Column(db.String(100), nullable=False)
    google_event_id = db.Column(db.String(100), nullable=False)
    google_calendar_id = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    diagnoses = db.Column(db.String(500), nullable=True)
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
    def getAllAppointmentByPatientId(self, patient_id, ds):
        results = self.query.filter(\
            Appointment.patient_id == patient_id
        ).all()
        results = appointments_schema.dump(results)
        if results.data :
            for i in range(len(results.data)):
                res, d = ds.getOneDoctorById(results.data[i]['doctor_id'])
                results.data[i]['doctor'] = d
            return True, results.data
        else:
            return False, []

    def getAllAppointmentByDoctorId(self, doctor_id, ps):
        results = self.query.filter(\
            Appointment.doctor_id == doctor_id
        ).all()
        results = appointments_schema.dump(results)
        if results.data :
            for i in range(len(results.data)):
                res, d = ps.getOnePatientById(results.data[i]['patient_id'])
                results.data[i]['patient'] = d
            return True, results.data
        else:
            return False, Exception('error')
    
    # delete an appointment
    def deleteAppointment(self, event_id):
        appoint = Appointment.query.filter(\
            Appointment.google_event_id == event_id
        ).first()
        db.session.delete(appoint)
        db.session.commit()

    # get one appointment
    def getAppointmentById(self, app_id):
        result = self.query.filter(Appointment.id == app_id).first()
        result = appointment_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, []

    # update appointment
    def update(self, appointment_id, data):
        app = self.query.get(appointment_id)
        for field in data:
            setattr(app, field, data[field])
        db.session.commit()

class AppointmentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'patient_id', 'doctor_id', 'appointed_from', 'appointed_to', 'created_at', 'google_event_id', 'google_calendar_id', 'notes', 'diagnoses')

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)