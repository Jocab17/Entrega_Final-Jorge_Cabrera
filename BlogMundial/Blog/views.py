from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-fecha']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        like_info = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = like_info.total_likes()
        liked = False

        if like_info.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class AddCommentView(CreateView):
    model = Comentario
    form_class = CommentForm
    template_name = 'add_comment.html'
    #success_url = reverse_lazy('post_details')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AllPostsView(ListView):
    model = Post
    template_name = 'all_posts.html'
    ordering = ['-fecha']

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))

def AcercaDeMiView(request):

    return render(request, 'about.html')