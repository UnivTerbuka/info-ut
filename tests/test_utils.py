from info_ut.feed import Feed
from info_ut.utils import get_feed, get_berita, get_pengumuman


def test_get_feed():
    feed = get_feed("https://www.ut.ac.id/pengumuman.xml")
    assert isinstance(feed, Feed)


def test_get_berita():
    feed = get_berita()
    assert isinstance(feed, Feed)


def test_get_pengumuman():
    feed = get_pengumuman()
    assert isinstance(feed, Feed)
