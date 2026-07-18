"""
machine.py

Profilo della macchina.

Questo modulo gestisce esclusivamente
lo Start GCode e l'End GCode.
"""

from pathlib import Path


class MachineProfile:

    def __init__(
        self,
        start_file="machine/start.gcode",
        end_file="machine/end.gcode",
    ):

        self.start_file = Path(start_file)
        self.end_file = Path(end_file)

    def read_start(self) -> str:

        if not self.start_file.exists():
            raise FileNotFoundError(
                f"Start GCode non trovato:\n{self.start_file}"
            )

        return self.start_file.read_text(
            encoding="utf8"
        )

    def read_end(self) -> str:

        if not self.end_file.exists():
            raise FileNotFoundError(
                f"End GCode non trovato:\n{self.end_file}"
            )

        return self.end_file.read_text(
            encoding="utf8"
        )
