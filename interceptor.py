from concurrent import futures
import grpc
import app_pb2
import app_pb2_grpc

import time
import logging

class UnaryUnaryClientInterceptor(grpc.UnaryUnaryClientInterceptor):

    def intercept_unary_unary(self, continuation, client_call_details, request):

        start_time = time.time() 
        response_future = continuation(client_call_details, request)
        elapsed_time = time.time() - start_time
        logging.debug("invoke server method={} duration={}".format(client_call_details.method, elapsed_time))
        
        return response_future


class ServerInterceptor(grpc.ServerInterceptor):

    def intercept_service(self, continuation, handler_call_details):

        start_time = time.time() 
        response_future = continuation(handler_call_details)
        elapsed_time = time.time() - start_time
        logging.debug("invoke server method={} duration={}".format(handler_call_details.method, elapsed_time))
        
        return response_future
