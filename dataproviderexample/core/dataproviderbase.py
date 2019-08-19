from abc import ABC, abstractmethod


class DataProviderBase(ABC):
    @abstractmethod
    def get_template(self, language: str) -> str:
        pass
