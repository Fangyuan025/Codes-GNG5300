from django.shortcuts import render
from .models import Post

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog_index.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'form': form})

def blog_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(categories=category).order_by('-created_on')
    return render(request, 'blog_category.html', {'category': category, 'posts': posts})