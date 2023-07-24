from django.views import generic
from .models import Post
from .forms import PostForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostNew(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/update_post.html"
