from django.test import TestCase
from django.db.utils import IntegrityError

from catalog.models import Genre


class GenreTests(TestCase):

    def test_create_fail(self):
        Genre.objects.create(name='test-genre')

        with self.assertRaises(IntegrityError):
            Genre.objects.create(name='test-genre')

    def test_create_ok(self):
        Genre.objects.create(name='test-genre')
        Genre.objects.create(name='test-genre-2', custom_data={'some custom data': 1})
        Genre.objects.create(name='test-genre-3', spotify_data={'some spotify data': True})
        self.assertEqual(Genre.objects.count(), 3)
