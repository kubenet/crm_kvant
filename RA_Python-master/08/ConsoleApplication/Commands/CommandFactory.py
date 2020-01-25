from .AbstractCommand import AbstractCommand
from .EchoCommand import EchoCommand
from .GetProductCommand import GetProductCommand
from .ReadFileCommand import ReadFileCommand


class CommandFactory(object):
    def __init__(self):
        self.commands = [
            EchoCommand(),
            GetProductCommand(),
            ReadFileCommand(),
        ]

    def get_command(self, line: str) -> AbstractCommand:
        for command in self.commands:
            if command.name == line:
                return command
