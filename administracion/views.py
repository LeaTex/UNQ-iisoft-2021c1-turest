from django.shortcuts import render

def itemList(request):
	return render(request, 'list.html', {})
