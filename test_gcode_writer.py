from ghostwriter.geometry import Document, Path
from ghostwriter.machine import MachineProfile
from ghostwriter.gcode_writer import GCodeWriter


def test_gcode_writer_creates_file(tmp_path):

    document = Document()

    path = Path()

    path.add(20, 20)
    path.add(70, 20)
    path.add(70, 70)
    path.add(20, 70)
    path.add(20, 20)

    document.add_path(path)

    machine = MachineProfile()

    output_file = tmp_path / "test_output.gcode"

    writer = GCodeWriter(machine)

    writer.write(
        document,
        output_file
    )

    assert output_file.exists()

    content = output_file.read_text(
        encoding="utf-8"
    )

    assert "G0 X20.000 Y20.000" in content
    assert "G1 X70.000 Y20.000" in content
    assert "G1 X70.000 Y70.000" in content
    assert "G1 X20.000 Y70.000" in content
