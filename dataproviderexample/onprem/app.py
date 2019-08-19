import psycopg2
from flask import Flask
from dataproviderexample.core.dataproviderbase import DataProviderBase
from dataproviderexample.core.greeter import Greeter

app = Flask(__name__)


class DataProvider(DataProviderBase):
    def __init__(self):
        self._conn = psycopg2.connect('dbname=dataproviderdb')

    def get_template(self, language: str) -> str:
        cur = self._conn.cursor()
        cur.execute('select template from templates where language = %s', (language,))
        template, = cur.fetchone()
        return template


data_provider = DataProvider()
greeter = Greeter(data_provider)


@app.route('/<language>/<name>', methods=['GET'])
def greet(language: str, name: str) -> str:
    return data_provider.get_template(language).format(name)


if __name__ == '__main__':
    app.run()
