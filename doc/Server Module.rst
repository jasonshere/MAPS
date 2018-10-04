Clerk Model
---------------------------------

.. code::

    This model is for process the google cloud data of clerk module, 
    it contains several methods that can store, fetch clerk data from google cloud data.

**The supports of Clerk model**

- Support to save clerk data into google cloud
- Support to Sign in the MAPS with a clerk account

**Table**

**maps_clerk:**

.. csv-table:: 
   :header: "Field Name", "Description", "Type", "Default", "Unique", "Nullable"
   :widths: 15, 30, 30, 15, 15, 15

   "id", "The primary key", "Integer", "None", "Yes", "No"
   "username","clerk user's name","String(80)","None","Yes","No"
   "email","clerk's email address","String(120)","None","Yes","No"
   "password","clerk's password","String(100)","None","No","No"
   "name","clerk's true name","String(120)","None","No","Yes"
   "phone","clerk's phone number","String(20)","None","No","Yes"
   "age","clerk's age","Integer","None","No","Yes"
   "sex","clerk's sex","Integer","None","No","Yes"


**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameters", "Return Value"
   :widths: 15, 30, 20, 15


   "__init__","The constructor of clerk model, initialise the clerk data","data:(dict, clerk object)","None"
   "addClerk","The method for saving clerk data into google cloud","None","None"
   "login","The method for signing in the system by clerk account","None","Boolean, Object"




