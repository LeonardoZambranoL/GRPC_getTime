# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import getTime_pb2 as getTime__pb2


class getTimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTimeAtZone = channel.unary_unary(
                '/getTime.getTime/GetTimeAtZone',
                request_serializer=getTime__pb2.TimeRequest.SerializeToString,
                response_deserializer=getTime__pb2.TimeOfDay.FromString,
                )


class getTimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTimeAtZone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getTimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTimeAtZone': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeAtZone,
                    request_deserializer=getTime__pb2.TimeRequest.FromString,
                    response_serializer=getTime__pb2.TimeOfDay.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getTime.getTime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getTime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTimeAtZone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getTime.getTime/GetTimeAtZone',
            getTime__pb2.TimeRequest.SerializeToString,
            getTime__pb2.TimeOfDay.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)