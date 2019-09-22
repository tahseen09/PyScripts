import boto3

aws_access_key_id = 'access_key_id'
aws_secret_access_key = 'secret'
region_name = 'us-east-1'
ec2 = boto3.client('ec2',aws_access_key_id = aws_access_key_id, 
    aws_secret_access_key = aws_secret_access_key, region_name = region_name)

#spawn EC2 instance
start = ec2.run_instances(ImageId='ami-id', MinCount=1, 
                            MaxCount=1, InstanceType = 't2.large', 
                            SecurityGroupIds=['sg1','sg2',], 
                            DryRun=False)

    instance_id = start['InstanceId']

#stop EC2 instance   
stop = ec2.terminate_instances(InstanceIds=[instance_id,])
