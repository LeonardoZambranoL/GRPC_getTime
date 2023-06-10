import grpc

import getTime_pb2
import getTime_pb2_grpc
from getTime_pb2 import TimeRequest


def run():
    tzDic = {
        "AB": TimeRequest.AB,
        "AD": TimeRequest.AD,
        "ADC": TimeRequest.ADC,
        "AE": TimeRequest.AE,
        "AJ": TimeRequest.AJ,
        "ALA": TimeRequest.ALA,
        "AM": TimeRequest.AM,
        "AS": TimeRequest.AS,
        "ASI": TimeRequest.ASI,
        "AT": TimeRequest.AT,
        "AV": TimeRequest.AV,
        "AW": TimeRequest.AW,
        "CP": TimeRequest.CP,
        "CY": TimeRequest.CY,
        "MBN": TimeRequest.MBN,
        "PST8PDT": TimeRequest.PST8PDT,
        "USP": TimeRequest.USP,
        "USPN": TimeRequest.USPN,
        "EUBlN": TimeRequest.EUBlN,
    }
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = getTime_pb2_grpc.getTimeStub(channel)
        print("Enter a Timezone or enter STP to stop")
        tz = ""
        while str.lower(tz) != "stp":
            tz = input("""AB: America/Boise,
                AD:America/Dawson,
                ADC:America/Dawson_Creek,
                AE: America/Ensenada,
                AJ:America/Juneau,
                ALA:America/Los_Angeles,
                AM:America/Mazatlan,
                AS:America/Sitka,
                ASI:America/Santa_Isabel,
                AT:America/Tijuana,
                AV:America/Vancouver,
                AW:America/Whitehorse,
                CP:Canada/Pacific,
                CY:Canada/Yukon,
                MBN:Mexico/BajaNorte,
                PST8PDT:PST8PDT,
                USP:US/Pacific,
                USPN:US/Pacific-New
                EUBlN:Europe/Berlin,
                """)
            if tz in tzDic:
                time_request = getTime_pb2.TimeRequest(tz=tzDic[tz])
                time = stub.GetTimeAtZone(time_request)
                print(f"Current time in {tzDic[tz]} is {time.hours}:{time.minutes}:{time.seconds}")
            else:
                print("Timezone not supported or invalid")


if __name__ == '__main__':
    run()
