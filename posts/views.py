from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'post.html'

