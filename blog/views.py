from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import CommentForm




def home(request):
    all_post = Post.Newmanager.all()
    return render(request, 'index.html', {'posts':all_post})

def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form  = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'single.html', {'post':post, 'comments':comments, 'comment_form':comment_form})

    
