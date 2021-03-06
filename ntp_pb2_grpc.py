# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ntp_pb2 as ntp__pb2


class NtpStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Query = channel.unary_unary(
        '/ntp.Ntp/Query',
        request_serializer=ntp__pb2.NtpRequest.SerializeToString,
        response_deserializer=ntp__pb2.NtpReply.FromString,
        )


class NtpServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NtpServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=ntp__pb2.NtpRequest.FromString,
          response_serializer=ntp__pb2.NtpReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ntp.Ntp', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
