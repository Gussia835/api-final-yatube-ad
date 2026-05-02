from rest_framework import viewsets, filters, permissions
from rest_framework import IsAuthenticatedOrReadOnly
from posts.models import Post, Comment, Follow
from posts.serializers import PostSerializer, CommentSerializer, FollowSerializer
from .permissions import IsAuthOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthOrReadOnly, IsAuthenticatedOrReadOnly) 
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('pub_date', )
    search_fields = ('text', )  


    def perfom_create(self, serializer):
        serializer.save(author=self.request.user)
    

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthOrReadOnly, IsAuthenticatedOrReadOnly)
    ordering_fields = ('pub_date', )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post_id=self.kwargs.get('post_id'))
    

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permissions_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_object = ('following__username', )

    def get_queryset(self):
        user_id = self.request.user.follower.all()

    def perfom_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


