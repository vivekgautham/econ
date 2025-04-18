
from pathlib import Path 

path = Path(__file__).resolve()

steps = 0
while True:
    path = path.parent
    steps += 1
    if steps > 2:
        break

__path__[0] = str(path / "econlib")