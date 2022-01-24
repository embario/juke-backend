from rest_framework import status
from rest_framework.test import APITestCase

from juke_auth.models import JukeUser


class TestSpotify(APITestCase):
    genre_url = '/api/v1/genres/?external=True'
    artist_url = '/api/v1/artists/?external=True'
    album_url = '/api/v1/albums/?external=True'
    track_url = '/api/v1/tracks/?external=True'


    def test_get_search_artists_ok(self):
        self.client.force_login(JukeUser.objects.create(username='test', password='test'))
        resp = self.client.get(self.artist_url, data={'q': 'test', 'external': True}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(len(resp.data['count']), 5)  # We got something out of spotify.
