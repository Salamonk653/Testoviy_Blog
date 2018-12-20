from django.shortcuts import render, get_object_or_404

# Create your views here.
from main.models import Posts


def index(request):
    posts = Posts.objects.all()
    return render(request, 'main/index.html', {'posts':posts})


def index_2(request, pk):
    new = get_object_or_404(Posts, id=pk)
    return render(request, 'main/index_2.html', {'new':new})

def index_3(request, a, b):
    s = str(a)+str(b)
    return render(request, 'main/index_3.html', {'s':s})