from abc import abstractmethod
from typing import Iterable


class DataStorage(object):
    @abstractmethod
    def get_objects(self) -> Iterable[dict]:
        pass

    @abstractmethod
    def get_object(self, key: str) -> dict:
        pass

    @abstractmethod
    def get_any_object(self) -> dict:
        pass

    @abstractmethod
    def put_object(self, key: str, value: dict):
        pass

    @abstractmethod
    def delete_object(self, key: str):
        pass
