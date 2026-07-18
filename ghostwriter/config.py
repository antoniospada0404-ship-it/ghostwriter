"""
config.py

Configurazione della macchina.

Tutte le unità sono espresse in millimetri.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class MachineConfig:
    # ------------------------------------------------------------------
    # Area di lavoro
    # ------------------------------------------------------------------

    bed_width: float = 200.0
    bed_height: float = 200.0

    # Margine di sicurezza
    margin: float = 10.0

    # ------------------------------------------------------------------
    # Penna
    # ------------------------------------------------------------------

    # Penna alzata
    pen_up_z: float = 5.0

    # Penna appoggiata sul foglio
    pen_down_z: float = 0.0

    # Velocità asse Z
    z_feed: int = 1200

    # ------------------------------------------------------------------
    # Movimento XY
    # ------------------------------------------------------------------

    # Movimento rapido (G0)
    travel_feed: int = 9000

    # Movimento di scrittura (G1)
    draw_feed: int = 3600

    # ------------------------------------------------------------------
    # Precisione
    # ------------------------------------------------------------------

    decimals: int = 3
