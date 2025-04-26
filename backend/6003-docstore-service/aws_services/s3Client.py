import boto3

class S3Client:
    def __init__(
            self,
            bucket_name = "red-pine-llm-models",
    ):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def download_file(self, s3_key, local_path):
        """Download a file from S3."""
        self.s3.download_file(self.bucket_name, s3_key, local_path)

    def list_files(self, prefix):
        """List all files in the bucket (optionally under a prefix/folder)."""
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
        if "Contents" in response:
            return [obj["Key"] for obj in response["Contents"]]
        else:
            return []
