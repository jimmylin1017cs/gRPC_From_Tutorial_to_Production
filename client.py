from concurrent import futures
import grpc
import app_pb2
import app_pb2_grpc

import interceptor
import logging

def runClient():

    # Creates an insecure Channel to a server.
    channel = grpc.insecure_channel(target='localhost:50051')
    intercept_channel = grpc.intercept_channel(channel, interceptor.UnaryUnaryClientInterceptor())
    cache = app_pb2_grpc.CacheStub(intercept_channel)

    key = 'gopher'
    val = b'con'
    key2 = 'gopher2'
    val2 = b'con2'
    account_token = 'inconshreveable'

    try:
        storeResp = cache.Store(app_pb2.StoreReq(key=key, val=val, account_token=account_token))
    except grpc.RpcError as e:
        print(e)

    try:
        storeResp = cache.Store(app_pb2.StoreReq(key=key2, val=val2, account_token=account_token))
    except grpc.RpcError as e:
        print(e)
    
    try:
        getResp = cache.Get(app_pb2.GetReq(key=key))
        print(getResp.val)
    except grpc.RpcError as e:
        print(e)

    try:
        getResp = cache.Get(app_pb2.GetReq(key='no'))
        print(getResp.val)
    except grpc.RpcError as e:
        print(e)

    print('End')



def clientMain():

    try:
        runClient()
    except grpc.RpcError as e:
        print(e)


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG)
    clientMain()