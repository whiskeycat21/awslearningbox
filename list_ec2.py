import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='yuzo')
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i)
