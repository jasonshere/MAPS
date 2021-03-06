import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from init import db, ma, PREFIX
import time

# model for appointment
class Appointment(db.Model):
    """
    Appointment Model
    """
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
    def __init__(self, data={}):
        """
        constructor
        :param data: init data
        """
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add an appointment
    def addAppointment(self):
        """
        add appointment
        :return: None
        """
        db.session.add(self)
        db.session.commit()

    # get all appointments by patient id
    def getAllAppointmentByPatientId(self, patient_id, ds):
        """
        get all appointments by patient id
        :param patient_id: patient id
        :param ds: doctor service
        :return: boolean,object
        """
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

    # get all appointments by doctor id
    def getAllAppointmentByDoctorId(self, doctor_id, ps):
        """
        get all appointments by doctor id
        :param doctor_id: doctor id
        :param ps: patient service
        :return:boolean,object
        """
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

    # get next patient by doctor id
    def getNextPatientByDoctorId(self, doctor_id, ps):
        """
        get next patient by doctor id
        :param doctor_id: doctor id
        :param ps: patient service
        :return: boolean,object
        """
        results = self.query.filter(\
            Appointment.doctor_id == doctor_id,
            db.func.unix_timestamp(Appointment.appointed_from) >= time.time()
        ).first()
        results = appointment_schema.dump(results)
        if results.data :
            res, d = ps.getOnePatientById(results.data['patient_id'])
            results.data['patient'] = d
            return True, results.data
        else:
            return False, Exception('error')
 
    # delete an appointment
    def deleteAppointment(self, event_id):
        """
        delete appointments
        :param event_id: event id
        :return: None
        """
        appoint = Appointment.query.filter(\
            Appointment.google_event_id == event_id
        ).first()
        if appoint.notes or appoint.diagnoses:
            return False
        db.session.delete(appoint)
        db.session.commit()

    # get one appointment
    def getAppointmentById(self, app_id):
        """
        get appointment by id
        :param app_id: appointment id
        :return: boolean,object
        """
        result = self.query.filter(Appointment.id == app_id).first()
        result = appointment_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, []

    # get doctor id by event id
    def getDoctorIdByEventId(self, eid):
        """
        get doctor id by event id
        :param eid: event id
        :return: boolean,object
        """
        result = self.query.filter(Appointment.google_event_id == eid).first()
        result = appointment_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, []

    # update appointment
    def update(self, appointment_id, data):
        """
        update appointment by appointment id and data
        :param appointment_id: appointment id
        :param data: data
        :return: None
        """
        app = self.query.get(appointment_id)
        for field in data:
            setattr(app, field, data[field])
        db.session.commit()

    # get appointments by doctor and start date
    def getAppointmentsGroupByDoctorAndStartDate(self):
        """
        get statistics
        :return: Object
        """
        # get All appointments
        
        appointments = self.query.filter(
            db.func.unix_timestamp(Appointment.appointed_from) >= time.time(), \
            db.func.unix_timestamp(Appointment.appointed_from) <= time.time() + 24*3600*7 \
        ).all()
        results = appointments_schema.dump(appointments)
        ids = self.getAllDoctorIds(results[0])
        # get futural 7 days
        data = []
        for j in range(7):
            # date = time.strftime('%Y-%m-%d',time.localtime(time.time() + i * 24 * 3600))
            dateStart = time.time() + j * 24 * 3600
            dateEnd = time.time() + (j + 1) * 24 * 3600
            apps = []
            for i in range(len(results[0])):
                t = time.mktime(time.strptime(results[0][i]['appointed_from'],'%Y-%m-%dT%H:%M:%S'))
                if t >= dateStart and t <= dateEnd:
                    b = self.hasDoctorId(apps, results[0][i]['doctor_id'])
                    if b is False:
                        b = {
                            'doctor_id': results[0][i]['doctor_id'],
                            'count': 1
                        }
                        apps.append(b)
                    else:
                        b['count'] += 1
            
            for n in range(len(ids)):
                bo = self.hasDoctorId(apps, ids[n])
                if bo is False:
                    apps.append({
                        'doctor_id': ids[n],
                        'count': 0
                    })
            d = {
                'date': time.strftime('%Y-%m-%d',time.localtime(time.time() + (j + 1) * 24 * 3600)),
                'appointments': apps
            }
            data.append(d)
        return data

    # get all doctor_id
    def getAllDoctorIds(self, results):
        """
        get all doctors
        :param results: id
        :return: boolean/object
        """
        ids = []
        for i in range(len(results)):
            if results[i]['doctor_id'] not in ids:
                ids.append(results[i]['doctor_id'])
        return ids

    # identify the doctor_id is exists
    def hasDoctorId(self, apps, doctorId):
        """
        identify if the doctor id is existing
        :param apps: appointments
        :param doctorId: doctor id
        :return: boolean/ids
        """
        for i in range(len(apps)):
            if apps[i]['doctor_id'] == doctorId:
                return apps[i]
        return False
        

class AppointmentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'patient_id', 'doctor_id', 'appointed_from', 'appointed_to', 'created_at', 'google_event_id', 'google_calendar_id', 'notes', 'diagnoses')

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)
