import sqlite3

from pathlib import Path
from typing import Iterable, List

from .DataStorage import DataStorage
from .FileFilter import FileFilter


class CollectionManager(object):
    class __SqliteDataStorage(DataStorage):
        def __init__(self, filename: str):
            self._connection = sqlite3.connect(filename)
            self._cursor = self._connection.cursor()

        def get_objects(self) -> Iterable:
            self._cursor.execute('SELECT * FROM objects')

            for row in self._cursor:
                yield self.__extract_object(row)

        def get_object(self, key: str) -> dict:
            self._cursor.execute('SELECT * FROM objects WHERE key = ?', (key,))
            return self.__extract_object(self._cursor.fetchone())

        def get_any_object(self) -> dict:
            self._cursor.execute('SELECT * FROM objects ORDER BY RANDOM() LIMIT 1')
            return self.__extract_object(self._cursor.fetchone())

        def put_object(self, key: str, value: dict):
            self.delete_object(key)

            translation = value.get('translation', str())
            transcription = value.get('transcription', str())

            self._cursor.execute(
                'INSERT INTO objects VALUES (?, ?, ?)',
                (key, translation, transcription,)
            )

            self._connection.commit()

        def delete_object(self, key: str):
            self._cursor.execute('DELETE FROM objects WHERE key = ? ', (key,))
            self._connection.commit()

        @staticmethod
        def __extract_object(row):
            return {
                'original': row[0],
                'translation': row[1],
                'transcription': row[2],
            } if row else None

    def __init__(self, path: Path):
        self._collections = {
            self.__basename(path): path
            for path in FileFilter('resources', 'db').all(path)
        }

    def collections(self) -> List[str]:
        return list(self._collections)

    def data_storage(self, collection: str) -> DataStorage:
        return self.__SqliteDataStorage(f'{self._collections[collection]}')

    @staticmethod
    def __basename(path: Path) -> str:
        return path.name.split('.')[0]
