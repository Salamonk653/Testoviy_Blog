from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from main.forms import CommentForm
from main.models import Posts, Comments


def index(request):
    posts = Posts.objects.all()
    return render(request, 'main/index.html', {'posts':posts})


def index_2(request, pk):
    new = get_object_or_404(Posts, id=pk)
    comment = Comments.objects.filter(post=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = new
            form.save()
            return redirect(index_2, pk)
    else:
        form = CommentForm()
    return render(request, 'main/index_2.html', {'new':new, 'comment':comment, 'form':form})

def index_3(request, a, b):
    s = str(a)+str(b)
    return render(request, 'main/index_3.html', {'s':s})