from dataclasses import dataclass

@dataclass
class MachineConfig:

    bed_width = 200.0
    bed_height = 200.0

    pen_up_z = 5.0
    pen_down_z = 0.0

    travel_feed = 9000
    draw_feed = 3600

    safe_margin = 10.0
