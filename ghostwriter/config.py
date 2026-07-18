from dataclasses import dataclass


@dataclass(slots=True)
class MachineConfig:
    """
    Configurazione della Flying Bear Ghost 5 usata come plotter.
    Tutte le misure sono espresse in millimetri.
    """

    # Area utile
    bed_width: float = 200.0
    bed_height: float = 200.0

    # Margine di sicurezza
    margin: float = 10.0

    # Penna
    pen_up_z: float = 5.0
    pen_down_z: float = 0.0

    # Velocità
    travel_feed: int = 9000      # G0
    draw_feed: int = 3600        # G1

    # Velocità asse Z
    z_feed: int = 1200

    # Precisione numerica
    decimals: int = 3
