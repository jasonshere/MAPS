# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC MAPS server."""
import os
from concurrent import futures
import time

import grpc
from sense_hat import SenseHat

import maps_pb2
import maps_pb2_grpc

from detect import detect

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ValidatePatient(maps_pb2_grpc.MAPS_serverServicer):

    def ValidatePatient(self, request, context):
        if detect(request.name) is True:
            sense_hat = SenseHat()
            text = 'The Doctor office number is {}'. format(request.office_no)
            sense_hat.show_message(text)
            return maps_pb2.MAPSReply(message='1')
        return maps_pb2.MAPSReply(message='2')


def serve():
    host = os.popen('hostname -I').read() # get the IP address of your Raspberry Pi
    print(host)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    maps_pb2_grpc.add_MAPS_serverServicer_to_server(ValidatePatient(), server)
    server.add_insecure_port('{}:50051'.format(host))
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
