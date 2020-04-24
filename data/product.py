from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Product:
    name: str
    friendly_name: str
    description: str
    picture: str
    technical: List[str]
