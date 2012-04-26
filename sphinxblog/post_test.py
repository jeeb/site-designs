import unittest
import textwrap
from post import Post

class TestPost(unittest.TestCase):

    def setUp(self):
        self.post = Post("sphinxblog/fixtures/2012/05/01/lorem-ipsum.rst")

    def test_date(self):
        self.assertEqual(self.post.date, "01/05/2012")

    def test_title(self):
        self.assertEqual(self.post.title, "Lorem ipsum")

    def test_author(self):
        self.assertEqual(self.post.author, "pigoz")

    def test_abstract(self):
        self.assertEqual(self.post.abstract,
                ("Lorem ipsum dolor sit amet,\n"
                 "consectetur adipisici elit,\nsed eiusmod tempor"))

    def test_body(self):
        self.assertEqual(self.post.body, "test")

if __name__ == '__main__':
    unittest.main()
