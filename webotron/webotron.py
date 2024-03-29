import boto3
import click

session = boto3.Session(profile_name='raspberry')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-backets')
def list_backets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)
@cli.command('list-backets-objects')
@click.argument('bucket')
def list_backets_objects():
    "List objects in an s3 bucket"
    for obj in s3.Bucket(bucket).objects.all()
        print(obj)

if __name__ == '__main__':
    cli()
