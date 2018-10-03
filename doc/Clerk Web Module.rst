Clerk Module
---------------------------------

.. code::

    This module is for process the clerk's API and render front end pages, 
    it contains login, add doctor, process appintment.

**The supports of Clerk module**

- Support to add a doctor
- Support to get doctor list
- Support to get doctor appointment
- Support to set doctor appointment
- Support to delete doctor appointment
- Support to get statistics of all doctors

**Render Page : views.py**

**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Route", "Render Page"
   :widths: 15, 30, 20, 15


   "clerkSetting","The method for setting menu","None","None"
   "index","The method for redirecting to specific route, default redirecting to clerk.addDoctor","/index","None"
   "addDoctor","The method for rendering and adding doctor's information","/add_doctor","clerk/add_doctor.html"
   "doctorsList","The method for getting all doctors' list","/doctors","clerk/doctors.html"
   "doctorsCalendar","The method for geting doctor's calendar","/doctors_calendar","clerk/doctors_calendar.html"
   "setFreeTime","The method for setting free time for doctor for AJAX","/set_free_time/<doctor_id>",""
   "getFreeTime","The method for get free time of doctor for AJAX","/get_free_time/<doctor_id>","JSON"
   "deleteFreeTime","The method for deleting free time of doctor for AJAX","/delete_free_time/<doctor_id>","JSON"
   "statistics","The method for getting chart for statistics of all doctors","/statistics","clerk/statistics.html"
   "staJson","The method for getting statistics data for AJAX","/statistics/json","JSON"



**Connect API : clerk_services.py**

**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameter", "Return Value"
   :widths: 15, 30, 20, 15


   "__init__","The constructor for initializing service base url","None","None"
   "getStatistics","The method for request API of statistics","None","Boolean, Object"
   "login","The method for login","payload(request payload for clerk endpoints)","Boolean, Object"
   

**Form : forms.py**

**Forms**

.. csv-table:: 
   :header: "Name", "Description", "Fields"
   :widths: 15, 30, 30

   "AddDoctorForm","Doctor's creation form","username(required), sex(required), name(required), phone(required), email(required), age(required)"
   