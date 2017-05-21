from django.shortcuts import render

# Create your views here.

def post_list(request):
	return render(request, 'zigApplication/post_list.html',{})