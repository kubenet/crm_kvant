import sqlite3

from abc import abstractmethod
from typing import Iterable

from pymongo import MongoClient


class DataStorage(object):
    @abstractmethod
    def get_objects(self) -> Iterable:
        pass

    @abstractmethod
    def get_object(self, key: str) -> dict:
        pass

    @abstractmethod
    def put_object(self, key: str, value: dict):
        pass

    @abstractmethod
    def delete_object(self, key: str):
        pass


class MemoryDataStorage(DataStorage):
    def __init__(self):
        self._storage = dict()

    def get_objects(self) -> Iterable:
        return self._storage.values()

    def get_object(self, key: str) -> dict:
        return self._storage.get(key)

    def put_object(self, key: str, value: dict):
        self._storage[key] = value

    def delete_object(self, key: str):
        self._storage.pop(key)


class SqliteDataStorage(DataStorage):
    def __init__(self):
        self._connection = sqlite3.connect('test.db')
        self._cursor = self._connection.cursor()

        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS objects (
                key TEXT, name TEXT, age TEXT, city TEXT, job TEXT
            )
        ''')

    def get_objects(self) -> Iterable:
        self._cursor.execute('SELECT * FROM objects')

        for row in self._cursor:
            yield self.__extract_object(row)

    def get_object(self, key: str) -> dict:
        self._cursor.execute("SELECT * FROM objects WHERE key = ?", key)
        return self.__extract_object(self._cursor.fetchone())

    def put_object(self, key: str, value: dict):
        self.delete_object(key)

        name = value.get('name', str())
        age = value.get('age', -1)
        city = value.get('city', str())
        job = value.get('job', str())

        self._cursor.execute(
            "INSERT INTO objects VALUES (?, ?, ?, ?, ?)",
            (key, name, age, city, job,)
        )

        self._connection.commit()

    def delete_object(self, key: str):
        self._cursor.execute("DELETE FROM objects WHERE key = ? ", key)
        self._connection.commit()

    @staticmethod
    def __extract_object(row):
        return {
            'name': row[1],
            'age': row[2],
            'city': row[3],
            'job': row[4],
        } if row else None


class MongoDataStorage(DataStorage):
    def __init__(self):
        self._client = MongoClient()
        self._db = self._client['testdb']

    def get_objects(self) -> Iterable:
        return (self.__pure_value(value) for value in self._db.objects.find())

    def get_object(self, key: str) -> dict:
        return self.__pure_value(self._db.objects.find_one({'_id': key}))

    def put_object(self, key: str, value: dict):
        value['_id'] = key

        self._db.objects.find_one_and_replace(
            {'_id': key}, value, upsert=True
        )

    def delete_object(self, key: str):
        self._db.objects.delete_one({'_id': key})

    @staticmethod
    def __pure_value(value: dict):
        if value:
            value.pop('_id')

        return value


if __name__ == '__main__':
    storage: DataStorage = MemoryDataStorage()

    storage.put_object('1', {
        'name': 'Alice',
        'age': 25,
        'city': 'Tomsk'
    })

    storage.put_object('2', {
        'name': 'Bob',
        'age': 34,
        'city': 'Moscow',
        'job': 'python developer'
    })

    storage.put_object('3', {
        'name': 'Carlos',
        'age': '19',
        'city': 'Ufa',
    })

    for person in storage.get_objects():
        print(person)

    print()
    print(storage.get_object('2'))
    storage.delete_object('2')
    print(storage.get_object('2'))
