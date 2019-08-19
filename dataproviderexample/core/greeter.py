from dataproviderexample.core.dataproviderbase import DataProviderBase


class Greeter:
    _data_provider: DataProviderBase

    def __init__(self, data_provider: DataProviderBase):
        self._data_provider = data_provider

    def greet(self, name: str, language: str) -> str:
        template = self._data_provider.get_template(language)
        return template.format(name)
