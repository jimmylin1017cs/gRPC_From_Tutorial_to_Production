from concurrent import futures
import grpc
import app_pb2
import app_pb2_grpc

import interceptor
import logging

class CacheServicer(app_pb2_grpc.CacheServicer):

    def __init__(self):
        
        # Creates an insecure Channel to a server.
        channel = grpc.insecure_channel(target='localhost:50050')
        # Intercepts a unary-unary invocation asynchronously.
        intercept_channel = grpc.intercept_channel(channel, interceptor.UnaryUnaryClientInterceptor())
        self.accounts = app_pb2_grpc.AccountsStub(intercept_channel)
        # string: int
        self.keysByAccount = {}
        # string: bytes
        self.store = {}

    def Store(self, request: app_pb2.StoreReq, context: grpc.ServicerContext) -> app_pb2.StoreResp:
        
        accountsCtx = grpc.ServicerContext()
        getByTokenResp = self.accounts.GetByToken(app_pb2.GetByTokenReq(token=request.account_token))

        if request.account_token not in self.keysByAccount:
            self.keysByAccount[request.account_token] = 0

        if self.keysByAccount[request.account_token] >= getByTokenResp.account.max_cache_keys:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details('Account {} exceeds max key limit {}'.format(request.account_token, getByTokenResp.account.max_cache_keys))
            return app_pb2.GetResp()
        
        if request.key not in self.store:
            self.keysByAccount[request.account_token] += 1
        self.store[request.key] = request.val

        return app_pb2.StoreResp()

    def Get(self, request: app_pb2.GetReq, context: grpc.ServicerContext) -> app_pb2.GetResp:

        # Handle Error
        # https://github.com/grpc/grpc/blob/master/doc/statuscodes.md
        if request.key not in self.store:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Key not found {}'.format(request.key))
            return app_pb2.GetResp()

        val = self.store[request.key]
        return app_pb2.GetResp(val=val)

def runServer():

    # Creates an insecure Channel to a server.
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(), interceptors=(interceptor.ServerInterceptor(),))
    app_pb2_grpc.add_CacheServicer_to_server(CacheServicer(), server)
    # Opens an insecure port for accepting RPCs.
    server.add_insecure_port('[::]:50051')
    # Starts this Server.
    server.start()
    # Block current thread until the server stops.
    server.wait_for_termination()

def serverMain():
    
    try:
        runServer()
    except grpc.RpcError as e:
        print(e)


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    
    serverMain()

