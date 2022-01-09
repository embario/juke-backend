from rest_framework import serializers

from juke_auth.models import JukeUser


class JukeUserSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField(source='auth_token.key')

    class Meta:
        model = JukeUser
        fields = ['url', 'username', 'email', 'groups', 'is_active', 'token']
