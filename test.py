import boto3


s3_client = boto3.client("s3")
s3 = boto3.resource("s3")

def lambda_handler(event, context):
    bucket_names = []
    
    for item in s3_client.list_buckets()["Buckets"]:
        bucket_names.append(item["Name"])
        
    for each_bucket in bucket_names:
        bucket = s3.Bucket(each_bucket)
        
        try:
                
            
            for obj in bucket.objects.all():
                
                try:
                    print(obj)
                except:
                    pass
        except:
                pass

    return