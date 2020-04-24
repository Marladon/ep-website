from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Product:
    name: str
    friendly_name: str
    description: str
    picture: str
    technical: List[str]

    def translated(self, tr: Callable[[str], str]):
        return Product(name=self.name,
                       friendly_name=tr(self.friendly_name),
                       description=tr(self.description),
                       picture=self.picture,
                       technical=[tr(x) for x in self.technical])
