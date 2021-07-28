import random
from info_ut.post import Post
from info_ut.utils import get_berita


def test_post():
    berita = get_berita()
    feed_item = random.choice(berita.items)
    post = Post.from_link(feed_item.link)
    assert isinstance(post, Post)
