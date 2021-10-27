# This demonstrates the use of 'put_object'
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_versioning



from botocore.config import Config
import boto3
import keyring
import json

with open('params.json', 'r', encoding='utf-8') as f:
	cred = json.load(f)
	acct = cred['put_object_example']['account']
	user = cred['put_object_example']['user']
	reg = cred['put_object_example']["reg"]
	buk = cred['put_object_example']["buk"]
	sig = cred['put_object_example']["sig"]
	key = cred['put_object_example']["key"]
	acl = cred['put_object_example']["ACL"]

passwd = json.loads(keyring.get_password(acct,user))
pub = passwd["access_key_id"]
sec = passwd["secret_access_key"]

conf = Config(
	region_name = reg,
	signature_version = sig
)

client = boto3.client(
	's3',
	aws_access_key_id = pub,
	aws_secret_access_key = sec,
	config = conf
)

test = b'test stuffs'

resp = client.put_object(
	ACL=acl, 				# access control
	Body = test, 			# actual file to send
	Bucket=buk, 			# bucket name
	BucketKeyEnabled=False, # disable encryption
	Key = key 				# file location + name
)

