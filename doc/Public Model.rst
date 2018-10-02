Public Model
---------------------------------

.. code::

    This model is for process the google cloud data of appointment, 
    it contains several methods that can store, update, fetch and delete appointment data from google cloud data.

**The supports of Appointment model**

- Support to save appointment data into google cloud
- Support to get appointments by patient id
- Support to get appointments by doctor id
- Support to delete appointment by event id
- Support to delete appointment by appointment id
- Support to get doctor id by event id
- Support to update appointment
- Support to get appointments group by doctor and start date

**Table**

**maps_doctor:**

.. csv-table:: 
   :header: "Field Name", "Description", "Type", "Default", "Unique", "Nullable"
   :widths: 15, 30, 30, 15, 15, 15

   "id", "The primary key", "Integer", "None", "Yes", "No"
   "patient_id","patient's primary id","Integer","None","Yes","No"
   "doctor_id","doctor's primary id","Integer","None","Yes","No"
   "appointed_from","appointment start datetime","String(100)","None","No","No"
   "appointed_to","appointment end datetime","String(100)","None","No","No"
   "google_event_id","Google's event id","String(100)","None","No","Yes"
   "notes","appointment's notes","String(500)","None","No","Yes"
   "diagnoses","appointment's diagnoses","String(500)","None","No","Yes"


**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameters", "Return Value"
   :widths: 15, 30, 20, 15


   "__init__","The constructor of appoinement model, initialise the appointment data","data:(dict, appointment object)","None"
   "addAppointment","The method for saving appointment data into google cloud","None","None"
   "getAllAppointmentByPatientId","The method for getting all appointments by patient id and doctor model","patient_id(integer), doctor's model(Object)","Boolean, Object"
   "getAllAppointmentByDoctorId","The method for getting all appointments by doctor id and patient model","doctor_id(integer), patient's model(Object)","Boolean, Object"
   "deleteAppointment","The method for delete an appointment","event_id(string, google event id)","Boolean"
   "getAppointmentById","The method for get one appointment by appointment id","app_id(integer, appointment primary key)","Boolean, Object"
   "getDoctorIdByEventId","The method for get one appointment by event id","event_id(string, google event id)","Boolean, Object"
   "update","The method for update appointment","app_id(integer, appointment primary key), data(Object)","None"
   "getAppointmentsGroupByDoctorAndStartDate","The method for get appointments by doctor and start date","None","None"