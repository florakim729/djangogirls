from django.shortcuts import render
from .models import Post

def post_list(request):
    post_all_data = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':post_all_data})
