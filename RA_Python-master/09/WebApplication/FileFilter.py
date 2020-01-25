from pathlib import Path
from typing import Iterable


class FileFilter(object):
    def __init__(self, prefix, extension):
        self._folder_prefix = prefix
        self._file_extension = extension

    def all(self, path: Path) -> Iterable[Path]:
        for folder in path.iterdir():
            if folder.is_dir() and folder.name.startswith(self._folder_prefix):
                yield from (
                    path
                    for path in folder.iterdir()
                    if path.is_file() and path.suffix == f'.{self._file_extension}'
                )
