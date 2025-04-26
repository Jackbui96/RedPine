import os
from concurrent import futures
import grpc
from protos import model_transfer_pb2, model_transfer_pb2_grpc
from aws_services.s3Client import S3Client

PORT = 6003
s3_client = S3Client()

class Transfer(model_transfer_pb2_grpc.ModelTransferServiceServicer):
    def SendModel(self, request, context):
        model_folder = request.model_folder
        print(f"Received {model_folder} transfer request!")

        local_folder = f"/tmp/{model_folder}"
        os.makedirs(local_folder, exist_ok=True)

        # Check for all files under model folder
        file_keys = s3_client.list_files(prefix=f"{model_folder}/")

        if not file_keys:
            context.abort(grpc.StatusCode.NOT_FOUND, f"{model_folder} is empty.")

        # Download all files
        for s3_key in file_keys:
            if s3_key.endswith("/"):    # skip directories
                continue
            file_name = s3_key.split("/")[-1]
            local_path = os.path.join(local_folder, file_name)
            s3_client.download_file(s3_key, local_path)

        return model_transfer_pb2.TransferStatus(
            success=True,
            message=f"Download successfully to {local_path}"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_transfer_pb2_grpc.add_ModelTransferServiceServicer_to_server(Transfer(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    print(f"docstore service running on port {PORT}...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
