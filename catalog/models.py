from django.db import models

CHOICES_ALBUM_TYPE = (
    ('ALBUM', 'Album'),
    ('SINGLE', 'Single'),
    ('COMPILATION', 'Compilation'),
)


class MusicResource(models.Model):
    """ Generic class for all music-related resource models. """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    spotify_data = models.JSONField(null=True, default=dict)
    custom_data = models.JSONField(null=True, default=dict)

    class Meta:
        abstract = True


class Genre(MusicResource):
    name = models.CharField(unique=True, blank=False, null=False, max_length=512)


class Artist(MusicResource):
    name = models.CharField(blank=False, null=False, max_length=512)
    genres = models.ManyToManyField(Genre, related_name='artists')


class Album(MusicResource):
    name = models.CharField(blank=False, null=False, max_length=1024)
    artists = models.ManyToManyField(Artist, related_name='albums')
    album_type = models.CharField(blank=False, null=False, default=CHOICES_ALBUM_TYPE[0][0], choices=CHOICES_ALBUM_TYPE, max_length=12)
    total_tracks = models.IntegerField(null=False)
    release_date = models.DateField(null=False)


class Track(MusicResource):
    name = models.CharField(blank=False, null=False, max_length=1024)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.PROTECT)
    track_number = models.IntegerField(null=False)
    disc_number = models.IntegerField(null=False, default=1)
    duration_ms = models.IntegerField(null=False)
    explicit = models.BooleanField(null=False, default=False)

    class Meta:
        unique_together = ('album', 'track_number')


class ImageResource(models.Model):
    url = models.CharField(null=False, blank=False, max_length=1024)

    class Meta:
        abstract = True


class ArtistImageResource(models.Model):
    image = models.ImageField(upload_to='downloads/artists/')
    artist = models.ForeignKey(Artist, related_name='images', on_delete=models.PROTECT)


class AlbumImageResource(models.Model):
    image = models.ImageField(upload_to='downloads/albums/')
    album = models.ForeignKey(Album, related_name='images', on_delete=models.PROTECT)
