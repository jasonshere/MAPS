Patient Model
---------------------------------

.. code::

    This model is for process the google cloud data of patient module, 
    it contains several methods that can store, update, fetch patient data from google cloud data.

**The supports of Patient model**

- Support to save patient data into google cloud
- Support to Sign in the MAPS with a patient account
- Support to update patient information by primary key
- Support to update patient information by patient's username

**Table**

**maps_patient:**

.. csv-table:: 
   :header: "Field Name", "Description", "Type", "Default", "Unique", "Nullable"
   :widths: 15, 30, 30, 15, 15, 15

   "id", "The primary key", "Integer", "None", "Yes", "No"
   "username","patient user's name","String(80)","None","Yes","No"
   "email","patient's email address","String(120)","None","Yes","No"
   "password","patient's password","String(100)","None","No","No"
   "name","patient's true name","String(120)","None","No","Yes"
   "birthday","patient's birthday","Date","None","No","Yes"
   "phone","patient's phone number","String(20)","None","No","Yes"
   "age","patient's age","Integer","None","No","Yes"
   "sex","patient's sex","Integer","None","No","Yes"


**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameters", "Return Value"
   :widths: 15, 30, 20, 15


   "__init__","The constructor of patient model, initialise the patient data","data:(dict, patient object)","None"
   "addPatient","The method for saving patient data into google cloud","None","None"
   "login","The method for signing in the system by patient account","None","Boolean, Object"
   "getOnePatientById","The method for fetching patient object by patient id","customer_id:(integer, patient's primary key)","Boolean, Object"
   "updateSchema","The method for update patient by id","customer_id:(integer, patient's primary key), data:(Patient's data)","Boolean"
   "updateByUsername","The method for update patient by username","username:(string, patient's unique username), data:(Patient's data)","Boolean"
   "getAllPatients","The method for get all patients","None","Object"


