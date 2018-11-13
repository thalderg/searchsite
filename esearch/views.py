from django.shortcuts import render
from .es_call import esearch

# Create your views here.



def search_index(request):
	results = []
	name_term = ""
	gender_term = ""
	if request.GET.get('name') and request.GET.get('gender'):
		name_term = request.GET['name']
		gender_term = request.GET['gender']
	elif request.GET.get('name'):
		name_term = request.GET['name']
	elif request.GET.get('gender'):
		gender_term = request.GET['gender']
	search_term = name_term or gender_term
	print("####test#####\n", search_term)
	results = esearch(firstname = name_term, gender=gender_term)
	print(results)
	context = {'results': results, 'count': len(results), 'search_term': search_term }
	return render(request, 'esearch/index.html', context) 

