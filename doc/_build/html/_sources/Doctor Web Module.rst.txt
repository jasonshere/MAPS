Doctor Module
---------------------------------

.. code::

    This module is for process the doctor's API and render front end pages, 
    it contains login, and process appintment and google calendar.

**The supports of Doctor model**

- Support to get scheduled patients
- Support to add notes for patient during appointment
- Support to add diagnoses for patient during appointment
- Support to pull up patient's history
- Support to set google calendar
- Support to set free time
- Support to get free time
- Support to delete free time

**Render Page : views.py**

**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Route", "Render Page"
   :widths: 15, 30, 20, 15


   "doctorSetting","The method for setting menu","None","None"
   "index","The method for redirecting to specific route, default redirecting to doctor.setCalendar","/index","None"
   "patients","The method for rendering all patients","/all_patients","doctor/patients.html"
   "editNotes","The method for editing notes for patient","/edit_notes/<appointment_id>","doctor/edit_notes.html"
   "editDiagnoses","The method for editing diagnoses for patient","/edit_diagnoses/<appointment_id>","doctor/edit_diagnoses.html"
   "history","The method for geting patient history","/history/<patient_id>","doctor/history.html"
   "setCalendar","The method for set google calendar","/set_calendar","doctor/set_calendar.html"
   "setFreeTime","The method for setting free time for AJAX","/set_free_time","JSON"
   "getFreeTime","The method for getting free time for AJAX","/get_free_time","JSON"
   "deleteFreeTime","The method for deleting free time for AJAX","/delete_free_time","JSON"



**Connect API : doctor_services.py**

**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameter", "Return Value"
   :widths: 15, 30, 20, 15


   "__init__","The constructor for initializing service base url","None","None"
   "register","The method for adding a doctor","payload(request payload for doctor endpoints)","Boolean, Object"
   "login","The method for login","payload(request payload for login endpoints)","Boolean, Object"
   "getAll","The method for request API of get all doctors","None","Boolean, Object"
   "setFreeTime","The method for request API to set datetime that is available","payload(request payload for doctor set free time endpoints)","Boolean, Object"
   "getFreeTime","The method for request API to get all events","google calendar id(string)","Boolean, Object"
   "deleteFreeTime","The method for request API to delete freetime","google calendar id(string), google event id(string)","Boolean, Object"
   "getDoctorById","The method for request API to get doctor by id","doctor id(integer)","Boolean, Object"
   "getDoctorByEmail","The method for request API to get doctor by email","doctor email(string)","Boolean, Object"
   "getAllPatients","The method for request API to get patients","doctor id(integer)","Boolean, Object"
   "editNotes","The method for request API for edit notes","appointment id(integer), notes data(string)","Boolean, Object"
   "editDiags","The method for request API for edit notes","appointment id(integer), diagnoses data(string)","Boolean, Object"
   "getAppointmentById","The method for request API to get appointments by id","appointment id(integer)","Boolean, Object"
   "getAppointmentsByPatientId","The method for request API to get appointments by patient id","patient_id(integer)","Boolean, Object"
   

**Form : forms.py**

**Forms**

.. csv-table:: 
   :header: "Name", "Description", "Fields"
   :widths: 15, 30, 30


   "NoteForm","Patient Note Form","Description(required)"
   "DiagnoseForm","Patient Diagnose Form","Description(required)"
   