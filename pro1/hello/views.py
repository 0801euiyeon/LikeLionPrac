from django.shortcuts import render, get_object_or_404, redirect
from.models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blog':blogs})

def detail(request,blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail':detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/'+str(blog.id))

def delete(request,blog_id):
    get_object_or_404(Blog, pk=blog_id)
    return redirect('/')

def edit(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'edit.html',{'blog':blog})

def update(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.title = request.GET[title]
    blog.body = request.GET[body]
    blog.save()
    return redirect('/detail/' + str(blog.id))