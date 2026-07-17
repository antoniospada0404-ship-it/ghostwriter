from .commands import Move
from .commands import Line
from .commands import PenUp
from .commands import PenDown


def square(x, y, side):

    return [

        PenUp(),

        Move(x, y),

        PenDown(),

        Line(x + side, y),

        Line(x + side, y + side),

        Line(x, y + side),

        Line(x, y),

        PenUp()

    ]
