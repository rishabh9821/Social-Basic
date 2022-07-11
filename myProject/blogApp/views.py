from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from blogApp.models import Post, Comment
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from blogApp.forms import CommentForm, PostForm
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blogApp/postList.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-createdDate')

class MyPostListView(ListView, LoginRequiredMixin):
    model = Post
    pk_url_kwarg = 'post_pk'
    template_name = 'blogApp/myPostList.html'
    login_url = '/login/'
    redirect_field_name = 'blogApp/postList.html'
    success_url = reverse_lazy('blogApp:post-list')
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author__exact = self.request.user).order_by('-createdDate')



class PostDetailView(FormMixin, DetailView):
    template_name = 'blogApp/postDetail.html'
    model = Post
    form_class = CommentForm
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    # ## Login Required Fields
    # login_url = '/login/'
    # redirect_field_name = 'blogApp/postList.html'
    # success_url = reverse_lazy('blogApp:post-list')

    def get_success_url(self):
        return reverse('blogApp:post-detail', kwargs={'post_pk': self.kwargs['post_pk']})
    
    def get_context_data(self, **kwargs):

        ## Previously User
        # context =  super().get_context_data(**kwargs)
        # post = get_object_or_404(Post, pk = self.kwargs['post_pk'])
        # context['form'] = CommentForm(initial={'post': post, 'author': self.request.user})

        ## Now Used
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            # form.save()

            ## Just added lines
            comment = form.save(commit = False)
            post = get_object_or_404(Post, pk = self.kwargs['post_pk'])
            comment.post = post
            comment.author = self.request.user
            comment.save()
            return super(PostDetailView, self).form_valid(form)



### Comment Delete View ###

class CommentDeleteView(DeleteView, LoginRequiredMixin):
    model = Comment
    template_name = 'blogApp/confirmCommentDelete.html'
    pk_url_kwarg = 'comment_pk'

    ## Login Required Fields
    login_url = '/login/'
    redirect_field_name = 'blogApp/postList.html'
    success_url = reverse_lazy('blogApp:post-list')

### Post Create View ###

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'blogApp/createPost.html'
    form_class = PostForm
    pk_url_kwarg = 'post_pk'

    ## Login Required Fields
    login_url = '/login/'
    redirect_field_name = 'blogApp/postList.html'
    success_url = reverse_lazy('blogApp:post-list')

    ## Newly Added Lines to remove author from form
    def form_valid(self, form):
        post = form.save(commit = False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


### Post Update View ###

class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'blogApp/createPost.html'
    form_class = PostForm
    pk_url_kwarg = 'post_pk'

    ## Login Required Fields
    login_url = '/login/'
    redirect_field_name = 'blogApp/postList.html'
    success_url = reverse_lazy('blogApp:post-list')


### Post Delete View ###

class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    template_name = 'blogApp/confirmPostDelete.html'
    pk_url_kwarg = 'post_pk'

    ## Login Required Fields
    login_url = '/login/'
    redirect_field_name = 'blogApp/postList.html'
    success_url = reverse_lazy('blogApp:post-list')










        






