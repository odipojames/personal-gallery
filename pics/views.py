from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import *

# Create your views here.
def index(request):
    locations = Places.objects.all()
    images = Image.objects.all()
    cat = Category.objects.all()
    title = "Gallery"
    if 'location' in request.GET and request.GET['location']:
        town = request.GET.get('location')
        pictures = Image.view_image(town)

        return render(request, 'index.html', {'title': title, 'content': pictures})


    elif 'category' in request.GET and request.GET['category']:
        pictures = Image.image_cat(request.GET.get('category'))

        return render(request, 'index.html', {'title': title, 'content': pictures})

    return render(request, 'index.html',{'location': locations, 'content': images, 'category': cat})

def search(request):

    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        pictures = Image.search_image(search_term)

        title = f'{search_term}'
        return render(request,'search.html',{'title': title, 'content': pictures})

    else:
        message = "You haven't searched for any Category"
        return render(request,'search.html')
