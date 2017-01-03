from django.shortcuts import render
from django.views.generic.list import ListView
from .models import RecallImage
# Create your views here.
def blank(request): 
	return render(request,'blank.html', 
		{
			'title':'blank'
		})

def images(request): 
	return render(request,'images.html', 
		{
			'title':'images'
		})

def water(request): 
	return render(request,'water.html', 
		{
			'title':'water'
		})

def prediction(request): 
	return render(request,'prediction.html', 
		{
			'title':'prediction'
		})

class RecallListView(ListView):
    model = RecallImage
    template_name = 'recall_list.html'  # Default: <app_label>/<model_name>_list.html
    #context_object_name = 'recalls'  # Default: object_list
    paginate_by = 5
    queryset = RecallImage.objects.all()  # Default: Model.objects.all()