from rest_framework import serializers

from juke_auth.models import JukeUser, MusicProfile


class JukeUserSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField(source='auth_token.key')

    class Meta:
        model = JukeUser
        fields = ['url', 'username', 'email', 'groups', 'is_active', 'token']


class MusicProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=JukeUser.objects.all())

    class Meta:
        model = MusicProfile
        fields = "__all__"
