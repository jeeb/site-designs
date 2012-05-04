#!/usr/bin/env python

from post import Post
from webblog import Webblog

if __name__ == "__main__":
    wb = Webblog("_posts", "source")
    wb.render_posts()
    wb.render_latest_posts(5)
    wb.render_archive()
