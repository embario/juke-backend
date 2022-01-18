from rest_framework import status
from rest_framework.test import APITestCase

from juke_auth.models import JukeUser, MusicProfile


class MusicProfileTests(APITestCase):
    base_url = '/api/v1/music-profiles/'

    def test_get_fail_unauthenticated_forbidden(self):
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_authenticated_ok(self):
        user = JukeUser.objects.create(username='test', password='test')
        MusicProfile.objects.create(user=user)
        self.client.force_login(user)
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_music_profile_ok(self):
        user = JukeUser.objects.create(username='test', password='test')
        self.client.force_login(user)

        response = self.client.post(self.base_url, data={
            'name': 'party-time',
            'user': user.id,
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'party-time')
        self.assertEqual(response.data['user'], user.id)
