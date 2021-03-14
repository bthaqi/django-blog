from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
