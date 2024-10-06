from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        caption = request.POST['caption']
        image_link = request.POST['image_link']
        #get the current login user
        user = request.user

        #save the post to the database
        Post.objects.create(caption = caption, image_link = image_link, user = user)

        return redirect('home')
    
    return render(request,'post/add_post.html')