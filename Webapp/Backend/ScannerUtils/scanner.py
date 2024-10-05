from threading import Thread

import ScannerUtils.chestpress



def exercise_chooser(type):
    if type.lower() == str("chestpress"):
            ScannerUtils.chestpress.start_loop()
    else:
        raise ValueError(f"Input {type} and/or source is not correct. \n Kindly refer to the documentation")

