Patient Module
---------------------------------

.. code::

    This module is for process the patient's API and render front end pages, 
    it contains register, login, update, process appintment.

**The supports of Patient model**

- Support to register patient
- Support to update patient data
- Support to make an appointment for patient
- Support to get doctors
- Support to delete appointment
- Support to get events by doctor id
- Support to update events by doctor id
- Support to delete events
- Support to get all appointments

**Render Page : views.py**

**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Route", "Render Page"
   :widths: 15, 30, 20, 15


   "patientSetting","The method for setting menu","None","None"
   "index","The method for redirecting to specific route, default redirecting to patient.account","/index","None"
   "account","The method for rendering and updating patient's information","/accounts","patient/account.html"
   "makeAppointment","The method for rendering tha page to show appointment","/make_appointment","patient/calendar.html"
   "getDoctor","The method for geting doctor by id for AJAX","/get_doctor/<doctor_id>","JSON"
   "register","The method for rendering patient register page and registing patient","/register","patient/register.html"
   "getEventsByDoctorId","The method for get events by doctor id for AJAX","/get_events/<doctor_id>","JSON"
   "updateEventsByDoctorId","The method for updating events by doctor id for AJAX","/update_events","JSON"
   "deleteEvents","The method for deleting events for AJAX","/delete_events","JSON"
   "getAppointments","The method for getting appointments for AJAX","/get_appointments","JSON"



**Connect API : patient_services.py**

**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameter", "Return Value"
   :widths: 15, 30, 20, 15


   "__init__","The constructor for initializing service base url","None","None"
   "register","The method for adding a patient","payload(request payload for patient endpoints)","Boolean, Object"
   "login","The method for login","payload(request payload for patient endpoints)","Boolean, Object"
   "update","The method for updating patient","payload(request payload for patient endpoints)","Boolean, Object"
   "getPatientById","The method for getting patient by id","patient_id(request id for patient endpoints)","Boolean, Object"
   "getAllEvents","The method for getting events by calendar id","calendar_id(request calendar id for patient endpoints)","Boolean, Object"
   "getEventConnector","The method for getting appointments by doctor id","doctor_id(request doctor_id for patient endpoints)","Boolean, Object"
   "getEventsByDoctorId","The method for getting events by doctor id","doctor_id(request doctor id for patient endpoints)","Boolean, Object"
   "updateEventsByDoctorId","The method for updating events status","doctor_id(doctor's id), event_id(google event's id), email(patient's email), delete(is delete from appointment)","Boolean, Object"
   "setAppointment","The method for setting appointment","doctor_id(doctor's id), event_id(google event's id), patient_id(patient's id), start(appointment start time), end(appointment end time)","Boolean, Object"
   "deleteAppointment","The method for delete appointment by event id","event_id(google event id)","Boolean, Object"
   "getAppointmentsById","The method for getting appointment by patient id","patient_id(patient's id)","Boolean, Object"
   

**Form : forms.py**

**Forms**

.. csv-table:: 
   :header: "Name", "Description", "Fields"
   :widths: 15, 30, 30


   "RegForm","Patient Register Form","username(required, lenght(4~25)), email(required, email), password(required, equalto confirm), confirm"
   "LoginForm","Patient Login Form","username(required), password(required), role(required)"
   "UpdateForm","Patient update information form","username(required), sex(required), name(required), birthday(required), phone(required), email(required), age(required)"
   