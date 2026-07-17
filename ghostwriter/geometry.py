"""
geometry.py

Modello geometrico interno di GhostWriter.

Tutto il progetto lavora esclusivamente con queste classi.

TESTO
SVG
DXF
QR CODE
LOGHI

↓

Document

↓

GCode
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Point:
    x: float
    y: float


@dataclass(slots=True)
class Path:
    """
    Un tratto continuo.

    La penna viene abbassata sul primo punto,
    percorre tutti i punti,
    poi viene rialzata.
    """

    points: list[Point] = field(default_factory=list)

    def add(self, x: float, y: float):
        self.points.append(Point(float(x), float(y)))

    @property
    def empty(self):
        return len(self.points) == 0

    @property
    def start(self):
        return self.points[0]

    @property
    def end(self):
        return self.points[-1]


@dataclass(slots=True)
class Document:
    """
    Un documento è una collezione di Path.

    Ogni Path rappresenta una linea continua.
    """

    paths: list[Path] = field(default_factory=list)

    def add_path(self, path: Path):

        if not path.empty:
            self.paths.append(path)

    def clear(self):
        self.paths.clear()

    def __len__(self):
        return len(self.paths)
