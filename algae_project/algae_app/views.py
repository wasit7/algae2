from django.shortcuts import render

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