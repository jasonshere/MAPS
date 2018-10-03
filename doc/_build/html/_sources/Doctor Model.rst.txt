Doctor Model
---------------------------------

.. code::

    This model is for process the google cloud data of doctor module, 
    it contains several methods that can store, update, fetch doctor data from google cloud data.

**The supports of Doctor model**

- Support to save doctor data into google cloud
- Support to Sign in the MAPS with a doctor account
- Support to get one doctor by primary key
- Support to get doctor by email
- Support to update doctor information by primary key
- Support to get all doctors

**Table**

**maps_doctor:**

.. csv-table:: 
   :header: "Field Name", "Description", "Type", "Default", "Unique", "Nullable"
   :widths: 15, 30, 30, 15, 15, 15

   "id", "The primary key", "Integer", "None", "Yes", "No"
   "username","doctor user's name","String(80)","None","Yes","No"
   "email","doctor's email address","String(120)","None","Yes","No"
   "password","doctor's password","String(100)","None","No","No"
   "name","doctor's true name","String(120)","None","No","Yes"
   "phone","doctor's phone number","String(20)","None","No","Yes"
   "age","doctor's age","Integer","None","No","Yes"
   "sex","doctor's sex","Integer","None","No","Yes"
   "calendar_id","google calendar's id","String(100)","None","No","Yes"


**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameters", "Return Value"
   :widths: 15, 30, 20, 15


   "__init__","The constructor of doctor model, initialise the doctor data","data:(dict, doctor object)","None"
   "addDoctor","The method for saving doctor data into google cloud","None","None"
   "login","The method for signing in the system by doctor account","None","Boolean, Object"
   "getOneDoctorById","The method for fetching doctor object by doctor id","customer_id:(integer, doctor's primary key)","Boolean, Object"
   "getOneDoctorByEmail","The method for fetching doctor object by doctor email","customer_email:(string, doctor's email)","Boolean, Object"
   "updateSchema","The method for update doctor by id","customer_id:(integer, doctor's primary key), data:(doctor's data)","Boolean"
   "getAllDoctors","The method for get all doctors","None","Object"


