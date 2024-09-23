from threading import Thread

from Serverapp.ScannerUtils.chestpress import Chestpress


class Starter:
    def __init__(self):
        self.chestpress = Chestpress()

    def exercise_chooser(self, type, source):
        if type.lower() == str("chestpress"):
            self.chestpress.exercise(source)
        else:
            raise ValueError(f"Input {type} and/or {source} is not correct. \n Kindly refer to the documentation")


def start_thread(exercise: str):
    scanner = Starter()
    scanner_thread = Thread(target=scanner.exercise_chooser, args=(exercise, 0))
    scanner_thread.start()


if __name__ == "__main__":
    start_thread("chestpress")
