from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

import sample_pb2
import sample_pb2_grpc


class HelloService(sample_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        return sample_pb2.HelloReply(message=f"Hello {request.name}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    service_names = (sample_pb2.DESCRIPTOR.services_by_name["HelloService"].full_name,)
    reflection.enable_server_reflection(service_names, server)
    addr = "[::]:50051"
    server.add_insecure_port(addr)
    print(f"start server: {addr}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
