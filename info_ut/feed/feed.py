import attr
from datetime import datetime
from feedparser import FeedParserDict
from typing import Iterator, List, Optional

from . import FeedItem


@attr.dataclass
class Feed:
    title: str
    link: str
    description: str
    published: datetime
    items: List[FeedItem] = attr.field(factory=list)

    def __attrs_post_init__(self) -> None:
        pass

    def __iter__(self) -> Iterator[FeedItem]:
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    @classmethod
    def from_feed(cls, feed: FeedParserDict) -> "Feed":
        return cls(
            title=feed.feed.title,
            link=feed.feed.link,
            description=feed.feed.description,
            published=datetime(*feed.feed.published_parsed),
        )
