from rest_framework import viewsets
from rest_framework import permissions
from juke_auth.serializers import JukeUserSerializer
from juke_auth.models import JukeUser


class JukeUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Juke users to be viewed or edited.
    """
    queryset = JukeUser.objects.all().order_by('-date_joined')
    serializer_class = JukeUserSerializer
    permission_classes = [permissions.IsAuthenticated]
