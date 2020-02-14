import grpc
import ntp_pb2
import ntp_pb2_grpc

import datetime
import time

import threading

import ntp_client

ntp_client.delay = 0.0
running = True

def sync():

    channel = grpc.insecure_channel('127.0.0.1:8844')
    stub = ntp_pb2_grpc.NtpStub(channel)

    request = ntp_pb2.NtpRequest()
    while running:
        start = round(time.time() * 1000)
        reply = stub.Query(request)
        m = (round(time.time() * 1000) - start) / 2
        print("RPC call used: ", m * 2, "ms")
        ntp_client.delay = (reply.message / float(1000000) - start - m) / float(1000)
        print("DEBUG: synced")
        time.sleep(5)

def tick():
    while True:
        current = datetime.datetime.now() + datetime.timedelta(0, ntp_client.delay)
        print("Current: ", current)
        time.sleep(1)



if __name__ == "__main__":

    try:
        #sync()
        t = threading.Thread(target=sync)
        t.start()
        tick()
    except KeyboardInterrupt:
        running = False
