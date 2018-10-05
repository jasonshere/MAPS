# MAPS(Medical APpointment System)

------

This system is for doctor, patient and clerk to manage medical appointment online，this system contains 3 parts, which are web interface, API endpoints and voice assistant：

> * web
> * services
> * maps_assis

### [Details]

> **For patients**: The system keep track of the patient list and allow new patients to register on the website. After registering, a patient is allowed to book an appointment with any available doctor. Each patient will have a list of medical records.

> **For doctors**: The system allows the doctor to specify their availability on a weekly basis on their personal calendar. And also save these appointments separately.

> **For medical clerks**: The system can show a list of doctors' appointments that had already been made for that week. The medical clerk may add or remove any appointments.

------

## Usage

You can sign in the system as a doctor, patient or clerk

### 1. The feature for doctor role

- [x] Sign in system
- [x] Set and delete the available weekly appointment
- [x] Pull up the medical record for the patient
- [x] Make notes for patient during appointment
- [x] Make diagnoses for patient during appointment

### 2. The feature for patient role

- [x] Sign in system
- [x] Register a new account online
- [x] Edit the patient own account information
- [x] Check the doctor's available appointments
- [x] Check the patient own appointments
- [x] Make an appointment on doctor's available time
- [x] Cancel the appointment

### 3. The feature for clerk role

- [x] Sign in system
- [x] Register a new doctor account online
- [x] Set a new appointment for doctor
- [x] Cancel an appointment for doctor
- [x] Statistics for all appointments of all doctors


### 4. Config the system

For web interface
```python
@config.ini
[MAIN]
; dev / pro
ENVIRONMENT = dev

[DEVELOPMENT]
PROTOCOL = http
SERVICE_ADDRESS = localhost:8081/api/v1.0
; API auth
APIKEY = Jason
APIPASS = secret
; debug
DEBUG = true
; timeZone
TIMEZONE = Australia/Melbourne
;port
PORT = 8080

[PRODUCTION]
PROTOCOL = http
SERVICE_ADDRESS = localhost:8081/api/v1.0
; API auth
APIKEY = Jason
APIPASS = secret
; debug
DEBUG = true
; timeZone
TIMEZONE = Australia/Melbourne
; PORT
PORT = 8080
```
For Services
```python
@config.ini
[MAIN]
; dev / pro
ENVIRONMENT = pro

[DEVELOPMENT]
; local
USER   = root
PASS   = root123123
HOST   = 127.0.0.1
DBNAME = maps
PREFIX = maps_
; API auth
APIKEY = Jason
APIPASS = secret
; debug
DEBUG = true
; session
SESSION_TYPE = filesystem
; timeZone
TIMEZONE = Australia/Melbourne

[PRODUCTION]
; GCP
USER   = root
PASS   = oTY8dQGPEdflBbPQ
HOST   = 35.189.59.241
DBNAME = maps
PREFIX = maps_
; API auth
APIKEY = Jason
APIPASS = secret
; debug
DEBUG = false
; session
SESSION_TYPE = filesystem
; timeZone
TIMEZONE = Australia/Melbourne
```
For assistant
```python
@asssiatnt_conf.py
class AssistantConf:
    # grpc host
    GRPC_HOST = '192.168.0.10'

    # grpc port
    GRPC_PORT = '50051'

    # doctor's email
    DOCTOR_EMAIL = 'doctor_1@maps.com'

    #office number
    OFFICE_NUMBER = '110'
```

### 5. Start up the system
For web interface
```shell
# pi @ raspberrypi : source venv/bin/activate
# pi @ raspberrypi : python3 run.py
```
For services
```shell
# pi @ raspberrypi : source venv/bin/activate
# pi @ raspberrypi : python3 run.py
```
For assistant and gRPC
```shell
@ Server
# pi @ raspberrypi : workon cv
# pi @ raspberrypi : X
# pi @ raspberrypi : python3 maps_server.py
```
```shell
@ Client
# pi @ raspberrypi : source google_env/bin/activate
# pi @ raspberrypi : python3 assistant.py
```
------

More details and documentations on folder "\doc" , please check!

Thank you!

Author [@Jason]
2018 年 10月 05日    


