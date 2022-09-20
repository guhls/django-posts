import boto3
import yaml


def get_s3_config():
    with open('__localcode/s3_config.yaml', 'r') as file:
        yaml_data = yaml.safe_load(file)

    return yaml_data


def get_secrets(bucket, key):
    s3 = boto3.client('s3')

    response = s3.get_object(Bucket=bucket, Key=key)

    yaml_data = yaml.safe_load(response['Body'])

    account_sid = yaml_data['auth']['account_sid']
    auth_token = yaml_data['auth']['auth_token']

    return {
        'account_sid': account_sid,
        'auth_token': auth_token,
    }


if __name__ == "__main__":
    s3_config = get_s3_config()
    get_secrets(bucket=s3_config['s3']['bucket'], key=s3_config['s3']['key'])
