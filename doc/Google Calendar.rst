Google calendar
---------------------------------

.. code::

    This model is for process the google calendar data, 
    it contains several methods that can store, update, fetch and delete event and calendar.

**The supports of Appointment model**

- Support to add one google secondary calendar
- Support to add google calendar event
- Support to get google events by calendar id
- Support to update google calendar events
- Support to delete google calendar event


**Methods**

.. csv-table:: 
   :header: "Name", "Description", "Parameters", "Return Value"
   :widths: 15, 30, 20, 15


   "addSecondaryCalendar","The method for add one secondary calendar","summary(String), description(String), location(String), timezone(String)","Boolean, Object"
   "setFreeTimeGoogleEvent","The method for set Freetime event","Object","Boolean, Object"
   "addGoogleEvent","The method for add event","Object","Boolean, Object"
   "getGoogleEvents","The method for getting all events","calendar_id(String)","Boolean, Object"
   "updateGoogleEvents","The method for update events","calendar_id(String), event_id(String), payload(Object)","Boolean, Object"
   "deleteGoogleEvent","The method for delete google event","calendar_id(String), event_id(String)","Boolean, Object"
   