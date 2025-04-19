
from pathlib import Path 
from logging.config import fileConfig



path = Path(__file__).resolve()
fileConfig(f'{path.parent.parent.parent}/logging.ini')

steps = 0
while True:
    path = path.parent
    steps += 1
    if steps > 2:
        break

__path__[0] = str(path / "econlib")