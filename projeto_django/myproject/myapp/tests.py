from django.test import TestCase
# from unittest import TestCase
from .models import Blog, Entry

# Create your tests here.


class BlogTest(TestCase):

    def setUp(self):
        # CREATE
        self.blog_1 = Blog.objects.create(name='Meu Blog 1')
        self.blog_2 = Blog.objects.create(name='Meu Blog 2')
        self.entry_1 = Entry.objects.create(
            headline='Dia 1', body_text='Hoje o dia foi louco.', pub_date='2019-04-26', blog=self.blog_1)
        self.entry_2 = Entry.objects.create(
            headline='Dia 2', body_text='Hoje o dia não foi.', pub_date='2019-04-27', blog=self.blog_2)
        self.entry_3 = Entry.objects.create(
            headline='Dia 3', body_text='Hoje não teve dia..', pub_date='2019-04-28', blog=self.blog_2)

    def testCrud(self):
        def printar(self):
            print("\n", blogs)
            print("Post", entrys[0], "por", entrys[0].blog)
            print("Post", entrys[1], "por", entrys[1].blog)
            print("Post", entrys[2], "por", entrys[2].blog)

        blogs = Blog.objects.all()
        entrys = Entry.objects.all()
        # entry = Entry.objects.get()

        # ADD
        b = Blog.objects.get(name='Meu Blog 2')
        e = Entry.objects.get(headline='Dia 1')
        b.entry_set.add(e)
        printar(self)

        # Remove e Clear só são possíveis se a Foreign Key for null.
        # REMOVE
        b = Blog.objects.get(name='Meu Blog 2')
        e = Entry.objects.get(headline='Dia 3')
        b.entry_set.remove(e)
        printar(self)

        # CLEAR
        b.entry_set.clear()
        printar(self)
    """
        # SET
        e.related_set.set(headline='Dia Um')
        printar(self)
    """