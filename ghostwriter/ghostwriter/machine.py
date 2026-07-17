from pathlib import Path


class MachineProfile:

    def __init__(self):

        self.start = Path("machine/start.gcode")

        self.end = Path("machine/end.gcode")

    def read_start(self):

        return self.start.read_text()

    def read_end(self):

        return self.end.read_text()
