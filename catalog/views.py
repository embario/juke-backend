from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from catalog import serializers, controller
from catalog.models import Genre, Artist, Album, Track


class MusicResourceViewSet(viewsets.ReadOnlyModelViewSet):
    def list(self, request):
        import ipdb; ipdb.set_trace()
        if 'external' in request.GET and bool(request.GET['external']) is True:
            return controller.route(request.path, request.GET['q'])
        return super().list(request)

    def get_object(self):
        if 'external' in request.GET and bool(request.GET['external']) is True:
            return controller.route(self.request.path, pk=self.lookup_field)
        return super().get_object()


class GenreViewSet(MusicResourceViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArtistViewSet(MusicResourceViewSet):
    queryset = Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlbumViewSet(MusicResourceViewSet):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrackViewSet(MusicResourceViewSet):
    queryset = Track.objects.all()
    serializer_class = serializers.TrackSerializer
    permission_classes = [permissions.IsAuthenticated]
