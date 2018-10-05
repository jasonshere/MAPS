# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import maps_pb2 as maps__pb2


class MAPS_serverStub(object):
  """The maps service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ValidatePatient = channel.unary_unary(
        '/MAPS_server/ValidatePatient',
        request_serializer=maps__pb2.MAPSRequest.SerializeToString,
        response_deserializer=maps__pb2.MAPSReply.FromString,
        )


class MAPS_serverServicer(object):
  """The maps service definition.
  """

  def ValidatePatient(self, request, context):
    """Sends a patient
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MAPS_serverServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ValidatePatient': grpc.unary_unary_rpc_method_handler(
          servicer.ValidatePatient,
          request_deserializer=maps__pb2.MAPSRequest.FromString,
          response_serializer=maps__pb2.MAPSReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MAPS_server', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))