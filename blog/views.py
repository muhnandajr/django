from django.shortcuts import render

# Create your views here.
from blog.models import Post, Comments
from blog.forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts" : posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category" : category,
        "posts" : posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    comments = Comments.objects.filter(post=posts)


    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = posts
            )
            comment.save()           

    context = {
        "post" : posts,
        "comments" : comments,
        "form" : form
    }
    return render(request, "blog_detail.html", context)