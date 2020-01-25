import asyncio

from dataclasses import dataclass

from Reminder.ApplicationSettings import application_settings
from Reminder.DataStorage import SqliteDataStorage


@dataclass
class Notification:
    original: str
    translation: str
    transcription: str

    def __init__(self, notification: dict):
        self.original = notification['original']
        self.translation = notification['translation']
        self.transcription = notification['transcription']


class DefaultNotifier(object):
    def send_notification(self, notification: Notification):
        pass


class StdOutputNotifier(DefaultNotifier):
    def send_notification(self, notification: Notification):
        print(notification)


async def main():
    notifiers = {
        'stdout': StdOutputNotifier,
    }

    notifier = notifiers.get(application_settings.notifier, DefaultNotifier)()
    storage = SqliteDataStorage(application_settings.collection)

    while True:
        await asyncio.sleep(application_settings.timeout)
        notifier.send_notification(Notification(storage.get_any_object()))

if __name__ == '__main__':
    asyncio.run(main())
