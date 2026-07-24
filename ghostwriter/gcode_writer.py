from pathlib import Path

from .gcode_builder import GCodeBuilder


class GCodeWriter:

    def __init__(self, machine):
        self.machine = machine

    def write(self, document, filename):
        builder = GCodeBuilder()

        # Start G-code
        builder.append_text(
            self.machine.read_start()
        )

        # Disegna ogni percorso
        for path in document.paths:

            if path.empty:
                continue

            # Porta la penna in posizione sicura
            builder.pen_up()

            # Spostamento senza disegnare
            builder.move(
                path.start.x,
                path.start.y
            )

            # Abbassa la penna
            builder.pen_down()

            # Disegna il percorso
            for point in path.points[1:]:

                builder.line(
                    point.x,
                    point.y
                )

            # Rialza la penna
            builder.pen_up()

            builder.blank()

        # End G-code
        builder.append_text(
            self.machine.read_end()
        )

        # Scrive il file
        Path(filename).write_text(
            builder.build(),
            encoding="utf-8"
        )
