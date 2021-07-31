from django.shortcuts import render
from .models import About


# Create your views here.
def blog(request):
    return render(request, 'blogs.html')


def about(request):
    about = About.objects.all()[0]
    context = {
        'about': about,
    }
    return render(request, 'aboutus.html', context)
