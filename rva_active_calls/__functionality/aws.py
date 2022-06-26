#%%
import boto3
from os import environ
from io import StringIO
import pandas as pd

class database():

    def __init__(self) -> None:
        self.__session = boto3.Session()

        self.__s3_client = self.__session.client(
            's3',
            aws_access_key_id = environ['AWS S3 Key ID'],
            aws_secret_access_key = environ['AWS S3 KEY'],
            region_name = 'us-east-1'
        )

    def read(self):

        self.database = pd.read_csv(self.__s3_client.get_object(Bucket = 'active-calls', Key='database.csv')['Body'])

        return self
        
    def write(self, data: pd.DataFrame):

        self.__csv_buffer = StringIO()

        self.to_aws = pd.concat([self.database, data]).drop_duplicates()

        self.to_aws.to_csv(self.__csv_buffer, index=False)

        results = self.__s3_client.put_object(Body=self.__csv_buffer.getvalue(), Bucket='active-calls', Key='database.csv')

        if results['ResponseMetadata']['HTTPStatusCode'] == 200:

            print('Uploaded Successfully')
        
        else:

            print('Rut Roh')


# %%
