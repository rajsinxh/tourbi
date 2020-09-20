from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = 'cool weather'
    dest1.img = 'download.jpg'
    dest1.price = 900
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Indore"
    dest2.desc = 'clean city'
    dest2.img = 'indore.jpg'
    dest2.price = 700
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Delhi"
    dest3.desc = 'beautiful places'
    dest3.img = 'delhi.jpg'
    dest3.price = 800
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request,"index.html",{'dests':dests})

def contact(request):
    return render(request,"contact.html")
