from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from rest_framework import viewsets
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer


# Create your views here.

class PostList(ListView):
    template_name = 'blog/post_list.html'
    model = Post


class PostDetail(DetailView):
    template_name = 'blog/post_detail.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, self.template_name, {'post': post})


class PostNew(CreateView):
    template_name = 'blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'


# --- APIs ---


class PostListApi(viewsets.ModelViewSet):
    """
    API endpoint to get a list of posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
