from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post, Comment, Follow, Group
from posts.serializers import (
    PostSerializer, CommentSerializer,
    FollowSerializer, GroupSerializer
)
from .permissions import IsAuthOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthOrReadOnly,
        IsAuthenticatedOrReadOnly
    )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('pub_date',)
    search_fields = ('text',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthOrReadOnly,
        IsAuthenticatedOrReadOnly
    )
    ordering_fields = ('pub_date',)
    pagination_class = None

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post_id')
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
    pagination_class = None


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user.follower.all()
        return Follow.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
