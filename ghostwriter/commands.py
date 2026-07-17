from dataclasses import dataclass


@dataclass
class Move:

    x: float
    y: float


@dataclass
class Line:

    x: float
    y: float


class PenUp:
    pass


class PenDown:
    pass
