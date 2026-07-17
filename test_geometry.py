from ghostwriter.geometry import *

doc = Document()

p = Path()

p.add(10, 10)
p.add(50, 10)
p.add(50, 50)
p.add(10, 50)
p.add(10, 10)

doc.add_path(p)

print(len(doc))
print(doc.paths[0].start)
print(doc.paths[0].end)
