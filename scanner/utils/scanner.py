from scanner.exercies.chestpress import Chestpress


class Starter:
    def __init__(self):
        self.chestpress = Chestpress()

    def rep(self, type, source):
        if type.lower() == str("chestpress"):
            self.chestpress.exercise(source)
        else:
            raise ValueError(f"Input {type} and/or {source} is not correct. \n Kindly refer to the documentation")


if __name__ == "__main__":
    gym = Starter()
    gym.rep("chestpress", "0")
