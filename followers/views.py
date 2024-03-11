from rest_framework import generics, permissions
from drf_api.permissions import isOwnerOrReadOnly
from followers.models import Followers
from followers.serializers import FollowerSerializer

class FollowersList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly],
    serializer_class = FollowerSerializer,
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowersDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [isOwnerOrReadOnly],
    serializer_class = FollowerSerializer, 
    queryset = Followers.objects.all()
    