from django.shortcuts import render
from . models import gallery
# Create your views here.
def index(request):
	mygallery = gallery.objects.all()
	context ={
	'mygallery':mygallery,
	}
	return render(request, 'index.html',context)