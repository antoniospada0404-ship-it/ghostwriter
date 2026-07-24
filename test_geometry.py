from ghostwriter.geometry import Document, Path


def test_create_document():
    doc = Document()

    path = Path()

    path.add(10, 10)
    path.add(50, 10)
    path.add(50, 50)
    path.add(10, 50)
    path.add(10, 10)

    doc.add_path(path)

    assert len(doc) == 1
    assert len(doc.paths[0].points) == 5


def test_path_start_and_end():

    path = Path()

    path.add(10, 10)
    path.add(50, 10)
    path.add(50, 50)

    assert path.start.x == 10.0
    assert path.start.y == 10.0

    assert path.end.x == 50.0
    assert path.end.y == 50.0
