from rest_framework import serializers

from juke_auth.models import JukeUser


class JukeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JukeUser
        fields = ['url', 'username', 'email', 'groups', 'is_active']
