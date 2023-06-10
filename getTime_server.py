from concurrent import futures
from datetime import datetime
import time
import pytz
from zoneinfo import ZoneInfo

import grpc

import getTime_pb2
import getTime_pb2_grpc
from getTime_pb2 import TimeRequest


class GetTimeServicer(getTime_pb2_grpc.getTimeServicer):
    def __init__(self):
        self.tzDic = {
            TimeRequest.AB: 'America/Boise',
            TimeRequest.AD: 'America/Dawson',
            TimeRequest.ADC: 'America/Dawson_Creek',
            TimeRequest.AE: 'America/Ensenada',
            TimeRequest.AJ: 'America/Juneau',
            TimeRequest.ALA: 'America/Los_Angeles',
            TimeRequest.AM: 'America/Mazatlan',
            TimeRequest.AS: 'America/Sitka',
            TimeRequest.ASI: 'America/Santa_Isabel',
            TimeRequest.AT: 'America/Tijuana',
            TimeRequest.AV: 'America/Vancouver',
            TimeRequest.AW: 'America/Whitehorse',
            TimeRequest.CP: 'Canada/Pacific',
            TimeRequest.CY: 'Canada/Yukon',
            TimeRequest.MBN: 'Mexico/BajaNorte',
            TimeRequest.PST8PDT: 'PST8PDT',
            TimeRequest.USP: 'US/Pacific',
            TimeRequest.USPN: 'US/Pacific-New',
            TimeRequest.EUBlN:'Europe/Berlin'
        }

    def GetTimeAtZone(self, request, context):
        requested_time_zone = self.tzDic[request.tz]
        print(requested_time_zone)
        time_at_zone = datetime.now(pytz.timezone(requested_time_zone))
        response = getTime_pb2.TimeOfDay(hours=time_at_zone.hour, minutes=time_at_zone.minute,
                                         seconds=time_at_zone.second)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    getTime_pb2_grpc.add_getTimeServicer_to_server(GetTimeServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("SERVER STARTED")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
