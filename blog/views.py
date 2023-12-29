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
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"
    # slug_url_kwarg = "slug"
    # queryset = Post.objects.all().prefetch_related("tags")

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        stored_posts = request.session.get("stored_posts")

        return render(request, self.template_name, {
            self.context_object_name: post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "saved_for_later": self.is_stored_post(request, post.id),
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
            "saved_for_later": self.is_stored_post(request, post.id),
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
class ReadLaterView(View):
    def get(self, request):
        context = {}
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = Post.objects.filter(id__in=stored_posts)
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
