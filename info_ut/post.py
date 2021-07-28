import attr
from bs4 import BeautifulSoup
from typing import List


@attr.dataclass(slots=True)
class Post:
    title: str
    url: str
    tags: List[str] = attr.field(factory=list)

    @classmethod
    def from_link(cls, link: str):
        pass
