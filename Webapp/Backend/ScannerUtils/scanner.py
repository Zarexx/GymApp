from threading import Thread

from ScannerUtils.chestpress import Chestpress


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
    scanner.exercise_chooser(exercise, 0)
  


if __name__ == "__main__":
    start_thread("chestpress")
