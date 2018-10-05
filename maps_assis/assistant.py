# import necessary packages
from __future__ import print_function
import sys
import os
sys.path.append('../web')
from sense_hat import SenseHat
from app.doctor.doctor_services import DoctorService
import aiy.assistant.auth_helpers
from aiy.assistant.library import Assistant
import aiy.audio
import aiy.voicehat
from google.assistant.library.event import EventType
import platform
import subprocess
import grpc
sys.path.append('./grpc')
import maps_pb2
import maps_pb2_grpc

# configration
from assistant_conf import AssistantConf

email = AssistantConf.DOCTOR_EMAIL
host = AssistantConf.GRPC_HOST
port = AssistantConf.GRPC_PORT
office_no = AssistantConf.OFFICE_NUMBER
sense = SenseHat()
is_arrived = '2'
appointment = {}

channel = grpc.insecure_channel('{}:{}'.format(host, port))

def get_next_patient():
    global is_arrived
    global appointment
    global office_no
    ds = DoctorService()
    res, data = ds.getDoctorByEmail(email)
    doctor_id = data['data']['id']
    res, next_patient = ds.getNextPatientByDoctorId(doctor_id)
    if next_patient['code'] == 1:
        # send to another rasppi
        appointment = next_patient['data']
        patient = next_patient['data']['patient']['name']
        text = 'Your next patient is {}, I have already helped you notify the frent desk. Please wait for a moment.'. format(next_patient['data']['patient']['name'])
        aiy.audio.say(text)
        res = grpc_run(patient, office_no)
        is_arrived = res
    else:
        aiy.audio.say('You do not have any appointments yet!')

def edit_notes(notes):
    global is_arrived
    global appointment
    ds = DoctorService()
    if is_arrived == '1':
        ds.editNotes(appointment['id'], notes)
        aiy.audio.say('Successfully added!')
    elif is_arrived == '2':
        aiy.audio.say('Please wait for patient to arrive first!')

def process_event(assistant, event):
    print(event)
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'next patient':
            assistant.stop_conversation()
            get_next_patient()
        if text.find('make a note') != -1:
            assistant.stop_conversation()
            edit_notes(text[19:])

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)

def grpc_run(patient, number):
    global channel
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # host = input("Enter your server's IP address: ") # get the IP address of your Raspberry Pi
    stub = maps_pb2_grpc.MAPS_serverStub(channel)
    response = stub.ValidatePatient(maps_pb2.MAPSRequest(name = patient, office_no = number))
    if response.message == '1':
        text = 'Your patient has already arrived! I will arrange to go your office right away. Please wait for a moment.'
    elif response.message == '2':
        text = 'Your patient has not arrived yet!'
    aiy.audio.say(text)
    return response.message

def main():
    if platform.machine() == 'armv6l':
        print('Cannot run hotword demo on Pi Zero!')
        exit(-1)

    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
