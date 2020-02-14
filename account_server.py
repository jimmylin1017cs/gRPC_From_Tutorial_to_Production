from concurrent import futures
import grpc
import app_pb2
import app_pb2_grpc

class AccountsServicer(app_pb2_grpc.AccountsServicer):

    def __init__(self):
        

        # string: int
        self.maxCacheKeysByToken = {'inconshreveable': 3}

    def GetByToken(self, request: app_pb2.GetByTokenReq, context: grpc.ServicerContext) -> app_pb2.GetByTokenResp:

        # Handle Error
        # https://github.com/grpc/grpc/blob/master/doc/statuscodes.md
        if request.token not in self.maxCacheKeysByToken:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Token not found {}'.format(request.token))
            return app_pb2.GetByTokenResp()

        max_cache_keys = self.maxCacheKeysByToken[request.token]
        account = app_pb2.Account(max_cache_keys=max_cache_keys)
        return app_pb2.GetByTokenResp(account=account)


def runServer():

    # Creates an insecure Channel to a server.
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor())
    app_pb2_grpc.add_AccountsServicer_to_server(AccountsServicer(), server)
    # Opens an insecure port for accepting RPCs.
    server.add_insecure_port('[::]:50050')
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
    
    serverMain()

