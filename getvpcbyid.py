import boto3

# Create a boto3 client for EC2 service
ec2 = boto3.client('ec2', aws_access_key_id="AKIA42OBUUIF54SCNDGE",
                   aws_secret_access_key="hzuIUT1XtPYYYYVmL3z8suZQ77bBHDNQi2g0nQl", region_name='us-east-2')

# Specify the VPC ID to get details for
# vpc_id = 'vpc-07ec751cf64a1bd87'
vpc_id = input("Enter the vpc id: ")

# Use the describe_vpcs() method to get details of the VPC with the specified ID
response = ec2.describe_vpcs(VpcIds=[vpc_id])

# Get the first VPC from the response
vpc = response['Vpcs'][0]

# Print the VPC details
print("get vpc by id method")
print(f"VPC ID: {vpc['VpcId']}")
print(f"VPC CIDR block: {vpc['CidrBlock']}")
