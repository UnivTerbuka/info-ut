import attr
from datetime import datetime


@attr.dataclass(slots=True)
class FeedItem:
    guid: int
    author: str
    title: str
    link: str
    description: str
    published: datetime

    def __attrs_post_init__(self) -> None:
        if isinstance(self.guid, str) and " at https://www.ut.ac.id" in self.guid:
            self.guid = int(str(self.guid).strip(" at https://www.ut.ac.id"))

    @classmethod
    def from_dict(cls, val) -> "FeedItem":
        return cls(
            guid=val.id,
            author=val.author,
            title=val.title,
            link=val.link,
            description=val.description,
            published=datetime(*val.published_parsed),
        )
