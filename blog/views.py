from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentForm
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = "-date"


class PostDetailView(View):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"
    # slug_url_kwarg = "slug"
    # queryset = Post.objects.all().prefetch_related("tags")

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, self.template_name, {
            self.context_object_name: post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog:post-detail-page", args=[slug]))

        context = {
            "comment_form": comment_form,
            "post": post,
            "post_tags": post.tags.all(),
        }
        return render(request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context


class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = "-date"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#       "posts": latest_posts
#     })


# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#       "all_posts": all_posts
#     })


# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#       "post": identified_post,
#       "post_tags": identified_post.tags.all()
#     })
