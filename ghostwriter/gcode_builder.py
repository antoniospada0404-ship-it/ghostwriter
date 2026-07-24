"""
gcode_builder.py

Classe che costruisce il GCode.
Non conosce font, SVG o Document.
Conosce soltanto movimenti della macchina.
"""

from ghostwriter.config import MachineConfig


class GCodeBuilder:

    def __init__(self, cfg: MachineConfig | None = None):

        self.cfg = cfg or MachineConfig()

        self.lines = []

    # -------------------------------------------------
    # utility
    # -------------------------------------------------

    def add(self, line: str):
        self.lines.append(line)

    def blank(self):
        self.lines.append("")

    # -------------------------------------------------
    # header / footer
    # -------------------------------------------------

    def append_text(self, text: str):

        if text:

            self.lines.extend(text.rstrip().splitlines())

    # -------------------------------------------------
    # penna
    # -------------------------------------------------

    def pen_up(self):

        self.add(
            f"G0 Z{self.cfg.pen_up_z:.3f} F{self.cfg.z_feed}"
        )

    def pen_down(self):

        self.add(
            f"G1 Z{self.cfg.pen_down_z:.3f} F{self.cfg.z_feed}"
        )

    # -------------------------------------------------
    # movimenti
    # -------------------------------------------------

    def move(self, x: float, y: float):

        self.add(

            f"G0 X{x:.3f} Y{y:.3f} F{self.cfg.travel_feed}"

        )

    def line(self, x: float, y: float):

        self.add(

            f"G1 X{x:.3f} Y{y:.3f} F{self.cfg.draw_feed}"

        )

    # -------------------------------------------------

    def build(self):

        return "\n".join(self.lines)
