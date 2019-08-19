import boto3
from flask import Flask
from dataproviderexample.core.dataproviderbase import DataProviderBase
from dataproviderexample.core.greeter import Greeter

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')


class DataProvider(DataProviderBase):
    def __init__(self):
        self._table = dynamodb.Table('Templates')

    def get_template(self, language: str) -> str:
        item = self._table.get_item(Key={'Language': language})['Item']
        return item['Template']


data_provider = DataProvider()
greeter = Greeter(data_provider)


@app.route('/<language>/<name>', methods=['GET'])
def greet(language: str, name: str) -> str:
    return data_provider.get_template(language).format(name)


if __name__ == '__main__':
    app.run(port=5001)
