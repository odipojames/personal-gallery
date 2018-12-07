from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

# Create your views here.
def index(request):
    try:
        pass
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    return render(request, 'index.html')
