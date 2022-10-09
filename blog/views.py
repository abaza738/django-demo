from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Post
from .forms import PostForm


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

    # def get(self, request, pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     form = PostForm(instance=post)
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request, pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     form = PostForm(request.POST, instance=post)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    #     return render(request, self.template_name, {'form': form})
